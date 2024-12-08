class Member:
    def __init__(self, member_id, member_name, contact_info, age, membership_type, membership_status):
        self.member_id = member_id
        self.member_name = member_name
        self.contact_info = contact_info
        self.age = age
        self.membership_type = membership_type
        self.membership_status = membership_status
        self.borrowed_books = []
        self.fine_amount = 0

    def update_contact_info(self, new_contact_info):
        if self.contact_info != new_contact_info:
            prev_contact_info = self.contact_info
            self.contact_info = new_contact_info
            print(f"{self.member_name}'s previous contact info: {prev_contact_info} updated to {self.contact_info}")
        else:
            print(f"{self.member_name}'s contact info is the same as the new one, no update needed.")   

    def borrow_book(self, book):
        if self.membership_status == "Active":
            self.borrowed_books.append(book)
            print(f"{self.member_name} borrowed the book: {book.title}")
        else:
            print(f"{self.member_name}'s membership is not active, cannot borrow books.")
        
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.member_name} returned the book: {book.title}")
        else:
            print(f"{self.member_name} has not borrowed the book: {book.title}.")
            
    def pay_fines(self, amount):
        if self.fine_amount > 0:
            self.fine_amount -= amount
            print(f"{self.member_name} paid Rs. {amount} as fine. Remaining fine is Rs. {self.fine_amount}")
        else:
            print("Fine amount must be greater than 0.")
    
    def make_loan(self, loan):
        print(f"{self.member_name} created a loan with ID: {loan.loan_id}.")
        
    def upgrade_membership(self):
        if self.membership_type == "Standard":
            self.membership_type = "Premium"
            print(f"{self.member_name}'s membership upgraded to Premium.")
        else:
            print(f"{self.member_name}'s membership is already Premium.")
    
    def downgrade_membership(self):
        if self.membership_type == "Premium":
            self.membership_type = "Standard"
            print(f"{self.member_name}'s membership downgraded to Standard.")
        else:
            print(f"{self.member_name}'s membership is already Standard.")