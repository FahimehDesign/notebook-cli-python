class Validator:
    @staticmethod
    def validate_title(title):
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        return title.strip()
    
    @staticmethod
    def validate_content(content):
        if not content.strip():
            raise ValueError("Content cannot be empty.")
        return content.strip()
    
    @staticmethod
    def validate_page_number(number, max_pages):
        if not isinstance (number, int):
            raise ValueError("Page number must be an integer.")
        
        if number < 1 or number > max_pages:
            raise IndexError("Page number out of range.")
        
        return number