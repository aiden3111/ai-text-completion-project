# AI Text Completion Project

This is a Python-based application that uses OpenAI's GPT-3.5 model to generate text completions from user-provided prompts. It demonstrates how generative AI can be used in creative, educational, and practical contexts.

## 🔧 Features

- Accepts natural language input from the user.
- Sends the prompt to OpenAI's GPT-3.5 model.
- Displays a coherent, AI-generated response.
- Allows user control over creativity using the `temperature` setting.
- Supports repeated input sessions with graceful exits and error handling.

## 🚀 Setup Instructions

1. **Clone the repository** (or download files manually):

    ```bash
    git clone https://github.com/your-username/ai-text-completion-project.git
    cd ai-text-completion-project
    ```

2. **Install the required libraries**:

    ```bash
    pip install openai python-dotenv
    ```

3. **Set up your `.env` file**:

    Create a `.env` file in the project root directory and paste your OpenAI API key:

    ```
    OPENAI_API_KEY=your_openai_key_here
    ```

4. **Run the application**:

    ```bash
    python text_completion_app.py
    ```

## 📝 Example Prompts

Try these:

- `Write a haiku about the ocean.`
- `Explain photosynthesis like I’m 10.`
- `Summarize the plot of The Matrix.`
- `Continue this story: "It was a stormy night, and the power went out..."`
- `List 3 pros and cons of AI in education.`

## ⚙️ Parameters

- **Temperature**: Controls creativity (range 0.0–1.0). Higher values = more random, lower = more focused.
- **Max Tokens**: Defines how long the output can be. Default is 100.

## 🔐 API Key Safety

**Do not share your API key publicly!**  
Your `.env` file should never be uploaded to GitHub. Add it to your `.gitignore`.

## 📄 Files Included

- `text_completion_app.py` – Main Python script.
- `.env` – (Not included) Securely stores your OpenAI key.
- `README.md` – This file.
- `project_report.docx` – Project summary and evaluation results.

## 📚 License

This project is for educational purposes and follows the guidelines of the Cognizant GenAI capstone project.
