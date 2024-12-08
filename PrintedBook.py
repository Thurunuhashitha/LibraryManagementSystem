from Book import Book
class PrintedBook(Book):
    def __init__(self, book_id, title, isbn, author_name, genre, quantity, location, condition):
        super().__init__(book_id, title, isbn, author_name, genre)
        self.quantity = quantity
        self.location = location
        self.condition = condition

    def view_location(self):
        print(f"{self.title}'s location is {self.location}")

    def update_location(self, new_location):
        if(self.location != new_location):
            prev_location = self.location
            self.location  = new_location
            print(f"{self.title}'s prev location{prev_location} set to {self.location}")
            return
        print(f"{self.title}'s location can not set to {new_location}")        
        

    def check_quantity(self):
        print(f"{self.title}'s quantity is {self.quantity}")

    def update_quantity(self, new_quantity):
        if(self.quantity != new_quantity):
            prev_quantity = self.quantity
            self.quantity  = new_quantity
            print(f"{self.title}'s prev quantity{prev_quantity} set to {self.quantity}")
            return
        print(f"{self.title}'s entered quantity is same as previous")       

    def update_condition(self, new_condition):
        if(self.condition != new_condition):
            prev_condition = self.condition
            self.condition  = new_condition
            print(f"{self.title}'s prev condition{prev_condition} set to {self.condition}")
            return
        print(f"{self.title}'s entered condition is same as previous")
