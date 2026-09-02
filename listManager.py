# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def optionsMenu():
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("         LIST MANAGER")
    print("")
    print("         1. VIEW LIST")
    print("         2. ADD ITEMS")
    print("         3. REMOVE ITEMS")
    print("         4. EDIT ITEMS")
    print("         5. MOVE ITEMS")
    print("         6. EXIT")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")    


def viewList():
    loadList()
    # Something


def addItems():
    loadList()
    # Something
    saveList()

def removeItems():
    loadList()
    # Something
    saveList()

def editItems():
    loadList()
    # Something
    saveList()

def moveItems():
    loadList()
    # Something
    saveList()

def loadList():
    try:
        with open("groceries.txt", "r") as file:
            loadedList = file.readlines()
            for idx in range(len(loadedList)):
                loadedList[idx] = loadedList[idx].replace("\n", "")
    except FileNotFoundError:
        loadedList = []

    return loadedList


def saveList():
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    options = {1: viewList,
               2: addItems,
               3: removeItems,
               4: editItems,
               5:moveItems}

    appOn = True
    while appOn:
        validOptionsChoice = False
        while not validOptionsChoice:
            optionsMenu()
            userChoice = input(" --> ").lower()
            if userChoice in ["1", "1.", "1 view list", "1. view list"]:
                userChoice = 1
                validOptionsChoice = True
            elif userChoice in ["2", "2.", "2 add items", "2. add items"]:
                userChoice = 2
                validOptionsChoice = True
            elif userChoice in ["3", "3.", "3 remove items", "3. remove items"]:
                userChoice = 3
                validOptionsChoice = True
            elif userChoice in ["4", "4.", "4 edit items", "4. edit items"]:
                userChoice = 4
                validOptionsChoice = True
            elif userChoice in ["5", "5.", "5 move items", "5. move items"]:
                userChoice = 5
                validOptionsChoice = True                
            elif userChoice in ["6", "6.", "6 exit", "6. exit"]:
                userChoice = 6
                validOptionsChoice = True
            else:
                print("Invalid Choice - Try Again!")

        if userChoice == 6:
            appOn = False
        else:
            options[userChoice]()



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()