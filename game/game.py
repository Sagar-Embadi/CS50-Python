# import the random module
import random
# get the level input from user
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

# set the random level
random_number = random.randint(1, level)

# get the guess input from user
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess<random_number:
                print("Too small!")
            elif guess>random_number:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass
