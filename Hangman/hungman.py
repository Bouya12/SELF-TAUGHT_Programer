"""
Edit Day : 2019/04/22
"""

def hangman(word):
    wrong = 0
    stages = ["",
              "_____     ",
              "|         ",
              "|    |    ",
              "|    O    ",
              "|   /|\   ",
              "|   / \   ",
              "          "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hungman!")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Please guess 1 character : "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose... The answer is {}.".format(word))
 
hangman("cat")       