# 🚀 Installation, Setup, and User Guide

## 📋 Prerequisites

Before we begin, ensure you have the following installed:
- 🐍 Python 3.7 or higher
- 🐼 Conda (for managing virtual environments)

[IMAGE PLACEHOLDER: prerequisites.jpg]

## 🛠️ Installation and Setup

### Step 1: Create a Conda Environment

1. 🖥️ Open your terminal or command prompt.

2. 🌟 Create a new Conda environment:

   ```bash
   conda create --name mindfulmarketer-ai python=3.9
   ```

3. ✅ Activate the environment:

   ```bash
   conda activate mindfulmarketer-ai
   ```

[IMAGE PLACEHOLDER: conda_setup.jpg]

### Step 2: Clone the Repository

1. 📂 Clone the repository:

   ```bash
   git clone https://github.com/yourusername/mindfulmarketer-ai.git
   ```

2. 📁 Navigate to the project directory:

   ```bash
   cd mindfulmarketer-ai
   ```

[IMAGE PLACEHOLDER: git_clone.jpg]

### Step 3: Install Dependencies

📦 Install the required packages using pip:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries including:
- 🌊 Streamlit
- 🔗 LangChain
- 🤖 Groq
- 🗄️ SQLite
- And more!

[IMAGE PLACEHOLDER: pip_install.jpg]

### Step 4: Set Up Environment Variables

1. 📝 Create a `.env` file in the root directory of the project.

2. 🔑 Add the following variables to the `.env` file:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   DEFAULT_SYSTEM_PROMPT="You are a helpful AI assistant."
   LANGCHAIN_API_KEY=your_langchain_api_key_here
   ```

   Replace `your_groq_api_key_here` and `your_langchain_api_key_here` with your actual API keys.

[IMAGE PLACEHOLDER: env_setup.jpg]

### Step 5: Prepare the Database

🗃️ The application uses SQLite for storing conversation history. The database file will be automatically created when you run the application for the first time.

[IMAGE PLACEHOLDER: sqlite_setup.jpg]

## 🚀 Running the Application

1. 📂 Navigate to the project directory if you're not already there.

2. 🏃‍♂️ Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

3. 🌐 Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

[IMAGE PLACEHOLDER: streamlit_running.jpg]

## 🎮 Using the Application

### Initial Setup

1. 🔑 If you haven't set the Groq API key in the `.env` file, you'll be prompted to enter it in the sidebar.

2. 💬 If you haven't set a default system prompt in the `.env` file, you can enter one in the sidebar.

3. 🤖 Select a model from the dropdown menu in the sidebar:
   - llama2-70b-4096
   - mixtral-8x7b-32768
   - llama2-70b-4096

[IMAGE PLACEHOLDER: app_setup.jpg]

### Chatting with mindfulmarketerAI

1. 💬 Type your questions or prompts in the chat input at the bottom of the page.

2. 🤔 The AI will process your input and provide a response.

3. 📜 The conversation history will be displayed in the main chat area.

[IMAGE PLACEHOLDER: chat_interface.jpg]

### Exporting Conversations

1. 📊 To export conversations to a JSONL file, click the "Export Conversations to JSONL" button in the sidebar.

2. 💾 Click the "Download JSONL" button that appears to save the file to your computer.

[IMAGE PLACEHOLDER: export_conversations.jpg]

## 🔧 Troubleshooting

- 🔑 If you encounter API key errors, double-check your `.env` file and ensure the keys are correctly entered.
- 🌐 If the application doesn't start, make sure all dependencies are installed and you're in the correct Conda environment.
- 💾 If the database isn't created, check that you have write permissions in the project directory.

[IMAGE PLACEHOLDER: troubleshooting.jpg]

## 🆘 Getting Help

If you encounter any issues or have questions:
- 📚 Check the project's documentation
- 🐛 Open an issue on the GitHub repository
- 📧 Contact the project maintainers

[IMAGE PLACEHOLDER: getting_help.jpg]

---

That concludes the installation, setup, and instruction guide for mindfulmarketerAI. This guide uses emojis for visual appeal and includes placeholders for images. You can replace these placeholders with actual screenshots or diagrams to make the guide even more engaging and informative.
