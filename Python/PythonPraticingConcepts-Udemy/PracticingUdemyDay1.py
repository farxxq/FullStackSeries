# # 1. Questions (if-else based)
# # Based on a user's order,work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
# # Small pizza (s): 150
# # Medium pizza (m): 200
# # Large pizza (l): 250
# # Add Pepporoni for small pizza (Y or N): + 20
# # Add Pepporoni for medium pizza (Y or N): + 30
# # Add extra cheese for any size pizza (Y or N): + 1

# print("Welcome to Python Pizza Delivery service")
# size = input("What size of pizza do you want? \nS, M or L:")
# pepperoni = input("Do you want pepperoni? \nY or N:")
# extra_cheese = input("Do you want extra Cheese? \nY or N:")
# bill = 0

# if (size == "S" or size == "s"):
#     bill += 150
#     if(pepperoni == "Y" or pepperoni == "y"):
#         bill += 20
#     if(extra_cheese == "Y" or extra_cheese == "y"):
#         bill += 10
#     print(f"Your bill : {bill},\nThanks for coming")
# elif (size == "M" or size == "m"):
#     bill += 200
#     if(pepperoni == "Y" or pepperoni == "y"):
#         bill += 30
#     if(extra_cheese == "Y" or extra_cheese == "y"):
#         bill += 10
#     print(f"Your bill : {bill},\nThanks for coming")
# elif (size == "L" or size == "l"):
#     bill += 250
#     if(pepperoni == "Y" or pepperoni == "y"):
#         print("Sorry, Pepperoni for large size pizza not provided")
#     if(extra_cheese == "Y" or extra_cheese == "y"):
#         bill += 10
#     print(f"Your bill : {bill},\nThanks for coming")
# else:
#     print("Enter a valid size")

# 2. Question ('random' module)
# Head or tails game (Coin toss)
import random

choice = input("Enter your choice Heads (H) or Tails (T):")
randomToss = random.randint(0, 1)
H = 0
T = 1
if randomToss == H:
    print("Toss: Heads Won")
else:
    print("Toss: Tails Won")