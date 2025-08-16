def greet():
    print("Hello there!\nI see we're here to try out our luck😏\nI'm thinking of a number between 1 and 100 (inclusive).\nGuess the number!\n")

def difficulty():
    print("Enter your diffculty:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")

    n=int(input("Enter your choice: "))
    print()
    if(n==1):
        print("Okay! Let's go newbie with the Easy option")
        print("Let's Start the game!\n")
        return 10
    elif(n==2):
        print("Okay! I see we have leveled up and choose Medium option")
        print("Let's Start the game!\n")
        return 5
    elif(n==3):
        print("Damn! I'm impressed that you choose Hard option. All the best!")
        print("Let's Start the game!\n")
        return 3
    else:
        print("\nCouldn't have been more clear🙂\nTry Again!")
        difficulty()


def game(n):
    import random as r
    random_number = r.randint(1,100)
    guess=0
    for x in range(n):
        test=True
        
        while(test):
            try:
                guess= int(input("Enter your guess: "))
                test=False
            except:
                print("Looks like your entered something else!\nTry again!")


        if(guess!=random_number):
            print(f"Incorrect! The number is {f"lesser than {guess}\n" if random_number<guess else f"greater than {guess}.\n"}")

        else:
            print(f"Congratulations! You guessed the correct number in {x+1} attempts.")
            break

    else:
        print(f"Well tried... Not!\nThe answer was {random_number}.\nHAHAHAHAHAH")


greet()
n=difficulty()
game(n)























