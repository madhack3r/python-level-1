###############################
# CodeX Learn python          #
# Assignment 2                #
# 29/4/2024                   #
###############################

print("Welcome to the Prime Evaluator!\n")


# Define a prime indicator and set to false by default
isTrue = False

while True:
  try:
    number=int(input("Please enter a number (enter \"Stop\" to end) !\n"))

    # If the number is 1 then it is not a prime - outlier case
    if number == 1:
        print(f"{number} is not a prime number")
    elif number > 1:
        # Prime check - loop through all divisors from 2 to number
        for i in range(2, number):
            # print(f"Value of i is : {i} \n")
            
            # Divide by integer and if the remainder is 0 
            # then it is not a prime as it can be divide by 
            # a number apart from 1 and itself
            if (number % i) == 0:
                # If factor is found, set flag to True and break out of loop
                isTrue = True
                break
        
        # Check if flag is True
        if isTrue:
            print(f"{number} is not a prime number\n")
        else:
            print(f"{number} is a prime number\n")
  except:
    print("OK, you are bored, let's end this")
    break
    
    