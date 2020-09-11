from time import sleep, gmtime, strftime
from os import system, name
import datetime
import sys
from random import randint

username = "Al zie je dit is er iets fout gegaan!"
delay = 0.7
writeDelay = 0.06

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

def guessTheNumber():
    print("=-=-= V0.1 Hello you =-=-=")
    print()
    sleep(delay)

    write("Ik heb een getal in gedachten, probeer het te raden! (Getal tussen 1 en 10)")
    print()

    number = randint(1, 10)

    guesses = 1
    userInput = ""
    userGetal = 0
    winner = False

    while True:
        # Als guesses groter is dan 3 heeft de gebruiker dus 3 keer geraden.
        if(guesses > 3):
             break
        
        userInput = input("Kans " + str(guesses) + "/3: ")

        # Probeer de userInput naar een integer te converteren
        try:
            userGetal = int(userInput)
        # Als het niet kan is de invoer ongeldig
        except:
            print()
            write("ERROR: invoer is ongeldig, probeer het opnieuw:")
            continue
            
        # Als het getal groter is dan 10 of kleiner dan 1 is de invoer ook ongeldig
        if(userGetal > 10 or userGetal < 1):
            print()
            write("ERROR: invoer is ongeldig, probeer het opnieuw:")
            continue

        # Als de userInput het goede getal is.
        if(userGetal == number):
            winner = True
            break
        else:
            print()
            # Als de userInput hoger is dan het goede getal.
            if(userGetal > number):
                write("Dat is fout. Het getal is lager!")
            # Anders is de userInput dus lager dan het goede getal.
            else:
                write("Dat is fout. Het getal is hoger!")
 
            guesses += 1
    
    # Als de gebruiker heeft gewonnen.
    if(winner):
        print()
        write("Je hebt gewonnen! GGs.")
    # Anders heeft de gebruiker dus verloren.
    else:
        print()
        write("Je hebt verloren... Het getal was: " + str(number))
    
    print()
    write("Druk op een knop om naar het hoofdmenu te gaan!")
    input()

    clearConsole()
    openMenu()
                
def openDateScreen():
    print("=-=-= V0.1 Hello you =-=-=")
    print()
    sleep(delay)

    # We krijgen een datetime object met veel informatie.
    currentTime = datetime.datetime.now()

    # We pakken steeds informatie uit de datetime object.
    time = str(currentTime.hour) + ":" + str(currentTime.minute) 
    date = str(currentTime.day) + "/" + str(currentTime.month) + "/" + str(currentTime.year)

    write("Hello " + username + "! De datum is " + date + " en het is " + time + "!")
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
        # .lower() zorgt ervoor dat de input altijd lowercase is dus Y, y, N of n maakt niet uit.
        userInput = input("Y/N: ").lower()

        # Als de input "n" is.
        if(userInput == "n"):
            print()
            write("Ok, " + username + "! Je naam is niet aangepast.")
            print()
            write("Druk op een knop om naar het hoofdmenu te gaan!")
            input()

            break
        # Anders als de input "y" is.
        elif(userInput == "y"):
            print()
            write("Waar wil je je naam naar veranderen?")
            username = input()

            print()
            write("Ok, je naam is nu " + username + "!")
            print()
            write("Druk op een knop om naar het hoofdmenu te gaan!")
            input()

            break
        # Anders is de input ongeldig.
        else:
            print()
            write("ERROR: invoer is ongeldig, probeer het opnieuw:")

        clearConsole()
        openMenu()      

def closeProgram():
    print("=-=-= V0.1 Hello you =-=-=")
    print()
    sleep(delay)

    write("Dag dag!")
    sleep(2)
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
    print("3 - Raad het getal")
    sleep(delay)
    print("4 - Programma beëindigen")
    print()
    sleep(delay)
    write("Kies wat je wilt doen (1-4):")

    userInput = ""
    userGetal = 0

    while True:
        userInput = input()

        # Probeer de input naar een integer te converteren.
        try:
            userGetal = int(userInput)
        # Als het mislukt printen we een error en gaan we terug naar het begin van de loop.
        except:
            print()
            write("ERROR: invoer is ongeldig, probeer het opnieuw:")
            continue

        # Als het getal groter dan 4 en kleiner dan 1 is printen we een error en gaan we terug naar het begin van de loop.
        if(userGetal > 4 or userGetal < 1):
            print()
            write("ERROR: invoer is ongeldig, probeer het opnieuw:")
            continue

        clearConsole()

        # We kijken welk getal de gebruiker heeft ingevoerd.
        if(userGetal == 1):
            openDateScreen()
        elif(userGetal == 2):
            changeName()
        elif(userGetal == 3):
            guessTheNumber()
        elif(userGetal == 4):
            closeProgram()

def begin():
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

begin()