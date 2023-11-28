# import traceback  # only for debug purpose
# I try not to use any more module or u will get mad
# I am sure if I use another module, the code will get shorter
# However, It doesn't matter now

import random


def difficulty_filter(difficulty_number):  # To filter difficulty
    # make sure these variable not assigned before statement
    second = None
    x = None
    # if difficulty number less than or equal 4
    # to use this function : operators[operator](first number, second number)
    operators_book = {'+': lambda a, b: a + b,
                      '-': lambda a, b: a - b,
                      '*': lambda a, b: a * b,
                      '/': lambda a, b: a / b}  # random operator function

    # Difficulty 1 - 4: plus and minus: 2 - 5 digits
    if int(difficulty_number) <= 4:
        operators_book_unique = {'+': lambda a, b: a + b,
                                 '-': lambda a, b: a - b}
        maximum_digit = "10"
        minimum_digit = "1"
        is_negative = False
        for x in range(1, int(difficulty_number)):
            maximum_digit += "0"
            minimum_digit += "0"
        first = random.randint(int(minimum_digit), int(maximum_digit))  # random the first number
        second = random.randint(int(minimum_digit), int(maximum_digit))  # random the second number
        if second > first:  # check if answer is a negative or not.
            is_negative = True
        while is_negative:
            second = random.randint(int(minimum_digit), int(maximum_digit))
            if second <= first:
                is_negative = False
        operators = ["+", "-"]
        operators = random.choice(operators)  # random operator
        answer = operators_book_unique[operators](first, second)
        return first, second, answer, operators

    # Difficulty 5 - 7: times: 3 - 5 digits
    # if difficulty number between 5 and 7
    elif 5 <= int(difficulty_number) <= 7:
        maximum_digit = "10"
        minimum_digit = "1"
        for x in range(1, int(difficulty_number) - 2):
            maximum_digit += "0"
            minimum_digit += "0"
        first = random.randint(int(minimum_digit), int(maximum_digit))  # random the first number
        # x will always be difficulty_number - 2
        second = random.randint(int(minimum_digit[:-x]),
                                int(maximum_digit[:-x]))  # second number, this will be always 1 - 10
        answer = first * second
        operators = "*"
        return first, second, answer, operators

    # Difficulty 7 - 9: divine: 3 - 4 digits
    # if difficulty number between 8 and 9
    elif 8 <= int(difficulty_number) <= 9:
        operators = "/"
        divisible = False
        while not divisible:
            maximum_digit = "10"
            minimum_digit = "1"
            for x in range(1, int(difficulty_number) - 2):
                maximum_digit += "0"
                minimum_digit += "0"
            first = random.randint(int(minimum_digit), int(maximum_digit))
            # x will always be difficulty_number - 2
            second = random.randint(int(minimum_digit[:-x]), int(maximum_digit[:-x]))  # this will be always 1 - 10
            if first % second != 0:  # makesure it is divisible
                divisible = False
            elif first % second == 0:
                answer = first / second
                return first, second, answer, operators

    # Difficulty 10: mixed: 5 digits
    elif int(difficulty_number) == 10:  # I am so happy, this one don't have for loop!
        maximum_digit_first = "100000"
        minimum_digit_first = "9999"

        operators = ['+', '-', '*', '/']
        operators = random.choice(operators)
        first = random.randint(int(minimum_digit_first), int(maximum_digit_first))
        if operators == '+' or operators == '-':  # filter number. Make sure it not too hard
            second = random.randint(9999, 100000)
        elif operators == '*':
            second = random.randint(2, 99)
        elif operators == '/':
            divisible = False
            while not divisible:
                second = random.randint(2, 30)
                if first % second != 0:  # makesure it is divisible
                    divisible = True
        else:
            second = None
            print("How did get this!!!!")
            print("End process with error please contact the author")

        answer = operators_book[operators](first, second)
        return first, second, answer, operators


# Ask a question which return str(1) and str(2) or str(3) (if existed)
def ask_me_a_question(a_question, first_option, second_option, third_option_optional=None):
    print(a_question + "\n1." + first_option + "\n2." + second_option)
    optional_open = False
    if third_option_optional is not None:
        optional_open = True
        print("3." + third_option_optional)
    the_user_input = str(input(":")).lower()
    if the_user_input == "1" or the_user_input == str(first_option).lower():
        return str("1")
    elif the_user_input == "2" or the_user_input == str(second_option).lower():
        return str("2")
    elif optional_open:
        if the_user_input == "3" or the_user_input == str(third_option_optional).lower():
            return str("3")
    else:
        print("\n\n_____________________________\nPlease only type a number provided in a question!\n "
              "Example: Are you sure? 1.Yes 2.No\n You type: 1\n\n\n______________________________\n\n")
        return ask_me_a_question(a_question, first_option, second_option)


# __________________________________________________________________________________________________________________ #
user_name = str(input("Hello user, What is your name?\n:"))
if not user_name.isalpha() and ' ' not in user_name:  # check if name contain weird letter or not
    print("well, your name is kinda weird. Anyway,")

asking = ask_me_a_question("Welcome " + user_name + "\nAre you ready for the test?", "yes", "No")
if asking == "1":

    # list of process for use in try except
    looping_before = True
    before_the_question = False
    in_the_question = False
    after_the_question = False

    # where the fun began
    while looping_before:
        before_the_question = True
        try:
            difficulty = int(input("How hard you want the test going to be 1 to 10\n "
                                   "1 is very easy.\n 10 is very hard\n:"))
            if difficulty > 10 or difficulty < 1:
                print("Please only type a number between 1 to 10")
            elif 1 <= difficulty <= 10:

                question_amount = int(input("How many question you want? (at lease 5)\n:"))
                if question_amount < 5:
                    print("make sure you choose more than  questions")
                if question_amount > 30:
                    asking = ask_me_a_question("That's alot of question, are you sure about that?",
                                               "Yes I want a lot of questions", "No I change my mind")
                    if asking == "2":
                        print("\n\n\n")
                if 5 <= question_amount <= 30:
                    asking = ask_me_a_question("So you want difficulty level: " + str(difficulty) +
                                               "\nand " + str(question_amount) + " questions?", "Yes",
                                               "No, I want to change")
                    if asking == '1':  # finally we can start the question!
                        i = 0  # to count how many question
                        mark = 0
                        while i != question_amount:
                            before_the_question = False
                            in_the_question = True

                            question = difficulty_filter(difficulty) 
                            # this will return as a list [first, second, answer, operators]
                            # and the variable type will be: [int(first), int(second), int(answer), str(operators)]
                            print(str(i + 1) + ')', " What is", question[0], question[3], question[1])
                            user_input = str(input(":"))
                            if user_input != str(question[2]):
                                print("Oops! that was wrong", question[0], question[3], question[1], "is", question[2])
                                print("________________________________________________________________")
                                i += 1
                            elif user_input == str(question[2]):
                                print("Yah! that's correct!", question[0], question[3], question[1], "is", question[2])
                                print("_________________________________________________________________")
                                mark += 1
                                i += 1

                        # calculate score and store them!
                        after_the_question = True
                        in_the_question = False
                        input("\n\npress enter to finish the question\n\n")
                        print("You answered", mark, "question(s) correct, "
                                                    "and", question_amount - mark, "question(s) wrong")
                        score_percentage = int((float(int(mark) / int(question_amount))) * 100)
                        print("You answered", score_percentage, "percent correct!")  # calculate score in percent
                        if score_percentage < 40:
                            print("aww have a better luck next time")
                        elif 40 <= score_percentage <= 60:
                            print("Good job!", user_name, 'you done well')
                        elif 60 < score_percentage <= 80:
                            print("Wow you done very good", user_name, "!")
                        elif 80 < score_percentage <= 99:
                            print("That so crazy, are you a genius?", user_name)
                        elif score_percentage > 99:
                            print("Wow", user_name, " you are a genius!")

                        summary_score = (str(("\nStudent name: " + str(user_name) +
                                              " gets " + str(mark) + " out of " + str(question_amount) + " mark(s) or "
                                              + str(score_percentage) + " percent(s)" + " on difficulty level " +
                                              str(difficulty))))
                        history = open("History.txt", 'a')
                        history.write(summary_score)
                        history.close()

                        asking = ask_me_a_question("Do you want to try again?", "Yes", "No")
                        if asking == '1':
                            pass
                        elif asking == '2':
                            input("Bye!\n Press enter to exit")
                            exit()

                    elif asking == '2':
                        print("okay!\n\n\n")

        except ValueError as error:  # error handling
            if before_the_question:  # something went wrong before the test
                print("Oops! only type a number :)")
                looping_before = True

            elif in_the_question:  # if something went wrong while in test (this should never happen)
                print("This is an error message, occur while in the question:", error)
                print("This is should not happening please contact the author")
                # print(traceback.format_exc())  # uncomment 'traceback' module before use (testing purpose only)
                input()
                exit()

            elif after_the_question:
                print("This is an error message, occur after the question:", error)
                print("Unexpected error contact the author right now")
                # print(traceback.format_exc())  # uncomment 'traceback' module before use (testing purpose only)
                input()
                exit()

            else:  # I have no word for this. This one will never happen (hopefully)
                print("This is an error message", error)
                print("Unexpected error contact the author right now")
                # print(traceback.format_exc())  # uncomment 'traceback' module before use (testing purpose only)
                input()
                exit()
else:
    input("OK... so why are you here?\n Press enter to exit\n")
