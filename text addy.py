import sys
# import random

doors1 = int(input("Which door will you take, 1 or 2? "))
if doors1 == 1:
    print("I lost the game ;)")
    sys.exit()
elif doors1 == 2:
    print("correct")
    doors2 = int(input("sugoma? 1 or 2? "))
    if doors2 == 1:
        print("You have died of dysentery.")
        sys.exit()
    elif doors2 == 2:
        print("u won lmao")
        sys.exit()
