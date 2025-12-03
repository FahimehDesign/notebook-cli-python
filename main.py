from menu import Menu
from notebook import Notebook

if __name__ == '__main__':
    notebook = Notebook("noteBook.json")
    menu = Menu(notebook)
    menu.run()