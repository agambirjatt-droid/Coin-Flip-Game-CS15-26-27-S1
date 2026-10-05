import random

while True:
    coin = random.choice(["heads", "tails"])

    while True:
        guess = input("What is your guess? (Heads/Tails)\n")
        guess = guess.lower()

        if guess == "heads" or guess == "tails":
            break
        else:
            print("Invalid input.")

    if guess == coin:
        print("Correct bro! The coin was", coin.capitalize())
    else:
        print("Incorrect bro. The coin was", coin.capitalize())
