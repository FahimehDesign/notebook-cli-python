from page import Page
from fileManager import FileManager
from utils import Utils
from validator import Validator

class Notebook:
    def __init__(self, file_name = 'notes.json'):
        self.pages = []
        self.file_manager = FileManager(file_name)
        self.load_from_file()
        

    def add_note(self, title, content):
        title = Validator.validate_title(title)
        content = Validator.validate_content(content)
        page_number = Utils.generate_page_number(self.pages)
        note = Page(title, content, page_number, Utils.get_current_time())
        self.pages.append(note)
        self.save_to_file()

    def delete_note(self, number):
        number = Validator.validate_page_number(number, len(self.pages))
        self.pages.pop(number-1)

        for index, page in enumerate(self.pages):
            page.page_number = index + 1
        self.save_to_file()


    def get_page(self, number):
        if number < 1 or number > len(self.pages):
            return None
        return self.pages[number-1]

    def list_pages(self):
        return [(page.page_number , page.title) for page in self.pages]

    def save_to_file(self):
        """صفحه ها را تبدیل به list of dict میکنیم"""
        data = [page.to_dict() for page in self.pages]
        self.file_manager.save(data)

    def load_from_file(self):
        data = self.file_manager.load()
        self.pages = [Page.from_dict(item) for item in data]