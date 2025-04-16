import tkinter as tk
from tkinter import Label,Entry,Button,Scrollbar,Text
import solver
import json
import os
def writeFile():#writes json file for solver
    containedInput = containedEntry.get()
    containedList = []
    if (len(containedInput) % 2) == 0:#makes sure there is an even amount of characters
        for index in range(0,len(containedInput)-1,2):
            letter = containedInput[index]
            if not letter.isalpha():
                outputBox.delete("1.0", tk.END)  # Clear previous content
                outputBox.insert(tk.END, f"expected letter in contained:{index}")
                return
            try:
                location = int(containedInput[index+1])
            except ValueError:
                outputBox.delete("1.0", tk.END)  # Clear previous content
                outputBox.insert(tk.END, f"expected int in contained:{index+1}")
                return
            else:
                containedList.append({"letter":letter,"location":location})
    else:
        outputBox.delete("1.0", tk.END)  # Clear previous content
        outputBox.insert(tk.END, f"Number of characters in found is not even:")
        return
    foundInput = foundEntry.get()
    foundList = []
    if (len(foundInput) % 2) == 0:#makes sure there is an even amount of characters
        for index in range(0,len(foundInput)-1,2):
            letter = foundInput[index]
            if not letter.isalpha():
                outputBox.delete("1.0", tk.END)  # Clear previous content
                outputBox.insert(tk.END, f"expected letter in found:{index}")
                return
            try:
                spot = int(foundInput[index+1])
            except ValueError:
                outputBox.delete("1.0", tk.END)  # Clear previous content
                outputBox.insert(tk.END, f"expected int in found:{index+1}")
                return
            else:
                foundList.append({"letter":letter,"spot":spot})
    else:
        outputBox.delete("1.0", tk.END)  # Clear previous content
        outputBox.insert(tk.END, f"Number of characters in found is not even:")
        return
    excludedInput = excludedEntry.get()
    excludedString = ""
    
    amountInput = amountEntry.get()
    amountList = []
    if (len(amountInput) % 2) == 0:#makes sure there is an even amount of characters
        for index in range(0,len(amountInput)-1,2):
            letter = amountInput[index]
            if not letter.isalpha():
                outputBox.delete("1.0", tk.END)  # Clear previous content
                outputBox.insert(tk.END, f"expected letter in found:{index}")
                return
            try:
                amount = int(amountInput[index+1])
            except ValueError:
                outputBox.delete("1.0", tk.END)  # Clear previous content
                outputBox.insert(tk.END, f"expected int in found:{index+1}")
                return
            else:
                amountList.append({"letter":letter,"amount":amount})
    else:
        outputBox.delete("1.0", tk.END)  # Clear previous content
        outputBox.insert(tk.END, f"Number of characters in found is not even:")
        return
    for character in excludedInput:#make sure an included character or found character is not excluded
        if character not in foundInput and character not in containedInput:
            excludedString += character
    fileDict = {"contains":containedList,"excludes":excludedString,"found":foundList,"amount":amountList}#combine into a dictionary
    with open("data.json","w") as file:#use dictionary to write to a json file
        json.dump(fileDict,file)
    solver.display(solver.findWords())
    with open("valid.txt","r") as file:#display possible words
        contents = file.read()
        outputBox.delete("1.0",tk.END)
        outputBox.insert(tk.END,contents)

window = tk.Tk()
window.title("Wordle Answer Finder")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")#make tkinter window fullscreen
window.configure(bg="#000000")#make dark

#title
titleLabel = Label(window,text="Wordle Solver",font=("Arial",20),fg="#FFFFFF",bg="#2B2A29")
titleLabel.grid(row=0,column=0,columnspan=2,sticky="ew")#center and take up whole row

#contained
containedLabel = Label(window,text="Letters Contained",font=("Arial",10),fg="#FFFFFF",bg="#595856")
containedLabel.grid(row=1,column=0,sticky="ew",padx=10,pady=5)
containedEntry = Entry(window,text="ex,(e2e1a3)",font=("Arial",10),fg="#FFFFFF",bg="#41403F")#letters than locations seperate items by commas
containedEntry.grid(row=1,column=1,sticky="ew",padx=10,pady=5)

#found
foundLabel = Label(window,text="Letters Found",font=("Arial",10),fg="#FFFFFF",bg="#595856")#letter then location
foundLabel.grid(row=2,column=0,sticky="ew",padx=10,pady=5)
foundEntry = Entry(window,text="ex, (u3i1)",font=("Arial",10),fg="#FFFFFF",bg="#41403F")
foundEntry.grid(row=2,column=1,sticky="ew",padx=10,pady=5)

#excluded
excludedLabel = Label(window,text="Letters Excluded",font=("",10),fg="#FFFFFF",bg="#595856")
excludedLabel.grid(row=3,column=0,sticky="ew",padx=10,pady=5)
excludedEntry = Entry(window,text="ex, (hjgke)",font=("Arial",10),fg="#FFFFFF",bg="#41403F")#no numbers
excludedEntry.grid(row=3,column=1,sticky="ew",padx=10,pady=5)
#amount
amountLabel = Label(window,text="Amount",font=("",10),fg="#FFFFFF",bg="#595856")
amountLabel.grid(row=4,column=0,sticky="ew",padx=10,pady=5)
amountEntry = Entry(window,text="ex, (a2b3)",font=("Arial",10),fg="#FFFFFF",bg="#41403F")
amountEntry.grid(row=4,column=1,sticky="ew",padx=10,pady=5)

#button
findButton = Button(window,text="Find Words",font=("Courier",10),fg="#000000",bg="#00FFFF",command=writeFile)
findButton.grid(row=5,column=0,columnspan=2,sticky="ew")

#scrollbar
scroll = Scrollbar(window,orient="vertical")
scroll.grid(row=6, column=2, sticky="ns")


#output
outputBox = Text(window, font=("Arial", 10), fg="#FFFFFF", bg="gray", yscrollcommand=scroll.set)
outputBox.insert(tk.END, "Words will be displayed here")  # Insert initial text
scroll.config(command=outputBox.yview)
outputBox.grid(row=6,column=0,columnspan=2,sticky="news")

#add weights
window.grid_columnconfigure(1, weight=3) 
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(6, weight=10)
window.mainloop()
