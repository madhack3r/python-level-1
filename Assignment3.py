###############################
# CodeX Learn python          #
# Assignment 3                #
# Tuples and Lists            #
# 08/5/2024                   #
###############################
import datetime

# Debug Mode - set to True to print debug messages
debug_mode = False


print("Welcome to the Financial Ledger!\n")

# Structure that holds the account details
account = []

# Loop while true
while True:

  # Print he request to add data
  request=input("Please enter \n'i' to add an income, \n'e' to add an expense, \n'v' to view a summary, \n'q' to quit !\n")

  if request == 'i':
    # Debug - inserting income
    if (debug_mode):
      print(f"i")
    
    # Add the amt to the ledger
    now = datetime.datetime.now()
    amt=float(input("Please enter an income to add to your balance: "))
    account.append({"Timestamp" : now.strftime("%x %X"), "Transaction": "Income", "amount": amt})

  elif request == 'e':
    # Debug inserting expense
    if (debug_mode):
      print("e")

    # Add the amt to the ledger
    # Multiply by -1 so that it is held as a debit
    now = datetime.datetime.now()
    amt=float(input("Please enter an income to add to your balance: "))*-1
    account.append({"Timestamp" : now.strftime("%x %X"), "Transaction": "Expense", "amount": amt})
    
  elif request == 'v':
    if (debug_mode):
      print("v")
  
    # Running account balance
    total=0
  
    # If we have transactions in the ledger
    # Then print a banner and loop through the
    # transactions
    if account:
      print("***********************************************\n")
      print("***********  Statment Balance  ****************\n")
      print("***********************************************\n\n")
      print("    Date\t\tTx Type\t\tAmount\n\n")
      for i in range(len(account)):
        print(f"{i + 1}.  {account[i]['Timestamp']}\t{account[i]['Transaction']}\t\t{account[i]['amount']:.2f}\n")
        total += account[i]['amount']
        
      print(f"\t\t\t\tTotal : {total:.2f}\n")
      print("************************************************\n")
    else:
      print("No ledger entries\n")


  # Quit the programme
  elif request == 'q':
    if (debug_mode):
      print("q")
    
    print("Quitting")
    break
  else:
    # Invalid input and loop again
    print("Invalid Input - Try again")

    