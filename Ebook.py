from Book import Book
class Ebook(Book):
    def __init__(self, book_id, title, isbn, author_name, genre, link, file_size):
        super().__init__(book_id, title, isbn, author_name, genre)
        self.link = link
        self.file_size = file_size

    def download(self):
        print(f"Ebook {self.title} downloadable link is {self.link}")

    def get_file_size(self):
        print(f"Ebook {self.title} file size is {self.file_size}")
