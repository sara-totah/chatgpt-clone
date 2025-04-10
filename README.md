# ChatGPT Clone with Streamlit

A ChatGPT clone built with Streamlit and OpenAI's API, featuring a modern chat interface and conversation persistence.

## Features

- Modern chat interface with Streamlit
- Real-time chat with OpenAI's GPT models
- Conversation history persistence
- Sidebar navigation for saved conversations
- Typing animation for responses
- New chat functionality

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Application

Run the application with:
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Project Structure

- `app.py`: Main Streamlit application
- `chatbot.py`: OpenAI API interaction logic
- `db.py`: Conversation persistence using TinyDB
- `config.py`: Configuration and environment variables
- `requirements.txt`: Project dependencies

## Usage

1. Start a new chat by clicking the "New Chat" button in the sidebar
2. Type your message in the chat input at the bottom
3. View previous conversations in the sidebar
4. Switch between conversations by clicking on them in the sidebar

## Dependencies

- streamlit==1.32.0
- openai==1.12.0
- python-dotenv==1.0.1
- tinydb==4.8.0 