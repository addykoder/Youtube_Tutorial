from random import randint
your = 0
comp = 0
for i in range(10000):
    computer = randint(0,3)
    if computer == 0:
        ch = "Stone"
    elif computer == 1:
        ch = "Paper"
    elif computer == 2:
        ch = "Scissor"


    #chance = input("Enter you chance (1-Stone, 2-Paper, 3-Scissor)  :")
    chance = "3"
    if chance  == "1":
        you = "Stone"
    elif chance == "2":
        you = "Paper"
    elif chance == "3":
        you = "Scissor"
    elif chance == "exit":
        print("Your points :",your)
        print("bots points :",comp)
        quit("bye")

        print("Computer              You")
        print(ch,"                ",you)

    chance = int(chance)
    if computer+1 == 1:
        if chance == 2:
            print("You won")
            your += 1
            continue
        elif chance == 3:
            print("You loose")
            comp+=1
            continue
    elif computer +1 == 2:
        if chance == 1:
            print("You loose")
            comp +=1
            continue
        elif chance == 3:
            print("You won")
            your+=1
            continue
    elif computer +1 == 3:
        if chance == 1:
            print("You won")
            your+=1
            continue
        elif chance == 2:
            print("You loose")
            comp+=1
            continue

    print("draw")
    print("")

print("Your points :",your)
print("bots points :",comp)
