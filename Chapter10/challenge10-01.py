import random

def hangman(word):
    win = False
    wrong = 0

    rLetters = list(word)
    board = ["_"] * len(word)

    stages = ["",
              "_______       ",
              "|      |      ",
              "|      O      ",
              "|     /|\\     ",
              "|     / \\     ",
              "|             "
              ]

    while wrong < len(stages):
        print("\n")
        print(" ".join(board))
        print("\n".join(stages[0:wrong+1]))
        print("({}/{})".format(wrong, len(stages) - 1))

        if "_" not in board:
            print("You Win!")
            print("The word was: {}".format(word))
            win = True
            break

        if wrong+1 == len(stages):
            print("You Lose!")
            print("The word was: {}".format(word))
            break

        userInput = input("Guess a letter: ")
        if userInput in rLetters:
            ind = rLetters.index(userInput)
            board[ind] = userInput
            rLetters[ind] = "$"
        else:
            wrong += 1



questions = ["apple",
             "banana",
             "cat",
             "dragon",
             "japan",
             "authentic",
             "consecutive",
             "optimistic",
             "frequency",
             "unconscious",
             "structure",
             "conviction",
             "corridor"
            ]

hangman(questions[random.randint(0, len(questions) - 1)])

