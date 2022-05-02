"""A/B/C/D Options checker v1 checks the options submitted by the user
if the answer is 'A' or 'B' or 'C' or 'D' the program continues if it isn't
the program loops"""


def options_checker(options_input):
    if options_input == "A" or options_input == "B" or \
                options_input == "C" or options_input == "D":
        return True
    else:
        return False


# Main routine
while True:
    response = input("Test input for A\B\C\D options checker\nResponse: ").upper()
    if options_checker(response) == True:
        print("Program continues")
    else:
        print("" "Error please enter 'A' or 'B' or 'C' or 'D'" "")
