import random

number = int(input(f"What number are you looking for?:"))
## Desc for number: the number the user picks.

maximum = int(input(f"What do you want the maximum amount of attempts to be?"))
## Desc for maximum: the maximum caps of turns the user picks.

def gen_random_number():
    cap = range(0, 101, 1)
    random_number = random.choice(cap)
    return random_number
## Desc for gen_random_number): a function that randomly picks out a number between 0 - 100.

turns_with_number = 0
attempts = 0

playing = True

while playing:
    result = gen_random_number()
    attempts += 1
    if result == number:
        turns_with_number += 1
    if attempts >= maximum:
        playing = False
print(f"Your number has shown {turns_with_number} times, within the interval 0 and 100, in {attempts} attempts.")




         




