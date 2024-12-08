from Member import Member
class Employee(Member):
    def __init__(self, member_id, member_name, contact_info, age, membership_type, membership_status, employee_id, position, salary):
        super().__init__(member_id, member_name, contact_info, age, membership_type, membership_status)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    def update_member_status(self, library, member_id, new_membership_status):
        for member in library.members:
            if member.member_id == member_id:
                member.membership_status = new_membership_status
                print(f"member with ID {member_id} membership status set to {new_membership_status}")
                return
            print(f"member with ID {member_id} is doesn't exist.")

    def manage_inventory(self,library, book, action):        
        if action == "add":
            library.add_book(book)
            print(f"Book '{book.title}' has been added to the inventory.")
        elif action == "remove":
            if library.remove_book(book.book_id):
                print(f"Book '{book.title}' has been removed from the inventory.")
            else:
                print(f"Book with ID {book.book_id} could not be found in the inventory.")
        else:
            print("Invalid action. Use 'add' or 'remove'.")

    def issue_fines(self, member, amount):
        if member.membership_status == "Active":
            member.fine_amount = amount
            print(f"Fine of Rs. {amount} issued to {member.member_name}. Total fine is now Rs.{member.fine_amount}.")
        else:
            print(f"Cannot issue a fine to {member.member_name}. Membership status is '{member.membership_status}'.")
