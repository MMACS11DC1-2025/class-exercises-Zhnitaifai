file = open("2.4/responses.csv")
junk = file.readline()
datalist = []
for i in range(2):
    datalist.append(file.readline().split(","))
print(datalist)