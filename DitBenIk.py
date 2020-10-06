from time import sleep
from os import system, name
from random import randint

writeDelay = 0.06
username = "Al zie je dit is er iets fout gegaan!"

questions = {1: {'used': False, 'question': 'Waar woon ik?', 'answer1': 'Heerhugowaard', 'answer2': 'Spierdijk', 'answer3': 'Obdam', 'correctAnswer': 2},
             2: {'used': False, 'question': 'Hoe oud ben ik?', 'answer1': '16', 'answer2': '17', 'answer3': '18', 'correctAnswer': 1},
             3: {'used': False, 'question': 'Hoeveel katten heb ik?', 'answer1': '5', 'answer2': '4', 'answer3': '3', 'correctAnswer': 3}}

usedQuestions = 0
maxQuestions = len(questions)
correctAnswers = 0

running = True

def write(text):
    string = ""
    length = len(text)
    index = 0

    for i in text:
        string += i

        # Als het de laatste char in de string is.
        if (length - 1 == index):
            print(string)
        else:
            print(string, end="\r", flush=True)
            index += 1
            sleep(writeDelay)

def clearConsole():
    if name == 'nt': # Windows
        _ = system('cls')
    else: # Mac/Linux
        _ = system('clear')

def askQuestion():
    global running
    global usedQuestions
    global correctAnswers
    global questions

    print("=-=-= V1 Dit ben ik =-=-=")
    print()

    question = randint(1, 3)
    answer = " "

    while True:
        if (questions[question]['used']):
            question += 1

            if (question > maxQuestions):
                question = 1
        else:
            break
    
    print("Vraag: " + str(usedQuestions + 1) + '/' + str(maxQuestions) + " | Score: " + str(correctAnswers) + '/' + str(maxQuestions))
    
    write(questions[question]['question'])
    print()
    print("A -" + questions[question]['answer1'])
    print("B -" + questions[question]['answer2'])
    print("C -" + questions[question]['answer3'])

    while True:
        answer = input("Antwoord (A/B/C): ").lower()

        if (answer == 'a'):
            answer = 1
            break
        elif (answer == 'b'):
            answer = 2
            break
        elif (answer == 'c'):
            answer = 3
            break
        else:
            write("Dat antwoord is ongeldig...")
            print()
    
    print()
    if (answer == questions[question]['correctAnswer']):
        write('Dat is correct!')
        correctAnswers += 1
    else:
        write('Dat is fout!')

    print()
    write("Druk op enter om door te gaan!")
    input()

    questions[question]['used'] = True
    usedQuestions += 1

    if (usedQuestions == maxQuestions):
        running = False

def reset():
    global running
    global usedQuestions
    global correctAnswers
    global questions

    running = True
    usedQuestions = 0
    correctAnswers = 0
    
    x = 1
    while (x <= maxQuestions):
        questions[x]['used'] = False
        x += 1

def endscreen():
    print("=-=-= V1 Dit ben ik =-=-=")
    print()

    write('Hello ' + username + ', je had ' + str(correctAnswers) + ' van de ' + str(maxQuestions) + ' vragen goed!')
    write("Wil je de quiz opnieuw doen?")

    answer = ' '

    while True:
        answer = input('(Y/N): ').lower()

        if (answer == 'y' or answer == 'n'):
            break
        else:
            write("Dat antwoord is ongeldig...")
            print()

    if (answer == 'y'):
        reset()
        clearConsole()
        quiz()

def quiz():
    while running:
        askQuestion()
        clearConsole()
    endscreen()

def begin():
    global username

    print("=-=-= V1 Dit ben ik =-=-=")
    print()

    write("Hello you!, ik ben Zoey.")
    print()
    write("Wie ben jij?")
    username = input("")
    print()
    write("Hello " + username + "!")
    print()
    write("Druk op enter om door te gaan!")
    input()

    clearConsole()
    quiz()

begin()