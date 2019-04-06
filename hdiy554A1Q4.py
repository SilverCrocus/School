"""
Name: Hivin Diyagama
Username: hdiy554
ID: 365061211

Dice Game
"""

import random

current_score = 0
top_banner = "*" * 45
print(top_banner)
print("REACH 100 IN THREE ROUNDS!   Initial total: 0")
print(top_banner)
print()
print()

#Round 1
random_dice1 = random.randrange(1,7)
random_dice2 = random.randrange(1,7)
random_dice3 = random.randrange(1,7)
random_dice4 = random.randrange(1,7)
random_dice5 = random.randrange(1,7)
dice_numbers =str(random_dice1) + str(random_dice2) + str(random_dice3) + str(random_dice4) + str(random_dice5)



print("Round 1:")
print("Your dice:", random_dice1, random_dice2, random_dice3, random_dice4, random_dice5)

tens = input("  Tens:")
units = input("  Units:")

position1 = int(tens)
position2 = int(units)

number1 = dice_numbers[position1 - 1]
number2 = dice_numbers[position2 -1]
final_number = number1 + number2

print("Dice value:", final_number)
current_score = int(final_number) + current_score

print("Your current total:", current_score)


#Round 2
random_dice1 = random.randrange(1,7)
random_dice2 = random.randrange(1,7)
random_dice3 = random.randrange(1,7)
random_dice4 = random.randrange(1,7)
random_dice5 = random.randrange(1,7)
dice_numbers =str(random_dice1) + str(random_dice2) + str(random_dice3) + str(random_dice4) + str(random_dice5)

print()
print()
print("Round 2:")
print("Your dice:", random_dice1, random_dice2, random_dice3, random_dice4, random_dice5)

tens = input("  Tens:")
units = input("  Units:")

position1 = int(tens)
position2 = int(units)

number1 = dice_numbers[position1 - 1]
number2 = dice_numbers[position2 -1]
final_number = number1 + number2

print("Dice value:", final_number)
current_score = int(final_number) + current_score

print("Your current total:", current_score)


#Round 3
random_dice1 = random.randrange(1,7)
random_dice2 = random.randrange(1,7)
random_dice3 = random.randrange(1,7)
random_dice4 = random.randrange(1,7)
random_dice5 = random.randrange(1,7)
dice_numbers =str(random_dice1) + str(random_dice2) + str(random_dice3) + str(random_dice4) + str(random_dice5)

print()
print()
print("Round 3:")
print("Your dice:", random_dice1, random_dice2, random_dice3, random_dice4, random_dice5)

tens = input("  Tens:")
units = input("  Units:")

position1 = int(tens)
position2 = int(units)

number1 = dice_numbers[position1 - 1]
number2 = dice_numbers[position2 -1]
final_number = number1 + number2

print("Dice value:", final_number)
current_score = int(final_number) + current_score

print()
print()


#Ending result
bottom_banner = "*" * 29
print(bottom_banner)
print("Your final score:", current_score)

goal = abs(100 - current_score)

print("You are", goal, "away from the goal")
print(bottom_banner)


















