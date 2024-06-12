###############################
# CodeX Learn python          #
# Assignment 6                #
# Writing to csv              #
# 20/5/2024                   #
###############################
import csv

# Debug Mode - set to True to print debug messages
debug_mode = True

#############################
# Display menu
#############################
def display_menu():
  print("\nDating Preference Menu")
  print("1. Add Preferences")
  print("2. Display Preferences")
  print("3. Quit")

#############################
# Add Preferences
#
# @file_path - the path to store the csv
#############################
def add_preferences(file_path, preferences):

  try:
    with open(file_path, mode='a', newline='') as file:
      writer = csv.writer(file)
    
      for preference in preferences:
        writer.writerow(preference)
    
    print("Successfully written to file")
    
  except IOerror:
    print("Error: Could not write to the file")
    
#############################
# Display csv file and 
#
#############################
def display_preferences(file_path):
  
  try:
    with open(file_path, mode='r', newline='') as file:
      reader = csv.reader(file)
      expenses = list(reader)
      if len(expenses) == 0:
        print("No preferences found")
        return
        
      for row in expenses:
        print(', '.join(row))
    
  except FileNotFoundError:
    print("Error: No preferences found")
  except IOError:
    print("Error: Could not read from the file")
  
#
#############################
# Main()
#
#
#############################
def main():
  
  # Excel Filename 
  path = "preferences.csv"

  # Print he request to add data
  print("Welcome to the User Dating Preferences Application")
  preferences = [
      ["Name", "Height Preference", "Trust Fund Preference", "Job Preference", "Eye Colour Preference"]
  ]


  # loop until break
  while True:
    display_menu()
    # Print he request to add data
    request=input("Please enter your choice 1, 2 or 3 :\n")
    
    if request == '1':
      # Print input details
      name = input("Please enter your name:")
      height = input("Please enter your height preference (e.g. 6'5):")
      trustFund = input("Please enter Trust Fund Status (Yes/No):")
      job = input("Please enter job area (e.g. Finance):")
      eyeColour = input("Please enter eye colour (e.g. Blue Eyes):")
      
      # Create a new row of data and append to record
      row = [name, height, trustFund, job, eyeColour]
      preferences.append(row)

    elif request == '2':
      add_preferences(path, preferences)
      display_preferences(path)
      
    elif request == '3':
      print("Quitting - Bye!")
      break
    else:
      print("Invalid input, try again")




    
if __name__ == "__main__":
  main()
  
  
  