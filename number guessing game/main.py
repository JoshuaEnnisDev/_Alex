import random


# get a random number
number = random.randint(0, 100)

# debug statement
print(number)

# get the user's guess
guess = int(input("Guess a number between 0 and 100: "))

while (guess != number):
    # if they are too high, tell them they are too high
    if guess > number:
        print("Too high!")
    # if lower, print "too low"
    elif guess < number:
        print("too low!")
    
    guess = int(input("Guess a number between 0 and 100: "))

# if they get right, tell them they win!
print("Good job! You got it!")

    # difference between a string and an integer
