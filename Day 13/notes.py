############DEBUGGING#####################

# # STEP 1: Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# what is for loop doing? -> loop from i = 1 to ...
# when function prints "You got it"? -> when i reaches 20
# what are assumptions about i? -> i reaches 20 -> THIS IS FALSE

# # STEP 2: Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])

# # STEP 3: Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   # 1981.....1993
#   print("You are a millenial.")
# elif year >= 1994:
#   # 1995.....
#   # from above two 1994 is missing in conditions
#   print("You are a Gen Z.")

# # STEP 4: Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#   print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger - Python tutor, breakpoints
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

#mutate([1,2,3,5,8,13])

# Run often