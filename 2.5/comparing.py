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
# find if like watching same sport as playing (not necessary)


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


numberSimilarities = []
nameSimilarities = []

for person in range(len(fatData)):
    for i in range(len(fatData[person])):
        if fatData[userLine][i] == fatData[person][i]:
            numberSimilarities.append(person)
            nameSimilarities.append(fatData[person][i])

print(numberSimilarities)
print(nameSimilarities)

# # i = int(len(similarities)/2)

# # print(getUser("Brendan Yap"))

# for each in range(int(len(similarities)/2)):
#     similarPerson = fatData[int(similarities[each])][1]
#     print(similarPerson)
#     getUser(0)
#     # if this plus this divided by index then from same person
#     # print(f"You and {} both like {}, {}, {}, {}, {}, {}, {}, {}")

#get item num of fatdata sub list that corresponds to value in similarities
def getItemNum(value):
    user = 0
    i = 0
    x = 0
    while user == 0:
        # check for user, get user line num
        for lines in fatData:
            x += 1
            for items in lines:
                i += 1
                if value == items:
                    return i-(x*10)
    return 0

# for each in range(int(len(numberSimilarities))):
#     # if each > 0 and each % 2 == 0:
#     #     eachIndex = each
#     # elif each > 0 and each % 2 == 0:
#     #     eachIndex = each-1
#     # else:
#     #     eachIndex = 0
    
#     similarPerson = fatData[numberSimilarities[each]][getItemNum(nameSimilarities[each])]
#     similar = 0
#     for i in range(len(numberSimilarities)):
#         if nameSimilarities[i] in fatData[userLine]:
#                 similar += 1
#     print(f"You have {similar} similarities with {similarPerson}")

# remove similaritie with themselves
num = len(numberSimilarities)-(len(numberSimilarities)-10)
for each in range(num):
    del numberSimilarities[len(numberSimilarities)-1]
    del nameSimilarities[len(nameSimilarities)-1]

print(numberSimilarities)

numOfSimilarAccumalative = 0
for each in range(len(numberSimilarities)):
    #get num of similar
    similar = 0

    # while n
    #     for items in range(len(numberSimilarities)):
    #         numOfSimilarAccumalative += numberSimilarities.count(items)
    


    # get 1st count, go the place in list curretnt+1st count, repeat

    for items in numberSimilarities:
        #count numbers on current index == items
        if numberSimilarities.count(numberSimilarities[numOfSimilarAccumalative]) == items:
            numOfSimilarAccumalative += 1
            similar += 1
    
    # get similar person
    similarPerson = nameSimilarities[numOfSimilarAccumalative]

    print(f"You have {similar} similarities with {similarPerson}")