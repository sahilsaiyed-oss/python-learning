computer = -1
yourstr = input("Enter your choice (s/w/g): ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1:"snake", -1:"water", 0: "gun"}

you = youDict[yourstr]

print(f"You chose {reverseDict[you]} Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw")
else:
    if computer == -1 and you == 1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You Lose!")

    elif computer == 1 and you == -1:
        print("You Lose!")
    elif computer == 1 and you == 0:
        print("You Win!")

    elif computer == 0 and you == -1:
        print("You Win!")
    elif computer == 0 and you == 1:
        print("You Lose!")
