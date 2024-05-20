###############################
# CodeX Learn python          #
# Lesson 5                    #
# Writing to files            #
# 20/5/2024                   #
###############################
import datetime

# Debug Mode - set to True to print debug messages
debug_mode = False
filename = "file2.txt"

  
# Print the menu
# @returns choice of values
def print_menu():
  print("\nMenu:")
  print("*****")
  print("1. Add a new diary entry ")
  print("2. View existing diary entry")
  print("3. Quit")
  choice = input("Enter your choice: ")
  return choice

# Reading from a file
'''
try:
  with open(filename, "r") as file:
    data = file.readlines()
    for line in data:
      print(line.strip())

except FileNotFoundError:
  print (f"The file called {filename} does not exist")
  
'''
# Writing to a file
try:
  with open(filename, "w") as file:
    file.write("Hello this is a sentence!\n")

except FileNotFoundError:
  print (f"The file called {filename} does not exist")
  
# Appending to a file
try:
  with open(filename, "a") as file:
    file.write("Hello this is another sentence!\n")

except FileNotFoundError:
  print (f"The file called {filename} does not exist")
  
 
# Appending to a file
date = datetime.date.today().strftime("%d-%m-%y")
print(date)

try:
  with open(filename, "a") as file:
    file.write("Hello this is another sentence!\n")

except FileNotFoundError:
  print (f"The file called {filename} does not exist")
  
    
  
  
  
  