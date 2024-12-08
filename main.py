from Library import Library
from Member import Member
from Patron import Patron
from Employee import Employee
from Loan import Loan
from Book import Book
from Ebook import Ebook
from PrintedBook import PrintedBook

# Example test case
if __name__ == "__main__":
    # Create a library
    library = Library("1", "City Library", "123 Main St")
    
    # Create a book and add to library
    book = Book("101", "Python Programming", "123456789", "John Doe", "Programming")
    book_2 = Book("102", "Data Science Essentials", "987654321", "Jane Smith", "Data Science")
    print("\n=== Book Operations ===")
    # Printing book details
    print(book.get_book_details())
    # Checking availabilty
    book.check_availability()
    # Update availabilty
    book.update_availability(False)
    print("\n=== Library Operations ===")
    # Adding book to the libarary
    library.add_book(book)
    library.add_book(book_2)
     # Find book by the book ID
    library.find_book("101")
    # Remove book by the book ID
    library.remove_book("102")
    
    # Create a member
    member = Member("201", "Alice", "alice@example.com", 25, "Standard", "Active")
    library.register_member(member)
    
    # Create a Loan instance
    loan = Loan("L001", "2024-12-01", "2024-12-07")
    # Example usage of loan methods
    print("\n=== Loan Operations ===")
    # Check if the book is overdue
    loan.check_due_date()        
    # Mark the book as returned
    loan.complete_return("2024-12-10")
    # Calculate fine
    loan.calc_fine()           
    # Extend Loan by days
    loan.extend_loan(5)

    # Create a PrintedBook
    book_3 = PrintedBook("102", "Data Science Essentials", "987654321", "Jane Smith", "Data Science", 10, "Aisle 3, Shelf B", "Good")
    # Example usage of PrintedBook methods
    print("\n=== Printed Book Operations ===")
    # View location of the book
    book_3.view_location()
    # Update the location of the book
    book_3.update_location("Aisle 5, Shelf D")
    # Check the quantity of the book
    book_3.check_quantity()
    # Update the quantity of the book
    book_3.update_quantity(8)
    # Update the condition of the book
    book_3.update_condition("Excellent")

    # Create an Ebook
    ebook = Ebook("201", "Machine Learning Basics", "456123789", "Alice Johnson", "Technology", "https://example.com/ml_basics", "5MB")
    # Example usage of Ebook methods
    print("\n=== Ebook Operations ===")
    # Get the downloadable link of the ebook
    ebook.download()
    # Get the file size of the ebook
    ebook.get_file_size()

    # Create an Patron
    patron = Patron("201", "Alice", "alice@example.com", 25, "Standard", "Active", 3, 500)
    print("\n=== patron Operations ===")
    # Patron reserves a book
    patron.reserve_book(library, "102")

    # Create an Employee
    employee = Employee("E001", "John", "john@example.com", 35, "Staff", "Active", "EMP001", "Librarian", 50000)
    # Example usage of Employee methods
    print("\n=== Employee Operations ===")
    # Update a member's status
    employee.update_member_status(library, "M001", "Suspended")
    # Add a book to the library inventory
    # Create Book 3 instance
    book_3 = Book("103", "Machine Learning Basics", "192837465", "Mark Johnson", "Machine Learning")
    employee.manage_inventory(library, book_3, "add")
    # Issue a fine to a member
    employee.issue_fines(member, 10)
    # Remove a book from the library inventory
    employee.manage_inventory(library, book_3, "remove")

    # Example usage of Member methods
    print("\n=== Member Operations ===")
    # Update contact info
    member.update_contact_info("alice_new@example.com")
    # Borrow a book
    book_4 = Book("101", "Python Programming", "123456789", "John Doe", "Programming")
    member.borrow_book(book_4)
    # Return a book
    member.return_book(book_4)
    # Pay fines
    member.pay_fines(5)