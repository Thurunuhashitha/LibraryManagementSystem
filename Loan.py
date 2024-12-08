from datetime import datetime, timedelta

class Loan:
    fine_rate = 10  # Example fine rate (e.g., 10 Rupees per day)

    def __init__(self, loan_id, loan_date, due_date, return_date=None):
        self.loan_id = loan_id
        self.loan_date = loan_date
        self.due_date = due_date
        self.return_date = return_date

    def calc_fine(self):
        if not self.return_date:
            print("Cannot calculate fine due to book not returning.")
            return 0

        # Parse dates and calculate difference
        due_date = datetime.strptime(self.due_date, "%Y-%m-%d")
        return_date = datetime.strptime(self.return_date, "%Y-%m-%d")

        if return_date > due_date:
            overdue_days = (return_date - due_date).days
            fine = overdue_days * self.fine_rate
            print(f"Loan ID - {self.loan_id}, Overdue by {overdue_days} days. Fine: Rs. {fine}")
            return fine
        else:
            print(f"Loan ID - {self.loan_id}, No fine. Book was returned on time.")
            return 0

    def complete_return(self, return_date):
        self.return_date = return_date
        print(f"Loan ID - {self.loan_id}, Book returned on {self.return_date}")

    def check_due_date(self):
        today = datetime.now()
        due_date = datetime.strptime(self.due_date, "%Y-%m-%d")

        if today > due_date:
            overdue_days = (today - due_date).days
            print(f"Loan ID - {self.loan_id}, Book is overdue by {overdue_days} days!")
        else:
            days_remaining = (due_date - today).days
            print(f"Loan ID - {self.loan_id}, {days_remaining} days left until due date.")

    def extend_loan(self, days):
        due_date = datetime.strptime(self.due_date, "%Y-%m-%d")
        extended_due_date = due_date + timedelta(days=days)
        self.due_date = extended_due_date.strftime("%Y-%m-%d")
        print(f"Loan ID - {self.loan_id}, Due date extended to {self.due_date}")
