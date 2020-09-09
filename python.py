from time import sleep

username = "Al zie je dit is er iets fout gegaan!"

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
            sleep(0.1)


def setup():
    global username

    write("Hello you!, ik ben Zoey.")
    sleep(1)

    write("Wie ben jij?")
    username = input("")
    sleep(1)

    write("Hello " + username)
    input()

setup()