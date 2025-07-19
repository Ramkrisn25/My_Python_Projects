# task3_library_management.py

class Book:
    """
    Represents a single book in the library.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        status (str): The current status of the book ('available' or 'issued').
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = 'available' # Default status when a book is added

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        """
        return f"'{self.title}' by {self.author} [{self.status.capitalize()}]"

class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        self.books = [] # A list to store Book objects

    def add_book(self, title, author):
        """
        Adds a new book to the library.
        """
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")

    def issue_book(self, title):
        """
        Issues a book to a borrower if it is available.
        """
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                found = True
                if book.status == 'available':
                    book.status = 'issued'
                    print(f"Book '{book.title}' has been issued.")
                else:
                    print(f"Book '{book.title}' is currently {book.status}.")
                return
        if not found:
            print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """
        Returns an issued book back to the library.
        """
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                found = True
                if book.status == 'issued':
                    book.status = 'available'
                    print(f"Book '{book.title}' has been returned.")
                else:
                    print(f"Book '{book.title}' is already {book.status}.")
                return
        if not found:
            print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """
        Lists all books currently marked as 'available'.
        """
        available_books = [book for book in self.books if book.status == 'available']
        if available_books:
            print("\n--- Available Books ---")
            for book in available_books:
                print(book)
            print("-----------------------")
        else:
            print("\nNo books currently available in the library.")

def main_menu():
    """
    Displays the main menu for the Library Management System.
    """
    library = Library()

    # Add some initial books for demonstration
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("Brave New World", "Aldous Huxley")
    print("\n--- Welcome to the Library Management System ---")

    while True:
        print("\n1. Add a new book")
        print("2. Issue a book")
        print("3. Return a book")
        print("4. List available books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("Enter the title of the book to issue: ")
            library.issue_book(title)
        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        elif choice == '4':
            library.list_available_books()
        elif choice == '5':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()