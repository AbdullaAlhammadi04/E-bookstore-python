# 1. EBook Class
class EBook:
    #Represents an e-book in the catalog

    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    def get_price(self):
        #Returns the price of the e-books
        return self.__price

    def __str__(self):
        return f"{self.__title} by {self.__author} (Genre: {self.__genre}), Price: AED {self.__price:.2f}"


# 2. Catalog Class
class Catalog:
    #Manages the collection of e-books available in the store

    def __init__(self):
        self.__ebooks = []

    def add_ebook(self, ebook):
        #Adds an e-book to the catalog
        self.__ebooks.append(ebook)

    def remove_ebook(self, title):
        #Removes an e-book from the catalog by title
        self.__ebooks = [ebook for ebook in self.__ebooks if ebook.title != title]

    def list_ebooks(self):
        #Prints all e-books in the catalog
        for ebook in self.__ebooks:
            print(ebook)

    def __str__(self):
        return "\n".join(str(ebook) for ebook in self.__ebooks)


# 3. LoyaltyCard Class
class LoyaltyCard:
    #Represents a loyalty card with a special discount rate

    def __init__(self, card_id, loyalty_discount=0.1):
        self.__card_id = card_id
        self.__loyalty_discount = loyalty_discount

    def apply_loyalty_discount(self, total_price):
        #Applies loyalty discount to the total price
        return total_price * (1 - self.__loyalty_discount)


# 4. Customer Class
class Customer:
    #Represents a customer who can browse and purchase e-books

    def __init__(self, name, contact_info, loyalty_card=None):
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_card = loyalty_card

    def get_loyalty_discount(self):
        #Returns the loyalty discount if available
        if self.__loyalty_card:
            return self.__loyalty_card.apply_loyalty_discount
        return None

    def __str__(self):
        return f"Customer: {self.__name}, Contact: {self.__contact_info}, Loyalty Card: {self.__loyalty_card is not None}"


# 5. ShoppingCart Class
class ShoppingCart:
    #Manages items selected by the customer for purchase

    def __init__(self):
        self.__items = {}

    def add_item(self, ebook, quantity=1):
        #Adds an item to the shopping cart
        if ebook in self.__items:
            self.__items[ebook] += quantity
        else:
            self.__items[ebook] = quantity

    def remove_item(self, ebook):
        #Removes an item from the shopping cart
        if ebook in self.__items:
            del self.__items[ebook]

    def calculate_total(self):
        #Calculates the total price of items in the cart
        return sum(ebook.get_price() * qty for ebook, qty in self.__items.items())

    def __str__(self):
        return "\n".join(f"{ebook} - Qty: {qty}" for ebook, qty in self.__items.items())


# 6. Discount Class
class Discount:
    #Handles the calculation of discounts

    def apply_bulk_discount(total_price, quantity):
        #Applies a bulk discount for orders of 5 or more items
        if quantity >= 5:
            return total_price * 0.8
        return total_price


# 7. Order and Invoice Classes
class Order:
    #Represents an order made by the customer

    def __init__(self, customer, shopping_cart):
        self.__customer = customer
        self.__shopping_cart = shopping_cart
        self.__total = 0

    def calculate_total(self):
        #Calculates the total order amount after applying discounts
        quantity = sum(self.__shopping_cart._ShoppingCart__items.values())
        total_price = self.__shopping_cart.calculate_total()

        # Apply bulk discount if applicable
        total_price = Discount.apply_bulk_discount(total_price, quantity)

        # Apply loyalty discount if applicable
        if self.__customer.get_loyalty_discount():
            total_price = self.__customer.get_loyalty_discount()(total_price)

        self.__total = total_price
        return total_price

    def generate_invoice(self):
        #Generates an invoice for the order
        return Invoice(self.__total)


class Invoice:
    """Represents an invoice for an order."""

    def __init__(self, total_amount):
        self.__total_amount = total_amount

    def __str__(self):
        return f"Invoice Total (with discounts): AED {self.__total_amount:.2f}"


# 8. Payment Class
class Payment:
    #Processes the payment for an order

    def __init__(self, payment_type):
        self.__payment_type = payment_type

    def process_payment(self, amount):
        #Processes the payment and outputs confirmation
        print(f"Processing {self.__payment_type} payment for AED {amount:.2f}")


# 9. Test Cases of the main function
def test_ebookstore():
    # Create a catalog and add e-books
    catalog = Catalog()
    ebook1 = EBook("Harry potter", "Author A", "1990-01-01", "Adventure", 30.00)
    ebook2 = EBook("Harry Potter The sequel", "Author B", "1990-05-15", "Adventure", 20.00)
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)
    print("Catalog:")
    catalog.list_ebooks()

    # Create a customer with a loyalty card
    loyalty_card = LoyaltyCard("123")
    customer = Customer("Abdulla", "Abdulla@myspace.com", loyalty_card)

    # Create a shopping cart and add items
    cart = ShoppingCart()
    cart.add_item(ebook1, 3)
    cart.add_item(ebook2, 2)
    print("\nShopping Cart:")
    print(cart)

    # Create an order, apply discounts, and generate an invoice
    order = Order(customer, cart)
    total = order.calculate_total()
    invoice = order.generate_invoice()
    print("\nInvoice:")
    print(invoice)

    # Process payment
    payment = Payment("Credit Card")
    payment.process_payment(total)


# Run test
test_ebookstore()
