import random
random_number = random.randrange(1, 10)
guess_number = None
status = None
while status != "exit":
    random_number = random.randrange(1, 10)
    while guess_number != random_number:
        guess_number = int(input("Guess the number from 1 - 9: "))
        if guess_number > random_number:
            print("Too high.")
        elif guess_number < random_number:
            print("Too low.")
        else:
            print(f"Exactly! {random_number}")
    status = input('Type ["exit" to quit] or ["continue" to play again]: ')
