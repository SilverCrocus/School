"""
Name: Hivin Diyagama
Username: hdiy554
ID: 365061211

Password Generator following the layout 4 letters then 4 numbers
"""




import random

banner = "*" * 20

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alphabet_random1 = len(alphabet)
alphabet_pos = random.randrange(0,len(alphabet))
random_letter1 = alphabet[alphabet_pos]
alphabet_pos2 = random.randrange(0,len(alphabet))
random_letter2 = alphabet[alphabet_pos2]
alphabet_pos3 = random.randrange(0,len(alphabet))
random_letter3 = alphabet[alphabet_pos3]
alphabet_pos4 = random.randrange(0,len(alphabet))
random_letter4 = alphabet[alphabet_pos4]
random_number = random.randrange(1,1000)


length_of_number = len(str(random_number))
zero = (4 - length_of_number) * str("0")


print(banner)
print("*Password Generator*")
print(banner)
print()
print("Your password is ", random_letter1, random_letter2, random_letter3, random_letter4, zero, random_number, sep="")
