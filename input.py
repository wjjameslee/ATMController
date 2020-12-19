class InputChecker:
    # Checks for invalid input
    def __init__(self, numeric):
        self.numeric = numeric

    def change(self, new):
        self.numeric = new

    def check(self, arg):
        if self.numeric:
            if arg.isalpha():
                raise Exception("Input received is an alphabetic string.")
            elif not arg.isdigit():
                raise Exception("Input received is not an integer.")


