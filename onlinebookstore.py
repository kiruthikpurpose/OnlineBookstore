class Author:
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.bio}"


class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author.name}, Price: ${self.price}, Stock: {self.stock}"


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer: {self.name}, Email: {self.email}"


class Order:
    def __init__(self, customer, book, quantity):
        self.customer = customer
        self.book = book
        self.quantity = quantity
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def __str__(self):
        status = "Delivered" if self.delivered else "Pending"
        return f"Order for {self.quantity} copy/copies of '{self.book.title}' by {self.customer.name} - {status}"


class OnlineBookstore:
    def __init__(self):
        self.books = []
        self.orders = []

    def add_book(self, book):
        self.books.append(book)

    def browse_books(self):
        for book in self.books:
            print(book)

    def place_order(self, customer, book_title, quantity):
        for book in self.books:
            if book.title == book_title:
                if book.stock >= quantity:
                    book.stock -= quantity
                    order = Order(customer, book, quantity)
                    self.orders.append(order)
                    print("Order placed successfully!")
                    return
                else:
                    print("Not enough stock available.")
                    return
        print("Book not found.")

    def manage_deliveries(self):
        for order in self.orders:
            if not order.delivered:
                order.deliver()
                print(f"Delivered: {order}")

    def view_orders(self):
        for order in self.orders:
            print(order)


# Example usage
if __name__ == "__main__":
    bookstore = OnlineBookstore()

    author1 = Author("J.K. Rowling", "British author, best known for the Harry Potter series.")
    author2 = Author("George R.R. Martin", "American novelist and short story writer, best known for A Song of Ice and Fire.")

    book1 = Book("Harry Potter and the Philosopher's Stone", author1, 20.00, 50)
    book2 = Book("A Game of Thrones", author2, 25.00, 30)

    bookstore.add_book(book1)
    bookstore.add_book(book2)

    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")

    print("Browsing books:")
    bookstore.browse_books()
    print()

    print("Placing orders:")
    bookstore.place_order(customer1, "Harry Potter and the Philosopher's Stone", 2)
    bookstore.place_order(customer2, "A Game of Thrones", 1)
    print()

    print("Viewing orders:")
    bookstore.view_orders()
    print()

    print("Managing deliveries:")
    bookstore.manage_deliveries()
    print()

    print("Viewing orders after deliveries:")
    bookstore.view_orders()
