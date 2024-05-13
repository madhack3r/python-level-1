###############################
# CodeX Learn python          #
# Assignment 4                #
# Dictionaires - Voting Dict  #
# 13/5/2024                   #
###############################
import hashlib

# Debug Mode - set to True to print debug messages
debug_mode = False

# Structure that holds candidate data and the number of votes that they have
candidates = {}

# Dictionary that holds voter register
voter_register = {}


# Keep the voter name secure
# @returns a hashed vote value
def hash_voter(voter_name):
  hashed_voter_name = hashlib.sha256(voter_name.encode()).hexdigest()
  return hashed_voter_name
  
# Print the menu
# @returns choice of values
def print_menu():
  print("\nMenu:\n")
  print("1. Vote for a candidate")
  print("2. View voting results")
  print("3. Quit")
  choice = input("Enter your choice: ")
  return choice

# Set up the list of candidates
def setup_candidates():
  candidates["Don"] = 0
  candidates["Hallie"] = 0
  candidates["Joe"] = 0
  candidates["Vivek"] = 0
  candidates["Vlad"] = 0

# Print the list of candidates
def print_candidates():
  for n,v in candidates.items():
    print(f"candidate {n} has {v}")
    
# Print the list of candidates to chose from
def print_candidate_choices():
  for n,v in candidates.items():
    print(f"You can vote for candidate {n}")

# Check if the voter has voted before
# by checking the list
def has_voted_before(encypted_voter):
  if encypted_voter in voter_register.keys():
    return True
  else:
    return False
  

# Start of Programme
print("Welcome to the Secure Voting System!")

# Set up the candidate list
setup_candidates()

# Ask user whether they want to continue
while True:

  # Print the menu items
  choice = print_menu()

  if(choice == "1"):
    # Get the name of the candidate that you want to vote for
    candidate = input("Please enter the name of the candidate you want to vote for :")
    # Get the name from the voter register
    name = input("Please now enter your name:")
    # Hash the name for the dominion systems    
    hashed_voter = hash_voter(name)

    # Check if we have a valid candidate
    if candidate in candidates:  
      if has_voted_before(hashed_voter) == True:
        print("It is illegal to vote more than once")
      else:
        # Add name to the voter register and an arbitary value pair
        # into the voter register - remember to bring your ID
        voter_register[hashed_voter] = "True"
        # Increment value of candidate in the candiate dictionary
        candidates[candidate] += 1
    else:
      print("Candidate does not exist")
  elif(choice == "2"):
      print_candidates()
  elif(choice == "3"):
    print("Goodbye!")
    break
  else:
    print("Invalid option. Try again")
  
  