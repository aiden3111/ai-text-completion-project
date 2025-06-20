import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Explicitly set up OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_completion(prompt, temperature=0.7, max_tokens=100):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to the OpenAI GPT-3.5 Text Completion App!")
    while True:
        prompt = input("\nEnter your prompt (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            print("Goodbye!")
            break
        if not prompt.strip():
            print("Empty input. Try again.")
            continue
        temperature = input("Enter temperature (0.0–1.0, press enter for 0.7): ")
        try:
            temperature = float(temperature) if temperature else 0.7
        except ValueError:
            temperature = 0.7
        print("\nAI Response:\n")
        print(generate_completion(prompt, temperature))

if __name__ == "__main__":
    main()
