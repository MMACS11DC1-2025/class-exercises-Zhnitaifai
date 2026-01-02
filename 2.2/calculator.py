"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, and use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
# """

# ask which operation
# get 1st value
# get 2nd value
# depending on which operation, use values to solve
# if not *, /, +, or - operator returns not a valid operator

match input("Which operator (*, /, +, or -)? "):
    case "*":
        print(int(input("Enter 1st value: ")) * int(input("Enter 2nd value: ")))
    case "/":
        print(int(input("Enter 1st value: ")) / int(input("Enter 2nd value: ")))
    case "+":
        print(int(input("Enter 1st value: ")) + int(input("Enter 2nd value: ")))
    case "-":
        print(int(input("Enter 1st value: ")) - int(input("Enter 2nd value: ")))
    case _:
        print("Not a valid operator. Try again")