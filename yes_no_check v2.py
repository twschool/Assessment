"""yes_no_check v2 based on ves_no_check_v1
this version is not a test version and works as intended"""


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
