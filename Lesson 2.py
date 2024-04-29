###############################
# CodeX Learn python          #
# Lesson 2                #
# 29/4/2024                   #
###############################

print("Welcome to the Weight Converter!\n")


print("WHat do you want to convert!\n")

conversion_choice=int(input("1) lbs to Kg\n2) Kg to lbs\n\n"))

#
if  (conversion_choice==1):
  while True:
    try:
      # Input lbs
      lbs=float(input("Enter the number of lbs you want to convert: "))
      break
    except:
      print("Invalid input. Please enter a numeric value.\n")

  print(f"{lbs} lbs is equivalent to {lbs / 2.20462:.2f} kg ")

elif (conversion_choice==2):
  while True:
    try:
      # Input kgs
      kgs=float(input("Enter the number of kilograms you want to convert: "))
      break
    except:
      print("Invalid input. Please enter a numeric value.\n")

  print(f"{kgs} kgs is equivalent to {kgs * 2.20462:.2f} pounds ")
else:
      print("\nInvalid input. Please enter 1 or 2.\n")


  
