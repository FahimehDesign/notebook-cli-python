import json
import os

class FileManager:
    def __init__(self, file_name = "notes.json"):
        self.file_name = file_name

        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", encoding = "utf-8") as file:
                json.dump([], file, ensure_ascii= False, indent=4)


    def save(self, page_list):
        """page list is a list of dictionary"""

        with open(self.file_name, "w", encoding = "utf-8") as file:
                json.dump(page_list, file, ensure_ascii=False, indent= 4)


    def load(self):
        """محتویاتفایل را میخواند و یک لیست از دیکشنری ها را برمیگرداند"""
        if not os.path.exists(self.file_name):
            return []
        
        with open(self.file_name, "r", encoding = "utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  #اگر فایل خراب بود