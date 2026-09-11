import random

score = 0
streak = 0

while True:
    coin = random.choice(["heads", "tails"])

    while True:
        guess = input("Heads or Tails? ")
        guess = guess.lower()

        if guess == "heads" or guess == "tails":
            break
        else:
            print("That's not a valid guess, try again.")

    if guess == coin:
        streak += 1
        points = 1

        if streak >= 5:
            points = points * 2
            print("You're on a streak! Points have doubled.")

        score += points
        print(f"Correct, it was {coin}! You got {points} point(s).")

    else:
        streak = 0
        print(f"Nope, it was {coin}. Streak has been reset.")

    print(f"Score: {score}  Streak: {streak}")
    print("-" * 20)