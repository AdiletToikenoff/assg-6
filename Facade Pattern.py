## Facade Pattern

# Define interface for the facade
class LibraryFacade:
    def __init__(self):
        self.book_inventory = BookInventory()
        self.user_management = UserManagement()

    def borrow_book(self, book_title, user_id):
        return self.book_inventory.borrow_book(book_title, user_id)

    def return_book(self, book_title, user_id):
        return self.book_inventory.return_book(book_title, user_id)

    def search_books(self, search_query):
        return self.book_inventory.search_books(search_query)

    def check_availability(self, book_title):
        return self.book_inventory.check_availability(book_title)


# Subsystem for book inventory
class BookInventory:
    def __init__(self):
        self.books = {}

    def add_book(self, book_title, quantity):
        self.books[book_title] = quantity

    def borrow_book(self, book_title, user_id):
        if book_title in self.books and self.books[book_title] > 0:
            self.books[book_title] -= 1
            return f"Book '{book_title}' borrowed by user {user_id}."
        else:
            return f"Book '{book_title}' is not available."

    def return_book(self, book_title, user_id):
        if book_title in self.books:
            self.books[book_title] += 1
            return f"Book '{book_title}' returned by user {user_id}."
        else:
            return f"Book '{book_title}' is not in inventory."

    def search_books(self, search_query):
        # Search logic here
        pass

    def check_availability(self, book_title):
        if book_title in self.books and self.books[book_title] > 0:
            return f"Book '{book_title}' is available."
        else:
            return f"Book '{book_title}' is not available."


# Subsystem for user management
class UserManagement:
    def __init__(self):
        self.users = {}

    # User management methods go here


# Test cases
def test_library_facade():
    facade = LibraryFacade()
    facade.book_inventory.add_book("Book1", 1)  # Adding Book1 with 1 quantity
    assert facade.borrow_book("Book1", "User1") == "Book 'Book1' borrowed by user User1."
    assert facade.return_book("Book1", "User1") == "Book 'Book1' returned by user User1."
    assert facade.check_availability("Book1") == "Book 'Book1' is available."


## Decorator Pattern

# Base Pizza class
class Pizza:
    def __init__(self):
        self.price = 10

    def get_price(self):
        return self.price


# Decorator class
class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_price(self):
        return self.pizza.get_price()


# Concrete decorator classes
class PepperoniTopping(PizzaDecorator):
    def get_price(self):
        return self.pizza.get_price() + 2


class MushroomTopping(PizzaDecorator):
    def get_price(self):
        return self.pizza.get_price() + 1


# Test program
def test_pizza_decorator():
    pizza = Pizza()
    pizza_with_toppings = MushroomTopping(PepperoniTopping(pizza))
    assert pizza_with_toppings.get_price() == 13


# Run test cases
test_library_facade()
test_pizza_decorator()
