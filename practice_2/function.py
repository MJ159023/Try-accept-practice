
def ask_user_for_number():
    """
    Asks User for number and then checks to make sure it's number before returning.
    Gives error message if User inputs anything but a number
    """

    while True:
        try:
            print("Hello please input a number.")
            user_choice = int(input())
            print("")
            return user_choice
        except ValueError:
            print("Please input only numbaers. Try again")
            print("")

