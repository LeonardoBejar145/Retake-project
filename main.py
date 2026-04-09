from entities import Book, User
from manager import LibrarySystem

def start(): 
    # System's activation 
    system = LibrarySystem("loan_history.csv")

    # Creation of books (ISBN, Title, Author) and Users (ID, Name)
    book1 = Book("123-1", "One Hundred Years of Solitude", "G. Garcia Marquez")
    book2 = Book("124-2", "Don Quixote", "Miguel de Cervantes")
    user1 = User("Client Number 1", "Carlos Perez")

    system.register_book(book1)
    system.register_book(book2)

    # Book's borrowing process 
    print("--- Loan Management ---")
    if system.process_loan(user1, "123-1", "09/04/2026"):
        print(f"Successful loan for: {user1.name}")
    else:
        print("The book is not available.")

    # Shows book status and availability 
    print("\nBook Status:")
    for b in system.books:
        print(b.get_info())

    print("\nUser Summary:")
    print(user1.user_summary())


if __name__ == "__main__":
    start()