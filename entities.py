class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_loaned = False

    def change_status(self, loaned: bool): 
        # Updates the availability of the book
        self.is_loaned = loaned

    def get_info(self): 
        # Returns a string containing the book's data and its current status
        status = "Loaned" if self.is_loaned else "Available"
        return f"[{self.isbn}] {self.title} - {self.author} ({status})"

    def check_availability(self): 
        # Indicates if the book is available for loan
        return not self.is_loaned

    def matches_isbn(self, target_isbn): 
        # Validates if the ISBN matches for search queries
        return self.isbn == target_isbn


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.active_books = []

    def link_book(self, isbn): 
        # Adds an ISBN to the user's list when they borrow a book
        self.active_books.append(isbn)

    def unlink_book(self, isbn): 
        # Removes an ISBN from the user's list when they return it
        if isbn in self.active_books:
            self.active_books.remove(isbn)
            return True
        return False

    def has_books(self): 
        # Checks if the user has any books currently in use
        return len(self.active_books) > 0

    def user_summary(self): 
        # Returns a summary of the user's profile
        return f"ID: {self.user_id} | Name: {self.name} | Books: {len(self.active_books)}"