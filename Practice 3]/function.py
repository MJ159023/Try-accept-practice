
def get_two_numbers():
    """
    No arguments
    Asks User for two numbers
    Checks for wrong input
    Returns Numbers
    """

    while True:
        try:
            print("Input two numbers")
            print("")

            number_1 = int(input("Input the first number "))
            print("")

            number_2 = int(input("Input the second number "))
            print("")

            return [number_1, number_2]
        except TypeError:
            print("Input only numbers. Try again")

get_two_numbers()