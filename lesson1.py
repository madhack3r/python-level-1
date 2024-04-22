#############
# CodeX Learn python 
# Lesson 1
# 22/4/2024
#############
print("This programme is a simple calcualtor that can multiply two numbers together!")

# Input first number
first_num=int(input("Enter your first number: "))

# input second number
second_num=int(input("Enter your second number: "))

# Multiply the values 
result=int(first_num)*int(second_num)

# Print Result
print(str(first_num) + " multiplied by " + str(second_num) + " = " + str(result) )

# Print using fstring
print(f"{first_num} multiplied by {second_num} = {first_num*second_num}")