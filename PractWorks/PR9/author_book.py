import Author
import Book


class AuthorBook(Author.Author, Book.Book):
    def print_full_name(self):
        print(self.full_name)
        print(self.name_book)
        print("Содержание:")
        for i, name_story in self.__list_story:
            print(f"{i}) {name_story}")

# class Book:
#     def __init__(self, name_book):
#         self.__list_story = []
#         self.name_book = name_book
#         print(f"Книга {name_book} создана")
#
#     def __del__(self):
#         print(f"Книга {self.name_book} удалена")
#
#     def add_story(self, name_story):
#         self.__list_story.append(name_story)
#
#     def count_story(self):
#         print(len(self.__list_story))
#
#     def book_info(self):
#         print(f"Книга: {self.name_book}")
#         print("Содержание:")
#         counter = 1
#         for i in self.__list_story:
#             print(f"\t{counter}) {i}")
#             counter += 1
#
# class Author:
#     def __init__(self, full_name, country):
#         self.full_name = full_name
#         self.country = country
#
#     def print_info(self):
#         print(f"ФИО: {self.full_name}, страна: {self.country}")
#
# class AuthorBook(Author, Book):
#     def __init__(self, full_name, country, title):
#         Author.__init__(self, full_name, country)
#         Book.__init__(self, title)
#
#     def print_full_name(self):
#         print(self.full_name)
#         print(self.name_book)
#         print("Содержание:")
#         for i, name_story in self.__list_story:
#             print(f"{i}) {name_story}")
#
# asd = AuthorBook("asd","asd", "asdad")
# asd.add_story("fasdfa")
# asd.add_story("fasdfa")
# asd.add_story("fasdfa")
# asd.print_full_name()