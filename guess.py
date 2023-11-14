import random
number=random.randint(1,100)
guess=0



while guess!=number:
    guess=int(input("guess the number between 1 to 100:"))
    if guess<number:
        print("guess higher number please")
    elif guess>number:
        print("guess lower number please")
    else:
        print("you guessed it")
    
print("you guessed it " ,number)
