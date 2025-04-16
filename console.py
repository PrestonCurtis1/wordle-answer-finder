import solver
import json
def writeFile():#writes json file for solver
    containedInput = input("what letters are contained type letter then spot eg (a1a2e3):\t")
    containedList = []
    if (len(containedInput) % 2) == 0:#makes sure there is an even amount of characters
        for index in range(0,len(containedInput)-1,2):
            letter = containedInput[index]
            if not letter.isalpha():
                # Clear previous content
                print(f"expected letter in contained:{index}")
                return False
            try:
                location = int(containedInput[index+1])
            except ValueError:
                print(f"expected int in contained:{index+1}")
                return False
            else:
                containedList.append({"letter":letter,"location":location})
    else:
        print("Number of characters in found is not even:")
        return False
    foundInput = input("what letters are correct type letter then spot eg (a1p2):\t")
    foundList = []
    if (len(foundInput) % 2) == 0:#makes sure there is an even amount of characters
        for index in range(0,len(foundInput)-1,2):
            letter = foundInput[index]
            if not letter.isalpha():
                print(f"expected letter in found:{index}")
                return False
            try:
                spot = int(foundInput[index+1])
            except ValueError:
                print(f"expected int in found:{index}")
                return False
            else:
                foundList.append({"letter":letter,"spot":spot})
    else:
        print("Number of characters in found is not even:")
        return False
    excludedInput = input("what letters are excluded:\t")
    excludedString = ""
    for character in excludedInput:#make sure an included character or found character is not excluded
        if character not in foundInput and character not in containedInput:
            excludedString += character
    amountInput = input("Any duplicate letters? E.g. apple → p2, sassy → s3:\t")
    amountList = []
    if (len(amountInput) % 2) == 0:#makes sure there is an even amount of characters
        for index in range(0,len(amountInput)-1,2):
            letter = amountInput[index]
            if not letter.isalpha():
                print(f"expected letter in found:{index}")
                return False
            try:
                amount = int(amountInput[index+1])
            except ValueError:
                print(f"expected int in found:{index+1}")
                return False
            else:
                amountList.append({"letter":letter,"amount":amount})
    else:
        print(f"Number of characters in found is not even:")
        return False
    fileDict = {"contains":containedList,"excludes":excludedString,"found":foundList,"amount":amountList}#combine into a dictionary
    with open("data.json","w") as file:#use dictionary to write to a json file
        json.dump(fileDict,file)
    print(solver.display(solver.findWords()))
    return True
while True:
    if(writeFile()):
        break