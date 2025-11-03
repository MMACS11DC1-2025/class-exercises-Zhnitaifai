import random
def generator():
    num = int(input("Enter a num: "))
    if num == random.randint(1, 2):
        print("That's correct")
        print(f"You took {guesses} guesses")
        return True
    else:
        print("That's wrong")
        generator()
generator()