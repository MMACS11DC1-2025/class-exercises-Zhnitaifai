"""
Create a program that uses comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You may use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
# get people wtih same sports
# enter name
# ask category the is similar

file = open("2.4/responses.csv")
file.readline()

fatData = []

for line in file:
    fatData.append(line.split(","))

data = []
data.append(fatData[0].split(","))
# fatData = file.read().strip(",")
print( )

for i in range(int(len(fatData)/10)):
    if fatData[i-(i*10)+6] == fatData[i-(i*10)+7]:
        print(fatData[i-(i*10)])

print(len(fatData)/10)
# for i in range(len(fatData)):
#     for each in fatData:
#         if i > 10:
#             if (i-(i*10)) % 6 == 0:

#         else:
#             dfddfdf