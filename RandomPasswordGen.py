#Pluggin Random
import random

numbers = "0123456789"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNopqrstuvwxyz"
characters = "!@#$%^&*()-_+"

All = numbers + lower + upper + characters

length = int(input("Select password length: "))

Password = "".join(random.sample(All, length))
print(Password)
