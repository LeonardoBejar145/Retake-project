import csv
from entities import Book, User

class LoanRecord:
    def __init__(self, user_id, isbn, date):
        self.user_id = user_id
        self.isbn = isbn
        self.date = date
        self.is_active = True

    def finish_record(self): 
        # Mark the loan as returned
        self.is_active = False

    def belongs_to_user(self, user_id): 
        # Check if the record belongs to a specific user
        return self.user_id == user_id

    def get_details(self): 
        # Format the record for printing
        status = "ACTIVE" if self.is_active else "RETURNED"
        return f"User: {self.user_id} | Book: {self.isbn} | Date: {self.date} | [{status}]"

    def serialize(self): 
        # Convert the object into a list for the CSV
        return [self.user_id, self.isbn, self.date, self.is_active]


class LibrarySystem:
    def __init__(self, data_file):
        self.data_file = data_file
        self.books = []
        self.records = []

    def register_book(self, book_obj): 
        # Add a book to the system
        self.books.append(book_obj)

    def find_book(self, isbn): 
        # Search for a book by ISBN
        for b in self.books:
            if b.matches_isbn(isbn):
                return b
        return None

    def process_loan(self, user, isbn, date): 
        # Process for creating a loan/borrow and saving it in the history of the user 
        book = self.find_book(isbn)
        if book and book.check_availability():
            book.change_status(True)
            user.link_book(isbn)
            new_record = LoanRecord(user.user_id, isbn, date)
            self.records.append(new_record)
            return True
        return False