from week0.christmastree import printTree
from week0.ship import printShip
from week0.swap import swap
from week0.matrix import print_matr
from week1.fibonacci import printFibo
from week1.lists import InfoDb
from week1.loops import for_loop,while_loop,recursive_loop

def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}")
    print("What is your choice? (enter the number value) ")

def presentMenu(menu):
    buildMenu(menu)
    choice = int(input())
    while choice not in menu:
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func":
            menu[choice]["exec"]()

        else:
            presentMenu(menu[choice]["exec"])
subMenu = {
    1: {"display":"Swap",
    "exec":swap,
    "type":"func"},
    2: {"display":"Matrix",
    "type":"func",
    "exec": print_matr},
    3: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }

}
hack2Menu = {
    1: {
        "display":"For loop",
        "exec": for_loop,
        "type":"func"
    },
    2: {
        "display":"While loop",
        "exec": while_loop,
        "type":"func"
    },
    3: {
        "display":"Recursive",
        "exec": recursive_loop,
        "type":"func"
    },
    4: {
        "display":"Quit program",
        "exec": quit,
        "type":"func"
    },
}
mainMenu = {
    1: {"display":"Christmas Tree",
    "exec":printTree,
    "type":"func"},
    2: {"display":"Ship",
    "exec":printShip,
    "type":"func"},
    3: {
        "display":"Tri2",
        "exec": subMenu,
        "type":"submenu"
    },
    4: {
        "display":"Fibonacci",
        "exec": printFibo,
        "type":"func"
    },
    5: {
        "display":"Lists and Loops",
        "exec": hack2Menu,
        "type":"submenu"
    },
    6: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}

if __name__ == "__main__":
  presentMenu(mainMenu)
