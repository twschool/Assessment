import random
import time

game_start = time.time()
"""[Finished_program_v1] (All components combined to create the final program)"""


def instructions():
    print("How to play:")
    print("This is a quiz game about testing your Māori knowledge")
    print("This quiz is multiple choice\n")
    print("This is an example of the format the questions will be asked in\n")
    print('(A): Wrong answer\t(B) Right answer'
          '\n(C) Wrong answer\t(D) Wrong answer\nThe right answer'
          ' will not always be (B) this is just an example')
    print("You have finished the instructions good luck\n")


def yes_no_checker(_question):
    while True:
        yes_no_input = input(f"{_question}").lower()
        print()

        if yes_no_input == "yes" or yes_no_input == "y":
            yes_no = False
            break

        elif yes_no_input == "n" or yes_no_input == "no":
            yes_no = True
            break

        else:
            print('Please enter "yes" or "no"')
    return yes_no


def options_checker(options_input):
    if options_input == "A" or options_input == "B" or \
                options_input == "C" or options_input == "D":
        return True
    else:
        return False


def generate_options(number_question_data, full_list_constant):
    options = ["A", "B", "C", "D"]

    question_picked = random.choice(number_question_data)
    number_questions_stored = number_question_data[:]
    # Question picked number is taking the second thing in the list eg: if the list
    # was ["Ono", 6] it would set itself to the number 6
    correct_picked_answer = question_picked[1]
    # Correct option is taking the first thing in the list eg: if the list
    # was ["Ono", 6] it would set itself to "Ono" because out of the randomly generated
    # options this is the right one
    correct_option = question_picked[0]
    number_questions_stored.remove(question_picked)
    temporary_list_1 = full_list_constant[:]
    temporary_list_2 = []
    random_options = []
    temporary_list_2.append(correct_option)
    temporary_list_1.remove(question_picked)
    # This means that the option picker will repeat 3 times (only 3 times because the correct
    # option has already been added
    for count in range(0, 3):
        # Chooses a random option from the temporary list 1 which is the same as number_questions_stored
        # except the correct answer is removed and the options that are picked are removed from the list
        # to avoid duplicate answers
        option_picked = random.choice(temporary_list_1)
        temporary_list_1.remove(option_picked)
        # Temporary_list_2 is used to store all the 3 random options as well as the 1 correct answer
        # It picks the first thing in the list as it needs the name and not the correct number
        temporary_list_2.append(option_picked[0])
    for count in range(0, 4):
        # All the random answers are in a list in temporary_options_2 like this
        # ["Actual answer", "Random", "Random", "Random"] since the correct answer is first
        # in the list I created another list called random_options to resort everything into random
        # order, so it would be easier to put them into options
        selected = random.choice(temporary_list_2)
        random_options.append(selected)
        temporary_list_2.remove(selected)
        # Random_options is a list of random options and the correct answer in a random order
        # This makes it easy to print it out randomly
    while True:
        print(f"What is {correct_picked_answer} in Māori? ")
        print(f'(A) {random_options[0]} \t (B) {random_options[1]} \n'
              f'(C) {random_options[2]} \t (D) {random_options[3]} ')
        user_input = input(f"Response:  ").upper()
        print()
        output_answer = options_checker(user_input)
        if output_answer is True:
            break
        elif output_answer is not True:
            print('''Please type a valid options ("A", "B", "C", or "D")''')
    find_correct_answer = random_options.index(correct_option)
    correct_answer = options[find_correct_answer]
    if correct_answer == user_input:
        return [True, question_picked]
    else:
        return [False, question_picked]


# Main routine
number_questions_stored_main = [["Tahi", 1], ["Rua", 2], ["Toru", 3], ["Whā", 4], ["Rima", 5],
                                ["Ono", 6], ["Whitu", 7], ["Waru", 8], ["Iwa", 9], ["Tekau", 10]]

days_of_the_week_stored_main = [["Rāhina", "Monday"], ["Rātū", "Tuesday"], ["Rāapa", "Wednesday"],
                                ["Rāpare", "Thursday"], ["Rāmere", "Friday"],
                                ["Rāhoroi", "Saturday"], ["Rātapu", "Sunday"]]

number_questions_constant = [["Tahi", 1], ["Rua", 2], ["Toru", 3], ["Whā", 4], ["Rima", 5],
                             ["Ono", 6], ["Whitu", 7], ["Waru", 8], ["Iwa", 9], ["Tekau", 10]]

days_of_the_week_constant = [["Rāhina", "Monday"], ["Rātū", "Tuesday"], ["Rāapa", "Wednesday"],
                             ["Rāpare", "Thursday"], ["Rāmere", "Friday"],
                             ["Rāhoroi", "Saturday"], ["Rātapu", "Sunday"]]

round_number = 1

wrong_questions = []
right_questions = []

print("Welcome to the Māori knowledge quiz")
do_show_instructions = yes_no_checker("Do you want to skip instructions: ")
if do_show_instructions is True:
    instructions()

while True:
    which_quiz = str(input("Do you want to be tested on:\n"
                           "(1): Numbers\n"
                           "(2): Days of the week\n"
                           "Response: "))
    print()
    if which_quiz == "1":
        main_questions_stored = number_questions_stored_main
        main_questions_constant = number_questions_constant
        repeat = 10
        break
    elif which_quiz == "2":
        main_questions_stored = days_of_the_week_stored_main
        main_questions_constant = days_of_the_week_constant
        repeat = 7
        break
    else:
        print('''Please answer either "1" or "2"''')

# if correct_answer == user_input:
#         return [True, "Nothing here", question_picked]
#     else:
#         return [False, question_picked, question_picked]
for item in range(0, repeat):
    print("Round {} out of {}".format(round_number, repeat))
    round_number += 1
    # print(f"{main_questions_stored}")
    options_output = generate_options(main_questions_stored, main_questions_constant)
    # print(f"{options_output} options output")
    question = options_output[1]
    main_questions_stored.remove(question)
    if options_output[0] is False:
        wrong_questions.append(question)
    else:
        right_questions.append(question)
print("Wrong answers: \n")
# print(wrong_questions)
length = len(wrong_questions)
# print(f"This is the length {length}")
for wrong_list_number in range(0, length):
    try:
        wrong_answer = wrong_questions[0]
        print(f"{wrong_answer[1]} in Māori is {wrong_answer[0]}")
        wrong_questions.remove(wrong_answer)
    except IndexError:
        print("This shouldn't be a problem contact Thomas for bug fixing")
        break
print()
print(f"You got {round_number - length -1} out of {repeat}")
print()
print(f"You played for {(time.time() - game_start):.0f} seconds")
print("Thanks for playing")
print("Goodbye")
