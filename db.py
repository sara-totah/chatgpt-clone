from tinydb import TinyDB, Query
from datetime import datetime
from config import DB_PATH

class ConversationDB:
    def __init__(self):
        self.db = TinyDB(DB_PATH)
        self.conversations = self.db.table('conversations')
        self.query = Query()

    def save_conversation(self, messages, title=None):
        if not title:
            title = f"Conversation {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        conversation = {
            'title': title,
            'messages': messages,
            'timestamp': datetime.now().isoformat()
        }
        
        return self.conversations.insert(conversation)

    def get_all_conversations(self):
        return self.conversations.all()

    def get_conversation(self, conversation_id):
        return self.conversations.get(doc_id=conversation_id)

    def delete_conversation(self, conversation_id):
        self.conversations.remove(doc_ids=[conversation_id])

    def update_conversation_title(self, conversation_id, new_title):
        self.conversations.update({'title': new_title}, doc_ids=[conversation_id]) 