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
    myList = listIn
    editMore = True
    while editMore:
        validEdit = False
        while not validEdit:
            viewList(myList)
            print("Enter an item name or number to edit (or 'quit to return')")
            toEdit = input (" --> ")

            try:
                toEdit =  int(toEdit) - 1
                if toEdit <= len(myList) and toEdit >= 0:
                    validEdit = True
                else:
                    print("Invalid Choice - Try Again!")                    
                print("Please enter new item.")
            except ValueError:
                if toEdit in myList:
                    toEdit = myList.index(toEdit)
                    validEdit = True  
                elif toEdit in ["quit"]:
                    validEdit = True                      
                else:
                    print("Invalid Choice - Try Again!")

        if toEdit in ["done", "quit", "exit", "return"]:
            editMore = False
        else:
            print("Enter New Item.")
            newEntry = input(" --> ")
            myList[toEdit] = newEntry
    saveList(myList)


def moveItems(listIn):
    myList = listIn
    moveMore = True
    while moveMore:
        validMoveFrom = False
        while not validMoveFrom:
            viewList(myList)
            print("Enter an item name or number to move")
            moveFrom = input (" --> ")

            try:
                moveFrom =  int(moveFrom) - 1
                if 0 <= moveFrom < len(myList):
                    validMoveFrom = True
                else:
                    print("Invalid Choice - Try Again!")                    
            except ValueError:
                if moveFrom in myList:
                    moveFrom = myList.index(moveFrom)
                    validMoveFrom = True  
                elif moveFrom in ["quit"]:
                    validMoveFrom = True                      
                else:
                    print("Invalid Choice - Try Again!")

        if moveFrom in ["done", "quit", "exit", "return"]:
            moveMore = False
        else:
            validMoveTo = False
            while not validMoveTo:
                print("Enter New Position For The Item.")
                toMove = input(" --> ")

                try:
                    toMove = int(toMove) - 1
                    if 0 <= toMove < len(myList) and toMove != moveFrom:
                        validMoveTo = True
                    else:
                        print("Invalid Choice - Try Again!")
                except ValueError:
                    if toMove in ["quit"]:
                        validMoveTo = True
                    else:
                        print("Invalid Choice - Try Again!")

            if toMove in ["quit"]:
                moveMore = False
            else:
                inTransit = myList.pop(moveFrom)
                myList.insert(toMove, inTransit)

    saveList(myList)


def loadList():
    try:
        with open("groceries.txt", "r") as file:
            loadedList = file.readlines()
            for idx in range(len(loadedList)):
                loadedList[idx] = loadedList[idx].replace("\n", "")
    except FileNotFoundError:
        loadedList = []

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