file = open("2.4/responses.csv")

DATA = file.read().split(",")

for line in DATA:
    if "brendan yap" in line.lower():
        print(line)
        break
