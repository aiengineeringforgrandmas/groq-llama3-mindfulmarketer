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

# Load environment variables and enter System Prompt here or in the frontend UI
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
default_system_prompt = os.getenv("DEFAULT_SYSTEM_PROMPT", "You are to act as the Marketing Guru Seth Godin. You are mindful, kind, humorous and passionate just like Seth Godin.")

tracing_enabled = os.getenv("LANGCHAIN_TRACING_V2")  # Default to False if not set
api_key = os.getenv("LANGCHAIN_API_KEY")

# --- Dataset Versioning ---
dataset_version = "1.0"

# --- Initialize Database ---
db_path = os.path.join(os.path.dirname(__file__), "data", "mindfulmarketer-ai.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)
db = DBUtils(db_path)

# --- Function to generate timestamps ---
def get_timestamp():
    return datetime.utcnow().isoformat()

# st.title("MindfulMarketerAI")
# st.image("media/images/blk ms mindfulgrandma 1000x500.png", use_column_width=True)
st.write("Powered by Groq - Llama3 - Langchain - Langsmith - SQlite3 - Streamlit")

st.video("media/videos/v1-720p-mindful-marketer.mp4", loop=True, autoplay=True, muted=True)

# st.sidebar.image("media/images/500x500_Llama3_3Llamas_nobg.png", caption="Llama Power!", use_column_width=True)

# st.sidebar.text("Groq's Ferrari Fast LPU")

st.sidebar.video("media/videos/720-full-final-grog-llama3-cover.mp4", loop=False, autoplay=True, muted=True)

# --- Streamlit App ---
# st.title("MindfulMarketerAI")

# --- User Profile (Example) ---
user_profile = {
    "user_id": "mindfulmarketer_ai",
    "age_range": "30+",
    "technical_proficiency": "intermediate",
    "learning_preferences": "visual_learner"
}

# Ensure user profile is in the database
db.update_user_profile(user_profile)

# --- Conversation History (Fetched from Database) ---
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = get_timestamp()

conversation_history = db.get_conversation_history(st.session_state.conversation_id)

# --- Groq Configuration ---
st.sidebar.title('Llama 3')
model = st.sidebar.selectbox(
    'Choose a Llama 3 model',
    ['llama3-70b-8192', 'llama3-8b-8192', 'llama3-groq-70b-8192-tool-use-preview', 'llama3-groq-8b-8192-tool-use-preview',
     'llama-3.1-8b-instant', 'llama-3.1-70b-versatile', 'llama3-groq-70b-8192-tool-use-preview']
)

# --- API Key Input ---
if not groq_api_key:
    groq_api_key = st.sidebar.text_input("Enter Groq API Key", type="password")
    if not groq_api_key:
        st.warning("Please enter a valid Groq API Key to continue.")
        st.stop()

# --- System Prompt Input ---
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = default_system_prompt

if not default_system_prompt:
    new_system_prompt = st.sidebar.text_area("Enter System Prompt", value=st.session_state.system_prompt, key="new_system_prompt")
    if st.sidebar.button("Enter Prompt"):
        st.session_state.system_prompt = new_system_prompt
else:
    st.sidebar.text_area("Current System Prompt (set in backend)", value=st.session_state.system_prompt, disabled=True)

# Groq rate limits
RATE_LIMITS = {
    'llama3-70b-8192': {'requests_per_minute': 30, 'tokens_per_minute': 6000},
    'llama3-8b-8192': {'requests_per_minute': 30, 'tokens_per_minute': 30000},
    'llama3-groq-70b-8192-tool-use-preview': {'requests_per_minute': 30, 'tokens_per_minute': 15000},
    'llama3-groq-8b-8192-tool-use-preview': {'requests_per_minute': 30, 'tokens_per_minute': 15000},
    'llama-3.1-8b-instant': {'requests_per_minute': 30, 'tokens_per_minute': 131072},
    'llama-3.1-70b-versatile': {'requests_per_minute': 30, 'tokens_per_minute': 131072},
}

# Rate limiting function
def rate_limit(model):
    limit = RATE_LIMITS[model]['requests_per_minute']
    time.sleep(60 / limit)

@traceable
# --- Groq Completion Function ---
def groq_completion(messages, model, **kwargs):
    rate_limit(model)
    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name=model)
    
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content=st.session_state.system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{human_input}")
    ])
    
    conversation = RunnableSequence(prompt | groq_chat)
    
    response = conversation.invoke({
        "chat_history": [HumanMessage(content=m['content']) if m['role'] == 'user' else SystemMessage(content=m['content']) for m in messages[1:-1]],
        "human_input": messages[-1]['content']
    })
    
    return response.content

# --- Display Conversation History ---
for turn in conversation_history:
    with st.chat_message(turn["role"]):
        st.markdown(turn["content"])

# --- Input Box for User's Question ---
if prompt := st.chat_input("Enter your questions here..."):
    # --- Display User Message ---
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Context Management ---
    context = {
        "previous_instructions": conversation_history[-1] if conversation_history else None,
        "user_profile": user_profile,
        "external_information": None
    }    

    # --- Request Metadata ---
    request_metadata = {
        "timestamp": get_timestamp(),
        "source": "mindfulmarketer_aiapp",
        "model_used": model,
        "dataset_version": dataset_version,
        "conversation_id": st.session_state.conversation_id,
        "user_id": user_profile["user_id"],
        "session_context": "learning_about_tech",
        "context": context,
        "tags": {
            "domain": "technology",
            "task": "explaining_concepts",
            "difficulty": "intermediate",
            "user_emotion": "inspired",
            "response_tone": "patient_and_encouraging",
            "requires_clarification": False,
            "feedback": None
        }
    }

    # --- Generate Response ---
    response_text = groq_completion(
        messages=[
            {"role": "system", "content": st.session_state.system_prompt},
            *conversation_history,
            {"role": "user", "content": prompt}
        ],
        model=model,
        metadata=request_metadata
    )

    # --- Display Response ---
    with st.chat_message("assistant"):
        st.markdown(response_text)

    # --- Update Conversation History in Database ---
    db.add_conversation_turn(st.session_state.conversation_id, "user", prompt)
    db.add_conversation_turn(st.session_state.conversation_id, "assistant", response_text)

    # --- Update conversation history for the current session ---
    conversation_history = db.get_conversation_history(st.session_state.conversation_id)

    # --- Save Metadata ---
    db.save_metadata(st.session_state.conversation_id, request_metadata)   


st.sidebar.info("Key Features: Utilizes Advanced Llama 3 AI/LLMs-7 Models to choose from.  Stores conversation history for context-aware interactions. AI observability, tracing, fine-tuning and dataset creation.  Allows exporting conversations in JSONL format."
) 

st.sidebar.link_button("Coded with ❤️ by Gregory Kennedy", "https://github.com/aiengineeringforgrandmas")

# st.sidebar.text("Coded with ❤️ by Gregory Kennedy")
# --- Export to JSONL button ---
if st.button("Export Conversations to JSONL"):
    output_path = os.path.join(os.path.dirname(__file__), "data", "mindfulmarketer_dataset.jsonl")
    db.export_to_jsonl(output_path)
    st.success(f"Exported conversations to JSONL file: {output_path}")
