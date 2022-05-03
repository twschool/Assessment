"""[Generate random options v1] A script to generate a random order of options
and to generate a random order of questions"""
# Main routine
import random

options = ["A", "B", "C", "D"]
number_questions_stored = [["Tahi", 1], ["Rua", 2], ["Toru", 3], ["Whā", 4], ["Rima", 5],
                           ["Ono", 6], ["Whitu", 7], ["Waru", 8], ["Iwa", 9], ["Tekau", 10]]

question_picked = random.choice(number_questions_stored)
# Question picked number is taking the second thing in the list eg: if the list
# was ["Ono", 6] it would set itself to the number 6
correct_picked_answer = question_picked[1]
# Correct option is taking the first thing in the list eg: if the list
# was ["Ono", 6] it would set itself to "Ono" because out of the randomly generated
# options this is the right one
correct_option = question_picked[0]
number_questions_stored.remove(question_picked)
temporary_list_1 = number_questions_stored
temporary_list_2 = []
random_options = []
final_randomised_list = []
temporary_list_2.append(correct_option)
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
    print(temporary_list_2)

for count in range(0, 4):
    selected = random.choice(temporary_list_2)
    random_options.append(selected)
    temporary_list_2.remove(selected)

print(random_options)
print(f"What is {correct_picked_answer} in Māori")
print(f'(A) {random_options[0]}  \t(B) {random_options[1]}'
      f'\n(C) {random_options[2]}  \t(D) {random_options[3]}')

find_correct_answer = random_options.index(correct_option)
correct_answer = options[find_correct_answer]
print(f"{correct_answer} is the correct answer")
