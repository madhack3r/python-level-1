###############################
# CodeX Learn python          #
# Assignment 1                #
# 22/4/2024                   #
###############################

print("Welcome to the Weight Converter!\n")

while True:
  try:
    # Input lbs
    kgs=float(input("Enter the number of kilograms you want to convert: "))
    break
  except:
    print("Invalid input. Please enter a numeric value.\n")
  
# Multiply kgs by 2.20462 to make Daily Mail readers happy
print(f"{kgs} kgs is equivalent to {kgs * 2.20462:.2f} pounds ")
# 100.5 kgs is equivalent to 221.56 pounds or 221.56431 without rounding ????? 
# Example 2 states that 
# 100.5 kg is equivalent to 221.66 pounds
