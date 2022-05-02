"""Instructions V2 Second version of instructions module
(Based on instructions v1)
I converted the instructions into a function and also
remove the input from the instructions to ovoid further
confusion as this was not a real question and just a training one"""


def instructions():
    print("How to play:")
    print("This is a quiz game about testing your Māori knowledge")
    print("This quiz is multiple choice\n")
    print("This is an example of the format the questions will be asked in\n")
    print('(A): Wrong answer\t(B) Right answer'
          '\n(C) Wrong answer\t(D) Wrong answer\nThe right answer'
          ' will not always be (B) this is just an example')
    print("You have finished the instructions good luck\n")


while True:
    played_before = input("Have you played before: ").title()
    if played_before == "No":
        instructions()
        break
    elif played_before == "Yes":
        print("No instructions shown")
        break
    else:
        print("Please enter 'yes' or 'no'")
