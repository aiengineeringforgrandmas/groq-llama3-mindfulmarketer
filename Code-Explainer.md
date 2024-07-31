# Code Explainer Guide for Beginners 

## Import Statements
# app.py

```python
import os
from dotenv import load_dotenv
import streamlit as st
from datetime import datetime
from v2DButils import DBUtils
from langsmith import traceable
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
import time
```

Here's what each import does:

1. `import os`: This module provides a way to use operating system dependent functionality like reading or writing to the file system.

2. `from dotenv import load_dotenv`: This imports the `load_dotenv` function from the `dotenv` library, which helps load environment variables from a `.env` file.

3. `import streamlit as st`: This imports the Streamlit library (aliased as `st`), which is used to create the web application interface.

4. `from datetime import datetime`: This imports the `datetime` class from the `datetime` module, used for working with dates and times.

5. `from v2DButils import DBUtils`: This imports the `DBUtils` class from a custom module named `v2DButils`, which likely handles database operations.

6. `from langsmith import traceable`: This imports the `traceable` decorator from the `langsmith` library, used for tracing and monitoring LangChain applications.

7. `from groq import Groq`: This imports the `Groq` class from the `groq` library, which is likely used to interact with the Groq API.

8. `from langchain_groq import ChatGroq`: This imports the `ChatGroq` class from the `langchain_groq` module, which integrates Groq with LangChain.

9. `from langchain_core.messages import SystemMessage, HumanMessage`: These are classes used to represent different types of messages in a conversation.

10. `from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate`: These are classes used to create and manage chat prompt templates.

11. `from langchain_core.runnables import RunnableSequence`: This imports the `RunnableSequence` class, which is used to create sequences of operations in LangChain.

12. `from langchain.chains.conversation.memory import ConversationBufferWindowMemory`: This imports a class used to manage conversation memory in LangChain.

13. `import time`: This module provides various time-related functions, used here for rate limiting.

---

# 🚀 Installation and Setup Guide

## Prerequisites

Before we begin, ensure you have the following installed:
- Python 3.7 or higher
- Conda (for managing virtual environments)

## Step 1: Create a Conda Environment

1. Open your terminal or command prompt.

2. Create a new Conda environment:

   ```bash
   conda create --name mindfulgrandma-ai python=3.9
   ```

3. Activate the environment:

   ```bash
   conda activate mindfulgrandma-ai
   ```

## Step 2: Clone the Repository

1. Clone the repository (replace with your actual repository URL):

   ```bash
   git clone https://github.com/yourusername/mindfulgrandma-ai.git
   ```

2. Navigate to the project directory:

   ```bash
   cd mindfulgrandma-ai
   ```

## Step 3: Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries including Streamlit, LangChain, Groq, and others.

## Step 4: Set Up Environment Variables

1. Create a `.env` file in the root directory of the project.

2. Add the following variables to the `.env` file:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   DEFAULT_SYSTEM_PROMPT="You are a helpful AI assistant."
   LANGCHAIN_API_KEY=your_langchain_api_key_here
   ```

   Replace `your_groq_api_key_here` and `your_langchain_api_key_here` with your actual API keys.

[IMAGE PLACEHOLDER: Setup_Environment_Variables.jpg]

## Step 5: Prepare the Database

The application uses SQLite for storing conversation history. The database file will be automatically created when you run the application for the first time.

---

Certainly! I'll continue with the next part of the installation guide and begin the Code Explainer Guide for the main code blocks.

---

## Step 6: Run the Application

1. Navigate to the project directory if you're not already there.

2. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

3. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

[IMAGE PLACEHOLDER: Streamlit_Running.jpg]

## Step 7: Using the Application

1. 🔑 If you haven't set the Groq API key in the `.env` file, you'll be prompted to enter it in the frontend UI sidebar.

2. 💬 If you haven't set a default system prompt in the `.app.py` file, you can enter one in the frontend UI sidebar.

3. 🤖 Select a model from the dropdown menu in the sidebar.

4. 💬 Type your questions or prompts in the chat input at the bottom of the page.

5. 📊 To export conversations to a JSONL file, click the "Export Conversations to JSONL" button.

[IMAGE PLACEHOLDER: Application_Interface.jpg]

That concludes the installation and setup guide. Now, let's continue with the Code Explainer Guide for the main code blocks.

---

## Environment Variables and Configuration

```python
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
default_system_prompt = os.getenv("DEFAULT_SYSTEM_PROMPT", "You are a helpful AI assistant.")

tracing_enabled = os.getenv("LANGCHAIN_TRACING_V2")
api_key = os.getenv("LANGCHAIN_API_KEY")

dataset_version = "1.0"
```

Here's what's happening in this code block:

1. `load_dotenv()`: This function loads environment variables from a `.env` file into the environment.

2. `groq_api_key = os.getenv("GROQ_API_KEY")`: This retrieves the Groq API key from the environment variables.

3. `default_system_prompt = os.getenv("DEFAULT_SYSTEM_PROMPT", "You are a helpful AI assistant.")`: This gets the default system prompt from the environment variables. If it's not set, it uses the provided default string.

4. `tracing_enabled = os.getenv("LANGCHAIN_TRACING_V2")`: This checks if LangChain tracing is enabled.

5. `api_key = os.getenv("LANGCHAIN_API_KEY")`: This retrieves the LangChain API key from the environment variables.

6. `dataset_version = "1.0"`: This sets the version of the dataset being used.

## Database Initialization

```python
db_path = os.path.join(os.path.dirname(__file__), "data", "mindfulgrandma-ai.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)
db = DBUtils(db_path)
```

This code block sets up the SQLite database:

1. `db_path = os.path.join(os.path.dirname(__file__), "data", "mindfulgrandma-ai.db")`: This creates the path to the database file. It uses the current file's directory, adds a "data" subdirectory, and specifies the database file name.

2. `os.makedirs(os.path.dirname(db_path), exist_ok=True)`: This creates the directory for the database if it doesn't exist. The `exist_ok=True` parameter prevents an error if the directory already exists.

3. `db = DBUtils(db_path)`: This creates an instance of the `DBUtils` class, which will be used to interact with the database.

## Utility Functions

```python
def get_timestamp():
    return datetime.utcnow().isoformat()
```

This function returns the current UTC time as an ISO formatted string. It's used to generate timestamps for the conversation history.

## Streamlit UI Setup

```python
st.write("Powered by Groq-Llama3-Langchain-Langsmith")
st.image("media/images/blk ms mindfulgrandma 1000x500.png", caption="Llama Power!", use_column_width=True)
st.write("Groq-Llama3-Langchain-Langsmith.")

st.sidebar.image("media/images/500x500_Llama3_3Llamas_nobg.png", caption="Llama Power!", use_column_width=True)
st.sidebar.video("media/videos/grog-llama3-langchain-langsmith-streamlit.mp4", loop=False, autoplay=True, muted=True)

st.title("Ask MindfulGrandaMaAI")
```

This section sets up the main elements of the Streamlit user interface:

1. `st.write()`: These commands write text to the main area of the app.

2. `st.image()`: These display images in the main area and sidebar of the app.

3. `st.sidebar.video()`: This adds a video to the sidebar.

4. `st.title()`: This sets the main title of the app.

---

## Streamlit Sidebar Configuration

```python
if not groq_api_key:
    groq_api_key = st.sidebar.text_input("Enter your Groq API key", type="password")
    if not groq_api_key:
        st.info("Please enter your Groq API key to continue.")
        st.stop()

system_prompt = st.sidebar.text_area("System Prompt", value=default_system_prompt)

selected_model = st.sidebar.selectbox(
    "Select a model",
    ["llama2-70b-4096", "mixtral-8x7b-32768", "llama2-70b-4096"]
)
```

This section sets up the configuration options in the Streamlit sidebar:

1. If the Groq API key isn't set in the environment variables, it prompts the user to enter it in the sidebar. If it's still not provided, it stops the app execution.

2. It creates a text area for the system prompt, pre-filled with the default value.

3. It creates a dropdown menu for selecting the AI model to use.

## Conversation History Management

```python
if "messages" not in st.session_state:
    st.session_state.messages = []

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = str(int(time.time()))

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(k=10, return_messages=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

This code manages the conversation history:

1. It initializes the `messages` list in the session state if it doesn't exist.

2. It creates a unique `conversation_id` based on the current timestamp if it doesn't exist.

3. It initializes a `ConversationBufferWindowMemory` object to store the last 10 messages of the conversation.

4. It displays all previous messages in the chat interface.

## User Input Handling

```python
if prompt := st.chat_input("What is your question?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
```

This section handles user input:

1. It waits for user input in the chat interface.

2. When a prompt is entered, it adds the user's message to the conversation history.

3. It displays the user's message in the chat interface.

## AI Response Generation

```python
@traceable(name="process_message")
def process_message(message: str) -> str:
    llm = ChatGroq(temperature=0.1, model_name=selected_model, groq_api_key=groq_api_key)

    system_message = SystemMessage(content=system_prompt)
    human_message = HumanMessage(content=message)

    prompt = ChatPromptTemplate.from_messages([
        system_message,
        MessagesPlaceholder(variable_name="history"),
        human_message
    ])

    chain = RunnableSequence(
        prompt | llm
    ).with_memory(st.session_state.memory)

    response = chain.invoke({"message": message})
    return response.content

if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = process_message(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
```

This complex section generates the AI's response:

1. The `process_message` function is decorated with `@traceable` for monitoring purposes.

2. Inside `process_message`:
   - It initializes a `ChatGroq` instance with the selected model and API key.
   - It creates system and human messages.
   - It sets up a chat prompt template.
   - It creates a `RunnableSequence` that combines the prompt and the language model.
   - It invokes the chain with the user's message and returns the response.

3. The main code block checks if the last message was from the user. If so:
   - It displays a "Thinking..." spinner.
   - It calls `process_message` to generate a response.
   - It displays the response in the chat interface.
   - It adds the assistant's response to the conversation history.

## Database Operations

```python
db.insert_conversation(
    st.session_state.conversation_id,
    dataset_version,
    get_timestamp(),
    prompt,
    response,
    selected_model
)
```

This code inserts the conversation details into the SQLite database:
- Conversation ID
- Dataset version
- Timestamp
- User's prompt
- AI's response
- Selected model

## Export Functionality

```python
if st.sidebar.button("Export Conversations to JSONL"):
    conversations = db.get_all_conversations()
    jsonl_data = "\n".join([json.dumps(conv) for conv in conversations])
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"conversations_{current_time}.jsonl"
    
    st.sidebar.download_button(
        label="Download JSONL",
        data=jsonl_data,
        file_name=filename,
        mime="application/json"
    )
```

This section adds an export feature:

1. It creates a button in the sidebar to trigger the export.

2. When clicked, it retrieves all conversations from the database.

3. It converts the conversations to JSONL format.

4. It creates a download button for the JSONL file, with a filename including the current timestamp.

---
