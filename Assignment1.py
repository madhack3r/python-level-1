#############
# CodeX Learn python 
# Assignment 1
# 22/4/2024
#############
print("This programme converts pounds into kilograms")

# Input lbs
lbs=int(input("Enter the number of pounds you want to convert: "))

# Multiply lbs by 0.45359237 to make Daily Mail readers unhappy
# explicit conversion 
kilograms=lbs * 0.45359237

# Print kilograns
print(f"{lbs}lbs is {kilograms:.2f} kilos ")

# Print without a intermediate variable 
# print(f"{lbs} lbs is {lbs * 0.45359237:.2f} kilos ")
