# binary = input("Enter the binary word: ")[::-1]
# num = 0

# for digits in range(len(binary)):
#     if int(binary[digits]) == 1:
#         num += 2**digits

# print(num)

binary = input("Enter the binary sentence: ")[::-1].split(" ")
sentence = ""

for digits in range(len(binary)):
    num = 0
    for digit in range(len(binary[digits])):
        if int(binary[digits][digit]) == 1:
            num += 2**digits
            sentence += str(num) + " "

print(sentence)