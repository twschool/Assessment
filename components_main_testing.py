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


def instructions():
    print("How to play:")
    print("This is a quiz game about testing your Māori knowledge")
    print("This quiz is multiple choice\n")
    print("This is an example of the format the questions will be asked in\n")
    while True:
        instructions_input = input('(A): Wrong answer\t(B) Right answer'
                                   '\n(C) Wrong answer\t(D) Wrong answer'
                                   '\nResponse: ').upper()
        if instructions_input == "B":
            print("Correct\n")
            break
        if instructions_input == "A" or instructions_input == "B" or \
                instructions_input == "C" or instructions_input == "D":
            print("Incorrect but at least now you are familiar with the options system")
            break
        else:
            print('Please answer "A", "B", "C", or "D"')
    print("You have finished the instructions good luck\n")


# Main routine
name = input("What is your name: ").title()
print(f"Hello {name} and welcome to the Māori language quiz")
played_before = yes_no_checker("Have you played before: ")
print()
if played_before is False:
    instructions()
else:
    print("Continuing")
