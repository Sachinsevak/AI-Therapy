import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")

def get_ai_response(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }

    messages = [
        {"role": "system", "content": "You are a friendly AI therapist. Keep responses empathetic and concise."},
        {"role": "user", "content": user_input}
    ]

    payload = {
        "model": "gpt-oss-120b",
        "messages": messages,
        "max_tokens": 400
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data.get("choices", [{}])[0].get("message", {}).get("content", "No response")


    try:
        result = response.json()
        # If OpenRouter returns error
        if "error" in result:
            return f"OpenRouter API Error: {result['error']}"
        # Normal response
        return result["choices"][0]["message"]["content"]
    except KeyError:
        # Print full response for debugging
        print("OpenRouter response:", result)
        return "Error: Unexpected response from OpenRouter API"
    except Exception as e:
        return f"Error: {str(e)}"
