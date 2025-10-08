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
    userLn = 0

    # checks each line in fatData to see if name matchs with data in FatData
    while userLn == 0:
        for lines in range(len(fatData)):
            if stringClean(fatData[lines][1]) == stringClean(name):
                userLn = lines
    return userLn

# checks if entered name is a valid name
index = 0
while True:
    user = input("Enter a valid name: ")

    # splits name for single name validation
    subName = user.split()

    # checks in fatData for single name
    if subName[index] in fatData[getUserLine(user)][1]:
        print("Name has been scanned and validated")
        break
    
    # prints error message
    print("Name not found. Please enter a valid name.")
    index += 1

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

# follow up question
personInput = input("Choose a person for a social interaction reccomendation from the similar people above: ").strip("!?,. ")

# checking with 
if personInput in similarPeople:

    selectedPerson = []

    for item in range(len(fatData[getUserLine(personInput)])):
        if fatData[getUserLine(personInput)][item] == fatData[getUserLine(user)][item]:
            selectedPerson.append(fatData[getUserLine(personInput)][item])

    print(selectedPerson)

    activity = random.choice(selectedPerson)
    print(f"I reccomend trying {activity} with {personInput}")