from collections import deque
from bst import BookBST

class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.waitlist = deque()

    def __str__(self):
        return f"{self.title} by {self.author} (Available: {self.available_copies})"

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"User: {self.name} | ID: {self.user_id} | Borrowed: {self.borrowed_books}"

class Library:
    

    def __init__(self):
        self.books = {}  # book_id -> Book
        self.users = {}  # user_id -> User
        self.book_bst = BookBST()  # for title-based BST

    def add_book(self, book):
        self.books[book.book_id] = book
        self.book_bst.insert(book)  # insert into BST

    def register_user(self, user):
        self.users[user.user_id] = user

    def search_book_by_title(self, keyword):
        results = [book for book in self.books.values() if keyword.lower() in book.title.lower()]
        return results

    def issue_book(self, user_id, book_id):
        if user_id not in self.users or book_id not in self.books:
            print("Invalid user or book ID.")
            return

        user = self.users[user_id]
        book = self.books[book_id]

        if book.available_copies > 0:
            book.available_copies -= 1
            user.borrowed_books.append(book_id)
            print(f"Book '{book.title}' issued to {user.name}.")
        else:
            book.waitlist.append(user_id)
            print(f"No copies available. {user.name} added to waitlist.")

    def return_book(self, user_id, book_id):
        if user_id not in self.users or book_id not in self.books:
            print("Invalid user or book ID.")
            return

        user = self.users[user_id]
        book = self.books[book_id]

        if book_id in user.borrowed_books:
            user.borrowed_books.remove(book_id)
            book.available_copies += 1
            print(f"{user.name} returned '{book.title}'.")

            if book.waitlist:
                next_user_id = book.waitlist.popleft()
                self.issue_book(next_user_id, book_id)
        else:
            print(f"{user.name} has not borrowed this book.")
    
    def list_books_sorted_by_title(self):
        sorted_books = self.book_bst.inorder()
        for book in sorted_books:
            print(book)


# -------------------------------
# Example Usage
if __name__ == "__main__":
    lib = Library()

    # Add books
    lib.add_book(Book("B001", "Python Programming", "Guido van Rossum", 3))
    lib.add_book(Book("B002", "Data Structures", "Robert Lafore", 2))

    # Register users
    lib.register_user(User("U001", "Alice"))
    lib.register_user(User("U002", "Bob"))

    lib.list_books_sorted_by_title()


    results = lib.search_book_by_title("Python")
    for book in results:
        print("Found:", book)

    # Issue & Return
    lib.issue_book("U001", "B001")
    lib.issue_book("U002", "B001")
    lib.issue_book("U001", "B001")  # All copies issued
    lib.issue_book("U002", "B001")
    lib.return_book("U002", "B001")

    # Search books
