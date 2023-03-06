name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")
answer = input("You are on a dirt road, it has come to an end and you can fo left or right. Which way would you want to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swin to swim accross. [walk/swim] ").lower()

    if answer == "swim":
        print("You swam accross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lose the game.")
    else:
        print("Not a valid option. you lose!")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobly, do you want to cross it or head back? [cross/back] ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk with him or no? [yes/no] ").lower()

        if answer == "yes":
            print("You talk with a strange, hi give you money. You WIN!")
        elif answer == "no":
            print("You ignor ethe stranger and they are offender and you lose!")
        else:
            print("Not a valid option. you lose!")  
    else:
        print("Not a valid option. you lose!")  
else:
    print("Not a valid option. you lose!")