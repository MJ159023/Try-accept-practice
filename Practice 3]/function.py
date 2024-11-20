
def get_two_numbers():
    """
    Asks User for two numbers than returns them.
    If User fails to input numbers prints error message.
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