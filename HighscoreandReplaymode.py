import random
high_score = None
while True:
    print("Choose a difficulty level: easy, medium, or hard")
    difficulty = input("Enter difficulty:").lower()
    if difficulty == "easy":
        max_number = 10
    elif difficulty == "medium":
        max_number = 50
    elif difficulty == "hard":
        max_number = 100
    else:
        print("Invalid choice, defaulting to easy.")
        max_number = 10
    secret_number = random.randint(1, max_number)
    guess = int(input(f"Guess the number (between 1 and {max_number}):"))
    tries = 1
    while guess != secret_number:
        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high.")
        guess = int(input("Try again: "))
        tries += 1
    print(f"You got it in {tries} tries! :D")
    if high_score is None or tries < high_score:
        high_score = tries
        print(f"NEW HIGH SCORE!")
    print(f"Current high score: {high_score} tries")
    play_again = input("Do you want to play again? (yes/no):"). lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break