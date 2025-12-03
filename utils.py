import os
from datetime import datetime

class Utils:
    @staticmethod
    def get_current_time():
        return datetime.now().strftime("%Y.%m.%d %H:%M")
    
    @staticmethod
    def generate_page_number(pages):
        return len(pages) + 1
    
    # @staticmethod
    # def clear_screen():
    #     os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def normalize_text(text):
        return text.strip()

    @staticmethod
    def get_int_input(message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Please enter a valid number! Thanks.")

    @staticmethod
    def line():
        print("-" * 50)

    @staticmethod
    def confirm(message = "Are you sure? (y/n): "):
        answ = input(message).strip().lower()
        return answ == 'y'