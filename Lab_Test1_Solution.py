def sum_of_squares(n):
    """Function that takes a number n and return
    the sum of the square of its digits"""

    # Convert number to string to iterate over its
    # digits
    n_str = str(n)
    sum = 0
    for digit in n_str:
        sum = sum + int(digit) ** 2
    return sum


def is_happy(n):
    """Function that takes a number n and returns True
    if n is happy of false otherwise"""

    # Keep getting the sum of squares while sum
    # is not 1 or 4 (assuming that the happy algorithm
    # ends)
    while True:
        n = sum_of_squares(n)
        if n == 1:
            return True
        elif n == 4:
            return False


def all_happy_numbers(upper_limit):
    """Print the numbers from 1 till upper_limit
    that are happy numbers"""

    for i in range(1, upper_limit + 1):
        if is_happy(i):
            print(i, end = " ")


# Main scope
upper_limit = int(input("Please enter a number: "))
while upper_limit < 0:
    upper_limit = int(input("Please enter a number: "))

print("All happy numbers up to", upper_limit, "are:")
all_happy_numbers(upper_limit)