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
    response = input("(A) (B) (C) (D) Response: ").upper()
    if options_checker(response) is True:
        print("Program continues")
    else:
        print("" "Error please enter 'A' or 'B' or 'C' or 'D'" "")
