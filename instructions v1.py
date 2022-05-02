"""Instructions v1 First version of instructions module"""
played_before = input("Have you played before: ").lower()
if played_before == "Yes":
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
        elif instructions_input == "A" or instructions_input == "C" or instructions_input == "D":
            print("Incorrect but at least now you are familiar with the options system")
            break
        else:
            print('Please answer "A", "B", "C", or "D"')
    print("You have finished the instructions good luck\n")
else:
    print("No instructions shown")
