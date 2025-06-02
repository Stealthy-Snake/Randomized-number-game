import random
secret_number = random.randint(1, 10)
guess = int(input("Guess the number (between 1 and 10): "))
while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high.")
    guess = int(input("Try again: "))
print("You got it! :D")