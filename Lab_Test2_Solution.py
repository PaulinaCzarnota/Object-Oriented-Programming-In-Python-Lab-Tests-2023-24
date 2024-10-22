class Publication(object):
    """Publication class that stores the title (string) and price (float) of publications.
    Contains a constructor and __str__ method."""

    def __init__(self, title="", price=0.0):
        """Creates an instance of Publication with user input if arguments are not passed or with arguments
        passed."""
        if title == "":  # Default value. Replace by user input
            self.title = input("Please enter a title: ")
        else:  # Use non default value.
            self.title = title

        if price == 0:  # Default value. Replace by user input
            while True:
                try:
                    self.price = float(input("Please enter a price: "))
                    break
                except ValueError:
                    print("Please enter a valid number")

        else:  # Use non default value.
            self.price = price

    def __str__(self):
        result = "Title: " + self.title + "\n"
        result += "Price: " + str(self.price) + "\n"
        return result


class Book(Publication):
    """Books class that inherits from Publication.
    It adds the page_count for each book and also overloads the + operator"""

    def __init__(self, title="", price=0, page_count=0):
        Publication.__init__(self, title, price)

        if page_count == 0:  # Default value. Replace by user input
            while True:
                try:
                    self.page_count = int(input("Please enter the page count: "))
                    break
                except ValueError:
                    print("Please enter a valid number")

        else:  # Use non default value.
            self.page_count = page_count

    def __str__(self):
        return Publication.__str__(self) + "Page count: " + str(self.page_count) + "\n"

    def __add__(self, other):
        """Adds two books. The new title is given by the user. Price and page_count are the sum of the two books being
        added."""

        # Introspection. Adds two books only
        if type(other) != Book:
            print("Only books accepted")
            return

        return Book(price=self.price + other.price, page_count=self.page_count + other.page_count)


# Main scope
book1 = Book()
print(book1)
print()

book2 = Book()
print(book2)
print()

# Test operator overloading
print(book1 + book2)
