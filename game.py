
room = 'tutorial_start'
solves = 0
red_solves = 0
blue_solves = 0
black_solves = 0
game_running = True
BLACK = '\033[30m'
RED = '\033[31m'
BLUE = '\033[34m'
RESET = '\033[0m'

while game_running:
    if room == 'tutorial_start':
        print("Hello! Welcome to Linglox!\nThis game is all about logic and lingo, you'll have to solve puzzles to beat the game!\nBut how do you play? Well, lets start off with this simple puzzle.\n")
        print("Puzzles will come in the form of rows, looking something like this:\n\n# ['Left', 'Middle', 'Right']\n\nAfter the puzzle is given, you will have to input an answer.\nIt will also give the amount of letters in the answer\nLets try a puzzle now!\n\n")
        room = 'tutorial_middle'
    if room == 'tutorial_middle':
        print("The answer to this puzzle is 'hello', can you guess why?\n\n5 ['', 'hello', '']\n\n")
        answer = input("Type your answer: ").lower()
        if answer == "hello":
            print("Good job! Did you guess why it was right?\nWhen the middle word is given, you type the same word! Lets try a different puzzle now.")
            room = 'tutorial_left'
        else:
            print("That's incorrect, let's try that again.")
    if room == 'tutorial_left':
        print("\nHere's a new puzzle, also, theres a rule I forgot to mention:\nEvery word in a puzzle will have the same answer.\nCan you find out what left means?\n\n2 ['high', 'hi', '']")
        answer = input("Type your answer: ").lower()
        if answer == "hi":
            print("Good job! Did you guess why it was right?\nWhen the left word is given, the answer is a homophone, meaning that when you say the word out loud, it will sound like a different word\nLets try a different puzzle now.")
            room = 'tutorial_right'
        else:
            print("That's incorrect, let's try that again.")
    if room == 'tutorial_right':
        print("\nHere's a new puzzle, can you find out what right means?\n\n3 ['', 'low', 'bottom']")
        answer = input("Type your answer: ").lower()
        if answer == "low":
            print("Good job! Did you guess why it was right?\nWhen the right word is given, the answer is a synonym, meaning that the answer has a similar meaning to the given word\nLets try a different puzzle now.")
            room = 'tutorial_color'
        else:
            print("That's incorrect, let's try that again.")
    if room == 'tutorial_color':
        print("\nHere's a new puzzle, and would you look at that?\nthe text is in a different color! Can you guess what the answer is?\n\n5 ['', '" + BLACK + "bye" + RESET + "', '']")
        answer = input("Type your answer: ").lower()
        if answer == "hello":
            print("Good job! Did you guess why it was right?\nWhen the word is black, the answer is the opposite of what is says, meaning that the answer is the direct opposite of the word.\nI think you are ready to face off against the main game now.\n")
            room = 'pre_start'
        else:
            print("That's incorrect, let's try that again. Here's a hint: let's consider black as the opposite of white, so what would be the opposite of bye?")
    if room ==  'pre_start':
        print("Before you you see a big room, you know that once you enter it you cannot escape until you have completes all of the puzzles.\n")
        answer = input("Are you ready?: ").lower()
        if answer == "yes" or answer == "yea" or answer == "yeah" or answer == "im ready" or answer == "i'm ready":
            print("Then let's enter the room.\n")
            room = 'start'
        else:
            print("Well too bad because you're entering the room anyway.\n")
            room = 'start'
    if room == 'start':
        print("In front of you lies a large gate, and three different doors, each in a different color, them being red, blue, and black. Once you are in a room you can type 'exit' to leave the room and come back at any time.")
        answer = input("Where will you go first?\nPlease type '1' for the Gate, '2' for the Red Door, '3' for the Blue Door, and '4' for the Black Door: ")
        if answer == '1':
            room = 'gate'
        elif answer == '2':
            room = 'red'
        elif answer == '3':
            room = 'blue'
        elif answer == '4':
            room = 'black'
        else:
            print("Please type one of the four listed numbers to traverse.")
    if room == 'gate':
        if solves == 9:
            print("You solved all the puzzles and the door has opened! You win!")
            game_running = False
        else:
            print("\n\nThe gate shows a number on it saying how many puzzles need to be solved for it to open. The gate says " + str(9 - solves) + " and you have solved " + str(solves) + " puzzles so far.")
            room = 'start'
    if room == 'red':
        print("The color red's gimmick is subtracting letters")
        if red_solves == 0:
            print("3 ['', '" + RED + "below" + RESET + "', 'bottom']")
            answer = input("Type your answer: ")
            if answer == 'low':
                red_solves += 1
                solves += 1
                print("Correct!")
            elif answer == 'exit':
                room =  'start'
            else:
                print("Incorrect!")
        if red_solves == 1:
            print("6 ['let her', '', '" + RED + "word" + RESET + "']")
            answer = input("Type your answer: ")
            if answer == 'letter':
                red_solves += 1
                solves += 1
                print("Correct!")
            elif answer == 'exit':
                room =  'start'
            else:
                print("Incorrect!")
        if red_solves == 2:
            print("5 ['" + RED + "brute" + RESET + "', '"+RED+"router"+RESET+"', '']")
            answer = input("Type your answer: ")
            if answer == 'route':
                red_solves += 1
                solves += 1
                print("Correct!")
            elif answer == 'exit':
                room =  'start'
            else:
                print("Incorrect!")
        if red_solves == 3:
            print("You have solved all the puzzles in the Red Room!")
            room =  'start'
    if room == 'blue':
        print("The color blue's gimmick is adding letters")
        if blue_solves == 0:
            print("8 ['', '" + BLUE + "add" + RESET + "', '']")
            answer = input("Type your answer: ")
            if answer == 'addition':
                blue_solves += 1
                solves += 1
                print("Correct!")
            elif answer == 'exit':
                room =  'start'
            else:
                print("Incorrect!")
        if blue_solves == 1:
            print("7 ['coquet', '', '"+BLUE+"flower"+RESET+"']")
            answer = input("Type your answer: ")
            if answer == 'bouquet':
                blue_solves += 1
                solves += 1
                print("Correct!")
            elif answer == 'exit':
                room =  'start'
            else:
                print("Incorrect!")
        if blue_solves == 2:
            print("4 ['"+BLUE+"eye"+RESET+"', '"+RED+"ideally"+RESET+"', '']")
            answer = input("Type your answer: ")
            if answer == 'idea':
                blue_solves += 1
                solves += 1
                print("Correct!")
            elif answer == 'exit':
                room =  'start'
            else:
                print("Incorrect!")
        if blue_solves == 3:
            print("You have solved all the puzzles in the Blue Room!")
            room =  'start'
    if room == 'black':
        print("The color black's gimmick is opposition")
        if black_solves == 0:
            print("5 ['', '" + BLACK + "adult" + RESET + "', '']")
            answer = input("Type your answer: ")
            if answer == 'child':
                black_solves += 1
                solves += 1
                print("Correct!")
            elif answer == 'exit':
                room =  'start'
            else:
                print("Incorrect!")
        if black_solves == 1:
            print("4 ['flu', '', '"+BLACK+"wolf"+RESET+"']")
            answer = input("Type your answer: ")
            if answer == 'flow':
                black_solves += 1
                solves += 1
                print("Correct!")
            elif answer == 'exit':
                room =  'start'
            else:
                print("Incorrect!")
        if black_solves == 2:
            print("4 ['"+BLACK+"tube"+RESET+"', '"+RED+"boots"+RESET+"', '']")
            answer = input("Type your answer: ")
            if answer == 'boot':
                black_solves += 1
                solves += 1
                print("Correct!")
            elif answer == 'exit':
                room =  'start'
            else:
                print("Incorrect!")
        if black_solves == 3:
            print("You have solved all the puzzles in the Black Room!")
            room =  'start'
            
            
