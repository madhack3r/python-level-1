###############################
# CodeX Learn python          #
# Assignment 2                #
# 29/4/2024                   #
###############################

# Debug Mode - set to True to print debug messages
debug_mode = False


print("Welcome to the Prime Evaluator!\n")

while True:
  # Define a prime indicator and set to false by default
  isPrime = True
  
  try:
    number=int(input("Please enter an integer number to test for primeness (enter \"Stop\" to end) !\n"))

    # If the number is 1 then it is not a prime - outlier case
    if number == 1:
      if (debug_mode):
        print(f"Outlier 1")
      isPrime = False
    elif number > 1:
      # Prime check - loop through all divisors from 2 to number
      for i in range(2, number):
      # Debug
        if (debug_mode):
          print(f"Value of i is : {i} \n")

          # Divide by i and if the remainder is 0 
          # then it is not a prime as it can be divided by 
          # a number apart from 1 and itself
        if (number % i) == 0:
          print(f"Value of i is : {i} \n")
          isPrime = False
          # ********** Debug ***********
          if (debug_mode):
            print(f"number % i is {number % i} \n")
              
          # If factor is found, set flag to True and break out of loop
          break
        
    if (debug_mode):
      print(f"isPrime is {isPrime} \n")
    # Check if flag is True
    if (isPrime):
      print(f"{number} is a prime number\n")
    else:
      print(f"{number} is not a prime number\n")
  except:
    # 
    print("OK, you are bored and not entered an integer, let's end this")
    break
    
    