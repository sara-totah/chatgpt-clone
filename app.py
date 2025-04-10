import streamlit as st
from chatbot import Chatbot
from db import ConversationDB
import time

# Initialize session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = Chatbot()
if 'db' not in st.session_state:
    st.session_state.db = ConversationDB()
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_conversation_id' not in st.session_state:
    st.session_state.current_conversation_id = None

# Page config
st.set_page_config(
    page_title="ChatGPT Clone",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("ChatGPT Clone")
    
    if st.button("New Chat"):
        st.session_state.messages = []
        st.session_state.current_conversation_id = None
        st.session_state.chatbot.clear_conversation()
        st.rerun()
    
    st.divider()
    
    # Display saved conversations
    st.subheader("Saved Conversations")
    conversations = st.session_state.db.get_all_conversations()
    for conv in conversations:
        if st.button(conv['title'], key=f"conv_{conv.doc_id}"):
            st.session_state.messages = conv['messages']
            st.session_state.current_conversation_id = conv.doc_id
            st.rerun()

# Main chat interface
st.title("Chat with AI")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display assistant response with typing animation
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Get response from chatbot
        response = st.session_state.chatbot.get_response(prompt)
        
        # Simulate typing animation
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.write(full_response + "▌")
        message_placeholder.write(full_response)
    
    # Add assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Save conversation if it's new
    if not st.session_state.current_conversation_id:
        st.session_state.current_conversation_id = st.session_state.db.save_conversation(
            st.session_state.messages
        )
    else:
        # Update existing conversation
        st.session_state.db.save_conversation(
            st.session_state.messages,
            title=f"Conversation {st.session_state.current_conversation_id}"
        ) 