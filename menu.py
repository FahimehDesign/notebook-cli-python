from notebook import Notebook
from utils import Utils
from validator import Validator
class Menu:
    def __init__(self, note):
        self.note = note
        self.running = True

    def show_menu(self):
        Utils.line()
        print("1. Add page")
        print("2. Delete page")
        print("3. Edit page")
        print("4. List pages")
        print("5. View page")
        print("6. Save & Exit")
        Utils.line()

    def get_number(self,  number):
        #add page
        if number == 1:
            title = input("Enter title: ") 
            content = input("Enter your content: ")
            self.note.add_note(title, content)
            print(f"The {title} has been added successfully!")

        #delete page
        elif number == 2:
            page_number = Utils.get_int_input("Enter page number to delete: ")
            try:
                self.note.delete_note(page_number)
                print("Page deleted.")
            except (ValueError, IndexError) as e:
                print(e)

        #edit page
        elif number == 3:
            try:
                page_number = Utils.get_int_input("Enter note number to edit: ")
                page = self.note.get_page(page_number)
                if not page:
                    print("page not found.")
                    return
                
                print("\n-----Editing Page-----")
                new_title = input("New title (leave empty to keep old): ")
                new_content = input("New content: ")

                if new_title.strip():
                    page.title = Validator.validate_title(new_title)
                if new_content.strip():
                    page.content = Validator.validate_content(new_content)

                print("Page updated!")

            except ValueError:
                print("Note number doesn't exist.")
        
        #list pages
        elif number == 4:
            pages = self.note.list_pages()
            if not pages:
                print("No pages yet.")
            for num, title in pages:
                print(f"{num}: {title}")

        #view page
        elif number == 5:
            try:
                page_number = Utils.get_int_input("Enter page number to view: ")
                page = self.note.get_page(page_number)

                if page:
                    print("\n=====page=====")
                    print("Title: ", page.title)
                    print("Content: ", page.content)
                    print("Created: ", page.created_at)
                else:
                    print("Page not found!")

            except ValueError:
                print("Please enter a number.")

        #exit
        elif number == 6:
            self.note.save_to_file()
            print("Note saved.Goodbye!")
            self.running = False

        else:
            print("Invalid choice.")

    def run(self):
        while self.running:
            self.show_menu()
            try:
                choice = Utils.get_int_input('Choose an option: ')
                self.get_number(choice)

            except ValueError:
                print('Invalid input. Please enter a number.')
                print()

