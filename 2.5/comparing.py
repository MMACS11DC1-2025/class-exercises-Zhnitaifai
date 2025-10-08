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

# test your own similarities
# give suggestion from fav fast food (including people to go with and dish)
# find personal suggestions for specific person

# init stuf
file = open("2.4/responses.csv")
file.readline()
fatData = []
for line in file:
    fatData.append(line.split(","))

userLine = 0

while userLine == 0:
    user = input("Enter your full name: ")
    # check for user, get user line num
    for lines in range(len(fatData)):
        if fatData[lines][1] == user.strip():
            userLine = lines


# similarThingsNameIndex = []
# similarThings = []

# for person in range(len(fatData)):
#     for i in range(len(fatData[person])):
#         if fatData[userLine][i] == fatData[person][i]:
#             similarThingsNameIndex.append(person)
#             similarThings.append(fatData[person][i])

# print(similarThingsNameIndex)
# print(similarThings)

# num = len(similarThingsNameIndex)-(len(similarThingsNameIndex)-10)
# for each in range(num):
#     del similarThingsNameIndex[len(similarThingsNameIndex)-1]
#     del similarThings[len(similarThings)-1]

# print(similarThingsNameIndex)

# numOfSimilarAccumalative = 0
# for each in range(len(similarThingsNameIndex)):
#     repeats = {}

#     for i in similarThings:
#         if i in repeats:
#             repeats[i] += 1
#         else:
#             repeats[i] = 1
    
#     # get similar person
#     similarPerson = fatData[similarThingsNameIndex[int(each)]][1]
#     print(f"You have {repeats[int(each)]} similarities with {similarPerson}")

similaritiesSentences = []
similarPeople = []

for person in range(len(fatData)):
    if person == userLine:
        continue

    similar = 0

    for item in range(len(fatData[person])):
        if fatData[person][item] == fatData[userLine][item]:
            similar += 1

    if similar == 0:
        continue
    else:
        similarPeople.append(fatData[person][1])

    print(f"You have {similar} similarities with {fatData[person][1]}")

#recommended activity part
"""
    - get name to be recommendec w/ from list of similar
"""

# personInput = input("Choose a person for a social interaction reccomendation from the similar people above: ").lower().strip("!?,. ")

# if personInput in 