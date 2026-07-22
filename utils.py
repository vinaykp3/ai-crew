import os

def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is not set."
        )
    print(api_key[:15] if api_key else "No key found")
    return api_key