class Library:
    def __init__(self, library_id, library_name, address):
        self.library_id = library_id
        self.library_name = library_name
        self.address = address
        self.books = []
        self.members = []

    def register_member(self, member):
        # Check for existing members
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                print(f"Member with ID {member.member_id} already exists")
                return

        # Add the member
        self.members.append(member)

    def add_book(self, book):
        # Check for duplicate book
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print(f"Book with ID {book.book_id} already exists")
                return

        # Add the book
        self.books.append(book)
        print(f"Book '{book.title}' (ID: {book.book_id}) has been successfully")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book with ID {book_id} has been removed")
                return
        print(f"Book with ID {book_id} not found in the library.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print(f"Found Book:\n{book.get_book_details()}")
                return book
        print(f"Book with ID {book_id} not found in the library.")
        return None
