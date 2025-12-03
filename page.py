from utils import Utils
class Page:
    def __init__(self, title, content, page_number, created_at = None):
        self.title = title.strip()
        self.content = content.strip()
        self.page_number = page_number
        self.created_at = created_at or Utils.get_current_time()
    
    def __str__(self):
        return f"Title: {self.title},\nContent: {self.content},\nCreated at: {self.created_at},\nPage number: {self.page_number}"

    def __repr__(self):
        return f"Page(page_number = {self.page_number}, Title = '{self.title}')"
    
    def to_dict(self):
        return {"page_number": self.page_number, "title": self.title, "content": self.content, "created_at": self.created_at}

    @classmethod
    def from_dict(cls, data):
        return cls(page_number = data["page_number"],title = data["title"],content = data["content"],created_at = data["created_at"])

