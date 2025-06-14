import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With Ollama"

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

# Response generation function
def generate_response(question, llm_model, temperature, max_tokens):
    llm = Ollama(model=llm_model, temperature=temperature, num_predict=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Title of the app
st.title("Enhanced Q&A Chatbot With Ollama")

# Sidebar parameters
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Callback function for processing input
def process_input():
    user_input = st.session_state.user_input
    response = generate_response(user_input, "llama3.2", temperature, max_tokens)
    st.session_state.chat_history.append((user_input, response))
    st.session_state.user_input = ""  # Clear input after processing

st.write("Go ahead and ask any question:")

# Input box with on_change callback
st.text_input("You:", key="user_input", on_change=process_input)

# Display chat history
for question, answer in st.session_state.chat_history:
    st.write(f"**You:** {question}")
    st.write(f"**Bot:** {answer}")
