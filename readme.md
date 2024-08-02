## Powered by Groq - Llama3 - Langchain - Langsmith - Streamlit - SQlite3  
![github-mindfulmarketing-ai](https://github.com/user-attachments/assets/025b20d7-afae-4364-9ee7-7c3b8668e9d0)

#  MindfulMarketer: Your AI Marketing Guru
Need a marketing mentor who's always got your back, offering insightful advice with a touch of Seth Godin's wisdom? Look no further! MindfulMarketerAI is a cutting-edge chatbot application that combines the speed of Groq, the intelligence of Llama 3, and a dash of marketing magic to help you navigate the ever-evolving world of marketing.

## Why Groq and Llama 3?
![10mb-groq-llama3-langchain-langsmith-sqlitedb](https://github.com/user-attachments/assets/8411f41c-5a68-4355-88f3-7f57d32ef00b)

* **Unmatched Speed and Performance:** Groq's hardware and software are specifically designed to accelerate LLM inference, making it the perfect platform for running demanding models like Llama 3. This translates into snappy responses and a smooth user experience.

![500x500_Llama3_3Llamas_nobg](https://github.com/user-attachments/assets/125a6281-e7cb-4a9d-b90a-5beaff5e23ad)

* **Open and Accessible AI:**  Llama 3's open-weight release has democratized access to cutting-edge AI capabilities. By combining Llama 3 with Groq, we're making it easier than ever for developers and marketers to build powerful AI-driven applications.

# 🛠️ Why Langchain, Langsmith, SQLite3 and Streamlit?

MindfulMarketerAI leverages a powerful combination of tools to create an efficient, intelligent marketing assistant:

## Langchain: One Framework, Infinite Use Cases
![1920x738-LangChain-logo-parrot-blk-text](https://github.com/user-attachments/assets/94266e6c-e626-4226-bba0-e645c51c6a5c)

Langchain is a versatile framework that connects Large Language Models (LLMs) to your company's private data and APIs, enabling context-aware, reasoning applications. It offers:

- 📊 Built-in ingestion and retrieval methods to augment LLM knowledge with company or user data
- 🔗 Comprehensive integrations and state-of-the-art techniques for building Retrieval-Augmented Generation (RAG) systems
- 🚀 Rapid prototyping and production deployment capabilities
- 🧩 Infinite composability for creating custom AI-powered workflows
https://github.com/user-attachments/assets/4e997174-05e8-43f7-a70b-24f6ea5a9fd0

## 🔍 Langsmith: LLM Application Lifecycle Management

![langchain_stack_dark](https://github.com/user-attachments/assets/017781c8-f08b-43e8-a02c-d0ea9eecc008)

Langsmith is an all-in-one developer platform designed for every stage of LLM-powered application development. Key features include:

- 🐞 Real-time debugging and performance optimization
- 👥 Collaboration tools for sharing chain traces
- 📝 Hub for crafting, versioning, and commenting on prompts
- 🏷️ Annotation Queues for human labeling and feedback
- 📊 Dataset creation for evaluations, few-shot prompting, and fine-tuning
- 🧪 Comprehensive testing and evaluation capabilities, including AI-assisted evaluation

![2-Langsmith-aiengineeringforgrandmas](https://github.com/user-attachments/assets/1f68ae84-3986-4aa2-aefc-1543526698b3)

## 💾 SQLite3: Embedded Database Power

![v1-logo-sqlite](https://github.com/user-attachments/assets/f4a1b724-d810-4670-a89f-96441808a30a)

SQLite3 is a software library that implements a small, fast, self-contained, full-featured SQL database engine. It offers:

- 📁 The ability to store structured data in a single database file
- 🔒 High reliability and cross-platform compatibility
- 📱 Widespread use across mobile phones, computers, and numerous applications
- 🔄 A stable file format pledged to remain backwards compatible through 2050
- 🔀 Suitability for transferring rich content between systems and long-term data archival

## 🌈 Streamlit: Rapid AI Application Development
![logo-streamlit](https://github.com/user-attachments/assets/b818f12a-7cc3-4edb-bc69-8e82fbaa4bce)

Streamlit provides an intuitive framework for building interactive web applications with minimal code, allowing us to focus on delivering a seamless user experience.

# 🌟 Key Features of MindfulMarketerAI:

1. 🤖 Utilizes 7 advanced Llama 3 AI/LLM models, each optimized for specific marketing tasks
2. 💬 Stores conversation history for context-aware interactions
3. 👁️ Enables AI observability and tracing through Langsmith integration
4. 🎛️ Supports fine-tuning and custom dataset creation
5. 📤 Allows exporting conversations in JSONL format for further analysis or AI training

By combining these powerful tools, MindfulMarketerAI offers a comprehensive solution for AI-driven marketing assistance.

**The Future of AI in Marketing**

We believe that AI has the potential to revolutionize marketing as we know it. By combining human creativity with the power of AI, we can create more effective, personalized, and engaging marketing campaigns. MindfulMarketerAI is just one example of what's possible when we embrace the potential of AI in this exciting field. 

## ✨ Features

* **Groq-Powered Speed:** Experience lightning-fast responses thanks to Groq's high-performance compute infrastructure. 

* **Llama 3 Intelligence:**  Benefit from the advanced reasoning and language generation capabilities of Llama 3, one of the most powerful large language models available.

* **Choice of Llama 3 Models:** Experiment with different Llama 3 models, each optimized for specific tasks, and find the perfect fit for your marketing needs.

* **Context-Aware Conversations:**  MindfulMarketerAI remembers your past interactions, ensuring that each response is relevant and personalized.

* **Easy Export for Analysis and Fine/Tuning:** Download your conversations in JSONL format, making it simple to use for fine-tuning an AI/LLM.

* **LangSmith for Tracing (Recommended):** LangSmith is a tool for observing, debugging, dataset creation, cost analysis and improving your AI/LLM applications. 

## 🚀 Quickstart

### 1. Set Up Your Environment

We'll be using `conda` for a smooth environment setup. If you don't have it, grab the Miniconda installer from [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html).

1. **Create a Conda Environment:**
   ```bash
   conda create -n mindfulmarketer-ai python=3.11  
   conda activate mindfulmarketer-ai
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### 2. Get Your API Keys Ready

1. **Obtain a Groq API Key:**
   * Head over to [https://groq.com/](https://groq.com/) and sign up for a free account.
   * Navigate to your account settings and generate a new API key.

2. **(Optional) LangSmith for Tracing (Recommended):**
    * LangSmith is a fantastic tool for observing, debugging, and improving your LLM applications. Sign up for a free account at [https://smith.langchain.com/](https://smith.langchain.com/).
    * Create a new project in LangSmith and retrieve your API key.

### 3. Configure Your `.env` File

1. **Create a `.env` File:**
   Create a file named `.env` in the root directory of your project.

2. **Add Your API Keys:**
   Paste the following lines into your `.env` file, replacing the placeholders with your actual Groq and (optionally) LangSmith API keys:
   ```
   GROQ_API_KEY=your_groq_api_key
   LANGCHAIN_TRACING_V2=true  # Enable=true if you're using LangSmith
   LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
   LANGCHAIN_API_KEY=your_langsmith_api_key 
   LANGCHAIN_PROJECT=projectname 
   ```

### 4. Launch the App

1. **Navigate to Your Project Directory:**
   ```bash
   cd /path/to/your/mindfulmarketer-ai/directory 
   ```
2. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

That's it! Your MindfulMarketerAI app should now be up and running in your web browser. 

```
## 🚀 Usage

1. **Choose Your Llama 3 Model:**  On the sidebar, you'll see a dropdown menu where you can select from a variety of Llama 3 models. Each model has its strengths and weaknesses, so feel free to experiment!

2. **(Optional) Craft Your System Prompt:** The system prompt sets the stage for your AI marketing guru's personality and expertise.  You can customize this prompt to influence the tone and style of the responses.

3. **Start Chatting!**  Type your marketing questions, challenges, or ideas into the chat interface. MindfulMarketerAI will respond with thoughtful insights and advice, drawing upon the vast knowledge of Llama 3 and the speed of Groq.

4. **Review and Export Conversations:**  Your conversation history is automatically saved. You can export it to a JSONL file for further analysis or to share your AI-powered marketing journey with others.

## 💡 Behind the Design: A Peek Under the Hood

Let's take a closer look at some of the key design decisions that make MindfulMarketerAI tick:

* **Groq for LLM Inference:** Groq's AI platform is purpose-built to deliver blazing-fast inference for large language models like Llama 3. By leveraging Groq, we ensure that you get responses in the blink of an eye, even for complex queries.

* **Langchain for Workflow Orchestration:** Langchain is our secret weapon for managing the complexities of interacting with LLMs. It provides a streamlined way to handle prompts, chain together different components, and manage conversation history.

* **SQLite3 for Lightweight Persistence:** We use SQLite3, a serverless database engine, to store your conversation history. This allows for easy data management without the overhead of a full-blown database server. 

* **LangSmith for Observability (Optional):**  If you choose to enable LangSmith, you'll gain valuable insights into your LLM application. Track conversations, debug issues, and monitor performance all within LangSmith's intuitive interface.

## 🧠 Why This Matters: The Power of AI in Marketing

In today's fast-paced marketing landscape, staying ahead of the curve is paramount. AI is rapidly transforming how we approach marketing, offering:

* **Data-Driven Insights:**  AI can analyze vast amounts of data to uncover hidden patterns and trends, providing valuable insights to inform your marketing strategies.

* **Personalized Experiences:**  AI enables you to create highly targeted and personalized marketing campaigns that resonate with your audience on a deeper level.

* **Increased Efficiency and Productivity:**  Automate repetitive tasks, freeing up your time and resources to focus on more strategic initiatives.

MindfulMarketerAI is your gateway to harnessing the power of AI in your marketing endeavors. 
```

```
## 🙌 Contributing

We believe in the power of community! If you're passionate about AI and marketing, we'd love for you to contribute to MindfulMarketerAI. Here's how you can get involved:

1. **Fork the Repository:** Click the "Fork" button at the top right of this page to create your own copy of the repository.

2. **Create a New Branch:**  Make your changes in a separate branch to keep things organized.
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit Your Changes:** Add clear and concise commit messages to explain your work.
   ```bash
   git commit -m "Add your descriptive commit message here"
   ```
4. **Push to Your Fork:** Send your changes to your forked repository on GitHub.
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request:**  Submit a pull request to the main repository, describing your changes and their benefits.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

