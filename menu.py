from week0.christmastree import printTree
from week0.ship import printShip
from week0.swap import swap
from week0.matrix import print_matr
from week1.fibonacci import printFibo
from week1.lists import InfoDb
from week2.factorial import printFact
from week1.loops import for_loop, while_loop, recursive_loop
from week2.gcd import gcdtest
from week2.palindrome import paltest
from week3.factor import normal_factor
import time
import os
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
ANSI_CLEAR_SCREEN = u"\u001B[2J"
# menu constructor
def buildMenu(menu):
    for key, value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}")
    print("\u001b[34m What is your choice? (enter the number value) ")

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
# menu bar build code
def printmenubar(n, display=None):
    # os.system("cls")
    ocean_print()
    print("\033[34m=" * n)
    if display:
        print("=", " " * int((n - 5 - len(display)) / 2), f"{display}", " " * int((n - 5 - len(display)) / 2), "=")
    else:
        print("=", " " * (n - 4), "=")
    print("=" * n, "\033[0m")

# print menu
def presentMenu(menu):
    for x in range(49):
        printmenubar(x)
        time.sleep(0.01)
    printmenubar(50, "Python Main Menu")
    buildMenu(menu)
    # error handling
    choice = input()
    options = [1, 2, 3, 4]
    while choice not in options:
        choice = int(input("Please select a valid item. "))       
    if (choice) in menu:
        if menu[choice]["type"] == "func":
            menu[choice]["exec"]()

        else:
            presentMenu(menu[choice]["exec"])


mathMenu = {
    1: {
        "display": "Fibonacci",
        "exec": printFibo,
        "type": "func"
    },
    2: {
        "display": "Factorial",
        "exec": printFact,
        "type": "func"
    },
    3: {
        "display": "GCD",
        "exec": gcdtest,
        "type": "func"
    },
    4: {
        "display": "Factor",
        "exec": normal_factor,
        "type": "func"
    },
    5: {
        "display": "Quit",
        "exec": quit,
        "type": "func"
    }
}

hack2Menu = {
    1: {
        "display": "For loop",
        "exec": for_loop,
        "type": "func"
    },
    2: {
        "display": "While loop",
        "exec": while_loop,
        "type": "func"
    },
    3: {
        "display": "Recursive",
        "exec": recursive_loop,
        "type": "func"
    },
    4: {
        "display": "Quit program",
        "exec": quit,
        "type": "func"
    },
}
drawingMenu = {
    1: {"display": "Christmas Tree",
        "exec": printTree,
        "type": "func"},
    2: {"display": "Ship",
        "exec": printShip,
        "type": "func"},
    3: {"display": "Matrix",
        "exec": print_matr,
        "type": "func"},
    4: {"display": "Swap",
        "exec": swap,
        "type": "func"},
    5: {
        "display": "Quit",
        "exec": quit,
        "type": "func"
    }
}
#submenus which go to specific files
listMenu = {
    1: {"display": "Lists and Loops",
        "exec": hack2Menu,
        "type": "submenu"
        },
    2: {
        "display": "Palindrome",
        "exec": paltest,
        "type": "func"
    },
    3: {
        "display": "Quit",
        "exec": quit,
        "type": "func"
    }
}
# main menu which directs to files organized by topics
mainMenu = {
    1: {
        "display": "Math Menu (Fibo, Factorial, GCD)",
        "exec": mathMenu,
        "type": "submenu"
    },
    2: {
        "display": "Drawing Menu (Matrix, Ship, Christmas Tree)",
        "exec": drawingMenu,
        "type": "submenu"
    },
    3: {
        "display": "List Menu (Lists, Loops, Pali)",
        "exec": listMenu,
        "type": "submenu"
    },
    4: {
        "display": "Quit",
        "exec": quit,
        "type": "func"
    }
}

if __name__ == "__main__":
    presentMenu(mainMenu)
