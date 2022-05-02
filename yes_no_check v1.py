"""yes_no_check v1 this function checks the user input and
checks if the user answered 'yes' or 'no' if they have
the program continues but if they put an invalid answer
the yes/no checker loops this version is used for a test version
so it always loops"""


def yes_no_checker(question):
    while True:
        yes_no_input = input(f"{question}").lower()

        if yes_no_input == "yes" or yes_no_input == "y":
            yes_no = True
            break

        elif yes_no_input == "n" or yes_no_input == "no":
            yes_no = False
            break

        else:
            print('Please enter "yes" or "no"')
    return yes_no


# Temp main routine
while True:
    check = yes_no_checker("Yes or no test: ")
    if check is False:
        print("You answered no")
    else:
        print("You answered yes")
    print("Program continues")
