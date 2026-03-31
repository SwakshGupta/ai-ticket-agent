# memory/chat_memory.py

class ChatMemory:
    def __init__(self):
        self.history = []

    def add(self, user, response):
        self.history.append({"user": user, "response": response})

    def get_history(self):
        return self.history