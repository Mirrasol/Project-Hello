from colorama import Fore, Style
import time

def main():
    print(Fore.RED + "Hello!" + Style.RESET_ALL)
    time.sleep(2)
    print(Style.DIM + "Wait a second..." + Style.RESET_ALL)
    time.sleep(1)
    print("Oh, sing a song of Balduran")
    print("Who founded Baldur's Gate!")


if __name__ == '__main__':
    main()

