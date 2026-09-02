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


def viewList(myList):
    myList = loadList()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("         GROCERIES")

    if len(myList) > 0:
        for idx in range (len(myList)):
            print(f"         {idx+1}. {myList[idx]}")
    else:
        print("         The list is empty!")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    


def addItems(listIn):
    myList = listIn
    addMore = True
    while addMore:
        viewList(myList)
        print("Enter an item to add(or 'quit' to return)")
        toAdd = input(" --> ")
        if toAdd in ["done", "quit", "exit", "return"]:
            addMore = False
        else:
            myList.append(toAdd)

    saveList(myList)

def removeItems(listIn):
    myList = listIn
    removeMore = True
    while removeMore:
        validRemove = False
        while not validRemove:
            viewList(myList)
            print("Enter an item or position to remove (or 'quit' to return)")
            toRemove = input(" --> ")

            try:
                toRemove = int(toRemove) - 1
                if toRemove <= len(myList):
                    validRemove = True
                else:
                    print ("Invalid Choice - Try Again!")
            except ValueError:
                if toRemove in myList:
                    toRemove = myList.index(toRemove)
                    validRemove = True
                elif toRemove in ["done", "quit", "exit", "return"]:
                    validRemove = True
                else:
                    print("Invalid Choice - Try Again!")

        if toRemove in ["done", "quit", "exit", "return"]:
            removeMore = False
        else:
            myList.pop(toRemove)
    
    saveList(myList)




def editItems(listIn):

    # Something
    saveList()


def moveItems(listIn):

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
    finally:
        return loadedList


def saveList(listIn):
    with open("groceries.txt", "w") as file:
        for idx in range(len(listIn)):
            if idx  < len(listIn) - 1:
                file.write(f"{listIn[idx]}\n")
            else:
                file.write(listIn[idx])



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
        myList = loadList()
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
            options[userChoice](myList)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()