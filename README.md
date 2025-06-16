# 🤖 Enhanced Q&A Chatbot with Ollama + LangChain + Streamlit

This project is a **local Q&A chatbot app** powered by:

- **[Ollama](https://ollama.com/)** (to run LLMs like LLaMA 3 locally),
- **LangChain** (to chain the prompt and model),
- **Streamlit** (to build a simple chat interface).

It allows users to interact with a local large language model and get helpful responses directly from their own machine.

---

## 📦 Features

- Chat with a local model like `llama3` (via Ollama).
- Adjustable **temperature** and **max token** limits via sidebar.
- Maintains chat history within the Streamlit session.
- Fully local — no need for external API keys or internet inference.

---

## 🧠 Tech Stack

- `streamlit` – front-end interface
- `langchain` – chaining prompt → model → output
- `ollama` – local LLM backend (e.g., Meta's LLaMA 3)
- `python-dotenv` – load environment variables from `.env`

---

## 🚀 Setup Instructions

### 1. Prerequisites

Make sure you have the following installed **locally**:

- Python 3.8+
- [Ollama](https://ollama.com/download) (macOS/Linux/Windows)
- Git (optional)

