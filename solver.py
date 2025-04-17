import json
def loadData():
  global contains, excludes, found, wordlist, amount
  with open("data.json") as JSONFile:
    JSONData = json.load(JSONFile)
    contains = JSONData["contains"]
    excludes = JSONData["excludes"]
    found = JSONData["found"]
    amount = JSONData["amount"]
  with open("words.txt","r") as file:
    wordlist = file.read().split("\n")
  with open("valid.txt","w") as file:
    file.write("Valid Words\n")
def hasLetter(word):#checks if it has letter in word but not in that spot
  for item in contains:
    if word[item["location"]-1] == item["letter"]:
      return False
    if item["letter"] not in word:
      return False
  return True
def hasntLetter(word):#checks if it doesn't have letter in word
  return all(item not in word for item in excludes)
def hasInSpots(word):#checks if it has letter in correct spot
  return all(word[item["spot"]-1] == item["letter"] for item in found)
def letterAmount(word):
  return all(word.count(item["letter"]) == item["amount"] for item in amount)
  
def checkWord(word):#check if word is valid
  return word in wordlist and hasntLetter(word) and hasLetter(word) and hasInSpots(word) and letterAmount(word) 
def findWords():#find all valid words
  loadData()
  acceptedList = []
  for word in wordlist:
    if checkWord(word):
      acceptedList.append(word)
  return bestWords(acceptedList) 
def display(validWords):
  with open("valid.txt","w") as file:
    title = f"{str(len(validWords))} Valid Words Found\nBest Word:{chooseWord(validWords)}\n"
    file.write(title)
  
  with open("valid.txt", "a") as file:
    track = 0
    for word in validWords:
      track += 1
      if((track % 10) == 0):
        file.write(f"{str(track)}. {word}({validWords[word]})\n")
      else:
        file.write(f"{str(track)}. {word}({validWords[word]}) ")
      
  with open("valid.txt","r") as file:
    return file.read()
def bestWords(validWords):
  scores = {}
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  #reset scoreIndex
  scoreIndex = [[0 for _ in range(26)] for _ in range(5)]
  #configure score index
  for word in range(len(validWords)):
    for char in range(len(validWords[word])):
      scoreIndex[char][alphabet.index(validWords[word][char])] += 1
  #score every word
  for word in range(len(validWords)):
    score = 0
    for char in range(len(validWords[word])):
      score += scoreIndex[char][alphabet.index(validWords[word][char])]
    scores[validWords[word]] = score
  #order words by score
  sortedWords = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
  return sortedWords
def chooseWord(validWords):
  return max(validWords, key=validWords.get)
      