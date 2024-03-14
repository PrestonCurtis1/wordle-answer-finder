import json
def loadData():
  global contains, excludes, found, wordlist
  with open("data.json") as JSONFile:
    JSONData = json.load(JSONFile)
    contains = JSONData["contains"]
    excludes = JSONData["excludes"]
    found = JSONData["found"]
  with open("words.txt","r") as file:
    wordlist = file.read().split("\n")
  with open("valid.txt","w") as file:
    file.write("Valid Words\n")
def hasLetter(word):#checks if it has letter in word
  for item in contains:
    letter = item["letter"]
    locations = item["locations"]
    for location in locations:
      if word[location] == letter:
        return False
      if letter not in word:
        return False
  return True 
def hasntLetter(word):#checks if it doesn't have letter in word
  return all(item not in word for item in excludes)
def hasInSpots(word):#checks if it has letter in correct spot
  return all(word[item["spot"]] == item["letter"] for item in found)
def checkWord(word):#check if word is valid
  isWord = word in wordlist
  wordExcludes = hasntLetter(word)
  wordContains = hasLetter(word)
  wordInSpots = hasInSpots(word)
  valid = isWord and wordExcludes and wordContains and wordInSpots
  return valid
def findWords():#find all valid words
  loadData()
  acceptedList = []
  for word in wordlist:
    if checkWord(word):
      acceptedList.append(word)
  return acceptedList  
def display(validWords):
  with open("valid.txt","w") as file:
    title = str(len(validWords)) + " Valid Words Found\n"
    file.write(title)
  with open("valid.txt", "a") as file:
    count = 0
    for word in validWords:  
      count += 1
      if((count % 10) == 0):
        file.write(str(count) + ". " + word + "\n")
      else:
        file.write(str(count) + ". " + word + " ")
      
  with open("valid.txt","r") as file:
    print(file.read())




    
  
