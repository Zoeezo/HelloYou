from time import sleep, gmtime, strftime
from os import system, name
import datetime
import sys
import random

username = "Al zie je dit is er iets fout gegaan!"
delay = 0.7
writeDelay = 0.06

def write(text):
    string = ""
    length = len(text)
    index = 0

    for i in text:
        string += i

        if (length - 1 == index):
            print(string)
            index = 0
        else:
            print(string, end="\r", flush=True)
            index += 1
            sleep(writeDelay)


def clearConsole():
    if name == 'nt': # Windows
        _ = system('cls') 
    else: # Mac/Linux
        _ = system('clear') 

def guessTheNumber():
    print("=-=-= V0.1 Hello you =-=-=")
    print()
    sleep(delay)

    write("Ik heb een nummer in gedachten, probeer het te raden! (Getal tussen 1 en 10)")
    print()

    number = random.random() * 10
    number = int(number)
    x = 1
    userInput = ""
    winner = False

    while True:
        if(x > 3):
             break
        
        userInput = input("Kans " + str(x) + "/3: ")

        if (userInput != "1" and userInput != "2" and userInput != "3" and userInput != "4" and userInput != "5" and userInput != "6" and userInput != "7" and userInput != "8" and userInput != "9" and userInput != "10"):
            print()
            write("ERROR: invoer is ongeldig, probeer het opnieuw:")
        else:
            if(int(userInput) == number):
                winner = True
                break
            else:
                print()
                if(int(userInput) > number):
                    write("Dat is fout. Het nummer is lager, probeer het opnieuw:")
                else:
                    write("Dat is fout. Het nummer is hoger, probeer het opnieuw:")
 
                x += 1
    
    if(winner):
        print()
        write("Je hebt gewonnen! GGs.")
    else:
        print()
        write("Je hebt verloren... Het nummer was: " + str(number))
    
    print()
    write("Druk op een knop om naar het hoofdmenu te gaan!")
    input()

    clearConsole()
    openMenu()     

    
                
def openDateScreen():
    print("=-=-= V0.1 Hello you =-=-=")
    print()
    sleep(delay)

    currentTime = datetime.datetime.now()

    write("Hello " + username + "! De datum is " + str(currentTime.day) + "/" + str(currentTime.month) + "/" + str(currentTime.year) + " en het is " + str(currentTime.hour) + ":" + str(currentTime.minute) + "!")
    print()
    write("Druk op een knop om naar het hoofdmenu te gaan!")
    input()

    clearConsole()
    openMenu()

def changeName():
    global username

    print("=-=-= V0.1 Hello you =-=-=")
    print()
    sleep(delay)

    write("Hello " + username + ", je wilt dus je naam aanpassen?")

    userInput = ""
    while True:
        userInput = input("Y/N: ")

        if(userInput != "Y" and userInput != "y" and userInput != "N" and userInput != "n"):
            print()
            write("ERROR: invoer is ongeldig, probeer het opnieuw:")
        else:
            break
    
    if(userInput == "N" or userInput == "n"):
        print()
        write("Ok, " + username + "! Je naam is niet aangepast.")
        write("Druk op een knop om naar het hoofdmenu te gaan!")
        input()

        clearConsole()
        openMenu()
    else:
        print()
        write("Waar wil je je naam naar veranderen?")
        username = input()

        print()
        write("Ok, je naam is nu " + username + "!")
        write("Druk op een knop om naar het hoofdmenu te gaan!")
        input()

        clearConsole()
        openMenu()      

def closeProgram():
    print("=-=-= V0.1 Hello you =-=-=")
    print()
    sleep(delay)

    write("Dag dag!")
    sleep(3)
    sys.exit()

def openMenu():
    print("=-=-= V0.1 Hello you =-=-=")
    print()
    sleep(delay)

    write("Hello " + username + ", welkom op het hoofdmenu!")
    print()
    print("1 - Datum & tijd weergeven")
    sleep(delay)
    print("2 - Naam aanpassen")
    sleep(delay)
    print("3 - Raad het nummer")
    sleep(delay)
    print("4 - Programma beëindigen")
    print()
    sleep(delay)
    write("Kies wat je wilt doen (1-4):")

    userInput = ""

    while True:
        userInput = input()

        if(userInput != "1" and userInput != "2" and userInput != "3" and userInput != "4"):
            print()
            write("ERROR: invoer is ongeldig, probeer het opnieuw:")
        else:
            break
    
    clearConsole()

    if(userInput == "1"):
        openDateScreen()
    elif(userInput == "2"):
        changeName()
    elif(userInput == "3"):
        guessTheNumber()
    elif(userInput == "4"):
        closeProgram()

def setup():
    global username

    print("=-=-= V0.1 Hello you =-=-=")
    print()
    sleep(delay)

    write("Hello you!, ik ben Zoey.")
    print()
    write("Wie ben jij?")
    username = input("")
    print()
    write("Hello " + username + "!")
    print()
    write("Druk op een knop om naar het hoofdmenu te gaan!")
    input()

    clearConsole()
    openMenu()

setup()