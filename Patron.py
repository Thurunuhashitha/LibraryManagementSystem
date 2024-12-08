from Member import Member

class Patron(Member):
    def __init__(self, member_id, member_name, contact_info, age, membership_type, membership_status, borrow_limit, membership_fee):
        super().__init__(member_id, member_name, contact_info, age, membership_type, membership_status)
        self.borrow_limit = borrow_limit
        self.membership_fee = membership_fee

    def reserve_book(self,library, book_id):
        for book in library.books:
            if book.book_id == book_id:
                if book.availability:
                    book.availability = False  # Mark the book as reserved
                    print(f"Book with ID {book_id} has been reserved.")
                    return
                else:
                    print(f"Book with ID {book_id} is already reserved.")
                    return
        print(f"Book with ID {book_id} is not found in the library.")
