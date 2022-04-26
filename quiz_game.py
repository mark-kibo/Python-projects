# the game requires 4  functions

def new_game():
    guesses = []
    correct_guesses = 0
    question_num =1

    for key in questions:
        print("-----------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        question_num += 1
        guess = input("Enter (A, B, C OR D :").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
    score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0
def score(correct_guesses, guesses):
    print("---------")
    print("RESULTS")
    print("---------")
    print("ANSWERS:", end=" ")
    for j in questions:
        print(questions.get(j), end=" ")

    print()#new line

    print("guesses:", end=" ")
    for i in guesses:
        print(i, end=" ")

    print()#new line
    score1 = int((correct_guesses /len(questions)) * 100)
    print("Your score is:" + str(score1) + "%")

def play_again():
    response = input("Do you wish to play again? (Yes or No):").upper()

    if response == "YES":
        return  True
    else:
        return False

#each question
questions = {
    "who created python?": "A",
    "what year was python created?": "B",
    "Python is tributed to which comedy group?" : "C",
    "Is the earth round?": "A"
}
#answers for each question
options = [["A. Guido van  Rossum ", "B. Elon Musk", "C. Bill gates", "D.Mak zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty python", "D. SNL"]
           ["A. True", "B. False", "C. sometimes", "D. What's earth"]]

new_game()

while play_again():
    new_game()

print()#new line
print("thank you for choosing us #kibby_python")