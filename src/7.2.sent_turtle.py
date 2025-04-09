from typing import Dict, List, Optional

class PostOffice:
    """A simple message passing system between users."""
    
    def __init__(self, usernames: List[str]) -> None:
        self.message_id: int = 0
        self.boxes: Dict[str, List[Dict]] = {user: [] for user in usernames}
        
    def send_message(self, sender: str, recipient: str, 
                   title: str, body: str, urgent: bool = False) -> int:
        """Send a message to a recipient's inbox."""
        if recipient not in self.boxes:
            raise KeyError(f"User {recipient} does not exist.")
            
        self.message_id += 1
        message = {
            'id': self.message_id,
            'title': title,
            'body': body,
            'sender': sender,
            'unread': True
        }
        
        if urgent:
            self.boxes[recipient].insert(0, message)
        else:
            self.boxes[recipient].append(message)
            
        return self.message_id

    def read_inbox(self, username, n=None):
        # My notes:
        # - Shows unread messages for a user
        # - Optional 'n' parameter limits number of messages
        # - Marks messages as read when returned
        # - Returns copies to prevent modification
        # - Nice use of list slicing for message limit
        if username not in self.boxes:
            raise KeyError(f"User {username} does not exist.")
            
        unread_msgs = [m for m in self.boxes[username] if m['unread']]
        messages = unread_msgs[:n] if n is not None else unread_msgs
        
        for msg in messages:
            msg['unread'] = False
            
        return [{
            'id': m['id'],
            'title': m['title'],
            'body': m['body'],
            'sender': m['sender'],
            'unread': False
        } for m in messages]

    def search_inbox(self, username, query):
        # My notes:
        # - Searches message content case-insensitively
        # - Returns basic message info without 'unread' status
        # - Good use of string.lower() for case-insensitive search
        # - Returns all matches (no limit parameter)
        # - Simple but effective search implementation
        if username not in self.boxes:
            raise KeyError(f"User {username} does not exist.")
            
        query = query.lower()
        return [{
            'id': m['id'],
            'title': m['title'],
            'body': m['body'],
            'sender': m['sender']
        } for m in self.boxes[username]
            if query in m['title'].lower() or 
               query in m['body'].lower()]
    