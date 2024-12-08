class Book:
    def __init__(self, book_id, title, isbn, author_name, genre, availability=True):
        self.book_id = book_id
        self.title = title
        self.isbn = isbn
        self.author_name = author_name
        self.genre = genre
        self.availability = availability

    def get_book_details(self):
        return (
            f"Book ID: {self.book_id}\n"
            f"Title: {self.title}\n"
            f"ISBN: {self.isbn}\n"
            f"Author Name: {self.author_name}\n"
            f"Genre: {self.genre}\n"
            f"Availability: {'Available' if self.availability else 'Unavailable'}"
        )

    def check_availability(self):
        print(f"{self.title} is {'Available' if self.availability else 'Unavailable'}")

    def update_availability(self, status):
        prev_availability_status = self.availability
        if prev_availability_status != status:
            self.availability = status
            print (
                f"{self.title}'s status updated from "
                f"{'Available' if prev_availability_status else 'Unavailable'} "
                f"to {'Available' if self.availability else 'Unavailable'} successfully."
            )
            return
        print(f"{self.title} is already {'Available' if self.availability else 'Unavailable'}.")
