###############################
# CodeX Learn python          #
# Assignment 5                #
# Writing to files            #
# 20/5/2024                   #
###############################
import datetime

# Debug Mode - set to True to print debug messages
debug_mode = False
filename = "Error.log"


# **************************
# Print the menu
# @returns int choice of values
# **************************
def print_menu():
  print("\nMenu:")
  print("*****")
  print("1. Add a new Error Log ")
  print("2. View existing Errors ")
  print("3. Quit")
  choice = int(input("Enter your choice: "))
  return choice

# **************************
# Adds a new error log entry
# **************************
def add_entries():
  try:
    date = input("Enter the date for the error log (DD-MM-YY) or leave blank for today")
    
    if date == "":
      date = datetime.date.today().strftime("%d-%m-%y")
    
    error = input("Enter the errorlog entry")
    with open(filename, "a") as file:
      file.write(f"{date} - {error}\n")
    
  except:
    errorMsg = "In add_entries: The file called " + filename + " does not exist"
    print (f"{errorMsg}")
    
  
  print("Error entry was written")

# **************************
# Prints the error log
# **************************
def show_errorlog():
  # Reading from a file
  try:
    # Pretty print
    print("\n")
    with open(filename, "r") as file:
      data = file.readlines()
      if data:
        for line in data:
          print(line.strip())
      else:
        print("No Error Log entries")

  except FileNotFoundError:
    errorMsg = "In show_errorlog: The file called " + filename + " does not exist"
    print (f"{errorMsg}")


# **************************
# Start of Code
# Print welcome message
# **************************
print("Welcome to the Error Logger")

# Loop while true
while True:

  # Print the menu items
  choice = print_menu()
  
  if choice == 1:
    add_entries()
  elif choice == 2:
    show_errorlog()
  elif choice == 3:
    print("Quit")
    break
  else:
    print("Invalid entry")
    
  
  
