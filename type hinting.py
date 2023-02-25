from typing import List


# type hinting in python:
# hint of variable type in fuction and hint of return type
# the following way is not a common practice
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


# list_avg(123)

# type hinting in classes
class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."