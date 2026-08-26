secret = 7
attempts = 0
while True:
    guess = int(input("Enter guess: "))
    attempts += 1
    if guess == secret:
        print("Correct! Attempts:", attempts)
        break
    print("Wrong guess, try again")
