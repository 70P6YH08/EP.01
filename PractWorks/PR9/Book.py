from turtledemo.sorting_animate import Block


class Book:
    def __init__(self, name_book):
        self.__list_story = []
        self.name_book = name_book
        print(f"Книга {name_book} создана")

    def __del__(self):
        print(f"Книга {self.name_book} удалена")

    def add_story(self, name_story):
        self.__list_story.append(name_story)

    def count_story(self):
        print(len(self.__list_story))

    def book_info(self):
        print(f"Книга: {self.name_book}")
        print("Содержание:")
        counter = 1
        for i in self.__list_story:
            print(f"\t{counter}) {i}")
            counter += 1

book = Book("ACDC")
book.add_story("asd")
book.add_story("zxc")
book.add_story("qwe")
book.add_story("qaz")
book.add_story("wsx")
book.add_story("edc")
book.book_info()
book.count_story()


