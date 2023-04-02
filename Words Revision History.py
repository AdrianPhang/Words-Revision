
#Defining a Function (addWord) and Parameter (new_key and old_key)
def reviseWord (new_key ,  old_key  ):
    dictionary[new_key] = dictionary[old_key]
    del dictionary[old_key]

#Defining a Function (addWord) and Parameter (word)
def addWord ( word  ):
    dictionaries = dictionary.get( word )
    global latestWordKey
#Triggers the existing word is in the dictionary and ask if the user wants to enter a new sentence to the current word.
    if dictionaries:
        for name in  dictionary.get( word ):
            print("Existing sentences: ")
            print(name)

#Giving a choice for the user if he/she wants to enter a new sentence to the existing word.
        userInput = str(input("Enter 1 to attach a new sentence to the current word or enter any other key to head back to the menu \n:  "))
        if userInput == "1":

            newSentence = str(input("Please enter a new sentence to be attached to the word: "))
            dictionary.get( word ).append( newSentence )
            latestWordKey = str(word)
            latestWordDisplayed =  latestWordKey+str(" - ")+str(newSentence)

    if not dictionaries:
        dictionary[ word ] = []
        newSentence = str(input("Please enter a new sentence to be attached to the word: "))
        dictionary.get( word ).append( newSentence )
        latestWordKey = str(word)
        latestWordDisplayed =  latestWordKey+str(" - ")+str(newSentence)
    return latestWordDisplayed

#To prevent infinite loop from happening
inputVar =  0

#Defining a global variable called (dictionary)
dictionary = {}
latestWordDisplayed = ""
latestWordKey = "";

#Close off the program if number 3 is chosen as the choice.
while inputVar != "3":

#Integrating a Main Menu for Users to pick 3 choices 1) Add a word 2) Display a word from the current dictionary database
    category = str(input("Please enter an option \n1. Add a word \n2. Display a word from the current dictionary \n: "))

#By picking 1, The user will add a word into the Historyy.
    if category == "1":
         word_1 = str(input("Please enter the word to be added into the dictionary: "))

#Word gets added into the array of (dictionary)

         latestWordDisplayed = addWord(word_1)
         print(dictionary)


#By picking 2, The system will show the words in the dictionary.
    if category == "2":
        print("Current words in the dictionaries are: ")
        for key , value in list(dictionary.items()):
            print(key);

#From choice 2, The users will be allowed to pick from a menu for 2 more choices again. 1) Display a word based on the latest revision made or 2) Display a list to show words and the respective revision freqncy being made
        userInput = str(input("Please choose 1 of the options: \n1. Display word based on the latest revision made \n2. Display word based on revision frequency of the word \n: "))

#Choosing the word based on the latest revision made (Choice 1)

        if userInput == "1":
            print( "Most recent revised word: "+latestWordKey)
            latestNewWordKey = str(input("Please enter new word to replace "))
            reviseWord(latestNewWordKey, latestWordKey)
            print( "Most recent revised word has been changed from "+latestWordKey +" to "+latestNewWordKey)


#Choosing the word and show the number of revisions that has been made to the word (Choice 2)
        if userInput == "2":
            size = 0

#Assigning latestWordKey to be the new revised word  
            for key, value in list(dictionary.items()):
                if len(value) > size:
                    size = len(value)
                    latestWordKey = key

#Prining out the brand new revised word
            print( "Most revised word: "+latestWordKey)
            latestNewWordKey = str(input("Please enter new word to replace "))
            reviseWord(latestNewWordKey, latestWordKey)
            print( "Most revised word has been changed from "+latestWordKey +" to "+latestNewWordKey)




#Looping back the program back to the Main Menu or to end the program
    inputVar = str(input("Please enter any other keys to head back to the main menu or enter 3 to end the program: "))

#Opening and writing history.txt, If there is no history.txt seen it will be created in the folder
f = open("History.txt","w+")

#By writing the program and allocated the program to make sure the new sentence attached to the string is moved to the right side. Next word and sentence will be moved to the next line.
for key, value in list(dictionary.items()):
    f.write(str(key) +"-->")
    for array in dictionary[key]:
        f.write(str(array) + ",")
    f.write("\n")
f.close()
