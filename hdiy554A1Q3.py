"""
Name: Hivin Diyagama
Username: hdiy554
ID: 365061211

Change making problem
"""



import math


prompt = "Value:"
value = int(input(prompt))

calculation_100 = value // 100
remaining1 = value - calculation_100 * 100
calculation_50 = remaining1 // 50
remaining2 = remaining1 - calculation_50 * 50
calculation_25 = remaining2 // 25
remaining3 = remaining2 - calculation_25 * 25
calculation_10 = remaining3 // 10
remaining4 = remaining3 - calculation_10 * 10
calculation_5 = remaining4 // 5
remaining5 = remaining4 - calculation_5 * 5
calculation_1 = remaining5 // 1
 


print("You will need:")
print("===================")
print("  100s:", calculation_100)
print("  50s:", calculation_50)
print("  25s:", calculation_25)
print("  10s:", calculation_10)
print("  5s:", calculation_5)
print("  1s:", calculation_1)
print("===================")
