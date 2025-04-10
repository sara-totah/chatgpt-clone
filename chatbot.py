import openai
from config import OPENAI_API_KEY, MODEL_NAME

class Chatbot:
    def __init__(self):
        if not OPENAI_API_KEY:
            raise ValueError("OpenAI API key is not set. Please check your .env file.")
        
        openai.api_key = OPENAI_API_KEY
        self.conversation_history = []

    def get_response(self, user_message):
        # Add user message to conversation history
        self.conversation_history.append({"role": "user", "content": user_message})
        
        try:
            # Get response from OpenAI
            response = openai.ChatCompletion.create(
                model=MODEL_NAME,
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=1000
            )
            
            # Extract and store assistant's response
            assistant_message = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": assistant_message})
            
            return assistant_message
            
        except Exception as e:
            error_message = f"Error: {str(e)}"
            self.conversation_history.append({"role": "assistant", "content": error_message})
            return error_message

    def clear_conversation(self):
        self.conversation_history = []

    def get_conversation_history(self):
        return self.conversation_history 