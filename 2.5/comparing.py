"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
"""
Create a program that uses comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You may use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

import random
import time

# Initialize responses.csv
file = open("2.4/responses.csv")
file.readline()

# adds all responses.csv file data to list
fatData = []
for line in file:
    fatData.append(line.split(","))

print("Hi. I am your personal social interaction planner!")

# makes it easier to repeat string lowering and stripping
def stringClean(string):
    return str(string).lower().strip("!?., ")

# returns the list index depending on the name input
def getUserLine(name):
    # splits name into parts to check only first or last name
    subName = str(name).split()

    # checks for every item in subName if it is in fatData
    for userLines in range(len(fatData)):
        for part in subName:
            if stringClean(part) in stringClean(fatData[userLines][1]):
                return userLines
    return -1

personInput = ""

# checks if entered name is a valid name
def checkUsername():
    while True:
        user = input("Enter a valid name: ")
        # splits name for single name validation
        subName = user.split()
        # gets line number in fatData of the chosen person to improve readability
        userLine = getUserLine(user)

        # follows up on no name found, restarts input cycle
        if userLine == -1:
            print("Name not found. Please enter a valid name.")
            continue

        # checks in fatData if any part of the name matches
        found = False
        for part in subName:
            if stringClean(part) in stringClean(fatData[userLine][1]):
                found = True
                break
        
        # outside main for loop in order to break out of while loop
        if found:
            print("Name found!")
            global personInput
            personInput = fatData[userLine][1]
            break
        else:
            # prints error message
            print("Name not found. Please enter a valid name.")

checkUsername()
# user variable is used as record user's name for later use; personInput unusable as changed with every checkUsername() call
user = personInput

# pause to read message
time.sleep(1)

# initalizes similarPeople list
similarPeople = []

# looks through fatData for similarities between each line and user
for person in range(len(fatData)):
    # prevents self comparison
    if person == getUserLine(user):
        continue

    similar = 0

    # checks if similar
    for item in range(len(fatData[person])):
        if fatData[person][item] == fatData[getUserLine(user)][item]:
            similar += 1

    # if no similarities, skips iteration
    if similar == 0:
        continue
    else:
        similarPeople.append(fatData[person][1])

    print(f"You have {similar} similarities with {fatData[person][1]}")

    # pauses to mimic slower computation, more human
    time.sleep(0.25)

# Follow up recommendation question
# personInput = input("Choose a person for a social interaction reccomendation from the similar people above").strip("!?,. ")
print("Choose a person for a social interaction reccomendation from the similar people above")

# reuses login code but to make sure selected similar person exists
checkUsername()

# checking with 
while True:
    if personInput in similarPeople:
        # selected person's similarities
        selectedPerson = []

        # adds user's similarities with selected person to selectedPerson list
        for item in range(len(fatData[getUserLine(personInput)])):
            if fatData[getUserLine(personInput)][item] == fatData[getUserLine(user)][item]:
                selectedPerson.append(fatData[getUserLine(personInput)][item])

        # chooses random activity to do from simliarities
        activity = random.choice(selectedPerson)

        # prints recommendation
        print(f"I recommend trying {activity} with {personInput}")
        print("Have fun with your new found social interaction!")
        break
    else:
        # if no similarities, asks to pick another person (not a good fit)
        print(f"No data found on {personInput}. Please enter another name")

''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Test Cases ~~~~~~~~~~~~~~~~~~~~~~~~~~
Case 1:
    User Input: "brendan" or "BRENDAN" or "yap" or "YAP" or "brendan yap" or "BRENDAN YAP" (*any name spelling correctly)
    Returns:
        Name found!
        You have 1 similarities with Ethan Wong
        You have 1 similarities with Leland Lei
        You have 3 similarities with Derick Su
        You have 2 similarities with Jayden Wong
        You have 4 similarities with Mason Lui
        You have 3 similarities with Gabe Armour
        You have 2 similarities with Evan Chan
        You have 2 similarities with Steven Zhang
        You have 2 similarities with Tejas Verma
        You have 2 similarities with Salomi Aiyathurai
        You have 2 similarities with Jeremy Wong
        You have 1 similarities with Aaryan Gogna
        You have 1 similarities with Karson Lum
        You have 2 similarities with Jacob Joe
        You have 1 similarities with Barak Sun
        You have 2 similarities with Nguyen Doan
        You have 5 similarities with Serene Lee
        You have 4 similarities with Greysen Li
        You have 3 similarities with Bella Gu
        You have 3 similarities with Daichi Lee
        You have 2 similarities with Theo Shim
        You have 1 similarities with Alessandra Ysabelle Guzman
    
    User Input: e.g. "nguyen" or "NGUYEN" or "doan" or "DOAN" or "nguyen doan" or "NGUYEN DOAN" (*any name spelling correctly)
    Returns:
        Name found!
        I recommend trying Badminton with Nguyen Doan
        Have fun with your new found social interaction!

        or

        Name found!
        I recommend trying Science with Nguyen Doan
        Have fun with your new found social interaction!

Case 2:
    User Input: "brneden" (any mispelled names)
    Returns:
        Name not found. Please enter a valid name.
        Enter a valid name:

    *will loop until given properly spelled name
    *same with second input
'''