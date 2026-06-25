import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import InMemoryVectorStore
from langchain.agents import create_agent
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver

# Load environment variables
load_dotenv()

# --- Page Config ---
st.set_page_config(page_title="Gemini RAG Assistant", layout="centered")
st.title("🤖 Gemini RAG Assistant")

# --- Session State ---
if "document_uploaded" not in st.session_state: st.session_state.document_uploaded = False
if "agent" not in st.session_state: st.session_state.agent = None
if "messages" not in st.session_state: st.session_state.messages = []

# --- Logic: Process Documents ---
def process_document(path):
    loader = PyPDFDirectoryLoader(path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(documents=docs)

    # FIX: Updated to a currently supported embedding model
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    vector_db = InMemoryVectorStore.from_documents(docs, embedding=embeddings)

    @tool
    def retrieve_context(query: str):
        """Retrieve documents relevant to a query from the knowledge base."""
        docs = vector_db.similarity_search(query=query, k=3)
        return "\n\n".join([doc.page_content for doc in docs])

    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
    tools = [retrieve_context]
    
    # Updated agent creation
    memory = InMemorySaver()
    agent = create_agent(
        model=llm,
        tools=tools,
        checkpointer=memory
    )

    st.session_state.agent = agent
    st.session_state.document_uploaded = True

# --- UI: Control Panel ---
with st.sidebar:
    st.header("Control Panel")
    if st.session_state.document_uploaded:
        st.success("Documents Loaded!")
        if st.button("Reset Session"):
            st.session_state.clear()
            st.rerun()

if not st.session_state.document_uploaded:
    uploaded = st.file_uploader(label="Upload PDF Files", type=["pdf"], accept_multiple_files=True)
    if uploaded:
        with st.spinner("Processing documents..."):
            path = "./doc_files/"
            os.makedirs(path, exist_ok=True)
            for file in uploaded:
                with open(os.path.join(path, file.name), "wb") as f:
                    f.write(file.getvalue())
            process_document(path)
            st.rerun()

# --- UI: Chat Interface ---
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if query := st.chat_input("Ask about your documents..."):
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").markdown(query)

        with st.spinner("Gemini is thinking..."):
            # Execute agent
            response = st.session_state.agent.invoke(
                {"messages": [("human", query)]},
                {"configurable": {"thread_id": "session_1"}}
            )
            answer = response["messages"][-1].content
            
        st.chat_message("ai").markdown(answer)
        st.session_state.messages.append({"role": "ai", "content": answer})