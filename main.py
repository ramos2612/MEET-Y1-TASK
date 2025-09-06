import random
import simple
import advanced


bot = input("What kind of bot do you want? 1) Simple, or 2) Advanced? ")
if bot == "1":
    simple.simple()
elif bot == "2":
    advanced.advanced()
