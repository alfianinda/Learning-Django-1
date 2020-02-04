# python pythonrefresh.py (variable and if statements)

### variable 

# age = 17
# name = "Inna"

# print(age)
# print("Hello my name is {}. I am {} years old from Mars".format(name, age))

### exercise 
# I have given you two variables, name and age. Use the format() function to create a sentence that reads:
# Hi my name is Julie and I am 42 years old
# Set that equal to the variable called sentence

# name = "Julie"
# age = 42
# sentence = "Hi my name is {} and I am {} years old".format(name, age)
# print(sentence)

### if statements and comments 
age = 12 
name = "Matt"

todayIsCold = True

# if age > 18: 
#     print("You are older than 18")
#     print("This is another line")
# else:
#     print("You are younger than 18")

# if todayIsCold: 
#     print("Today is cold")
# else:
#     print("Today is hot")

# if name == "Matt": 
#     print("My name is Matt")
# else:
#     print("My name is Inna")

# single comment
""" multiple rows 
of comment """

### exercise
# Make an if-else statement where if year is between 2000 and 2100 (including both numbers), then print out:
# Welcome to the 21st century!
# Else print out:
# You are before or after the 21st century

year = 2050 

# if 2100 >= year >= 2000 :
#     print("Welcome to the 21st century")
# else:
#     print("You are before or after the 21st century")

if year >= 2000 and year <= 2100:
    print("Welcome to the 21st century")
else:
    print("You are before or after the 21st century")