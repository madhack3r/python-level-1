###############################
# CodeX Learn python          #
# Assignment 3                #
# Tuples and Lists            #
# 08/5/2024                   #
###############################

# Debug Mode - set to True to print debug messages
debug_mode = False


print("Welcome to the Simple To Do List!\n")

# taskList
taskList = []

while True:

  
  request=input("Please enter \n'a' to add a task, \n'v' to  view tasks, \n'r' to remove a task, \n'c' to mark a task as complete, \n'q' to quit !\n")

  if request == 'a':

    if (debug_mode):
      print(f"a")
  
    task=input("Please enter enter a task")
    taskList.append({"task": task, "complete": False})

    print(*taskList)
    
  elif request == 'v':
    
    if (debug_mode):
      print("v")
    
    if taskList:
      for i in range(len(taskList)):
        print(i)
        print(f"{i + 1}. [{ 'x' if taskList[i]['complete'] else ' ' }] {taskList[i]['task']}")
    else:
      print("No tasks in the list")
      
  elif request == 'r':
    # Remove a task
    if (debug_mode):
      print("r")
    
    if taskList:
      print("1")
      index=int(input("Please enter enter the number of the task"))-1
      if 0<=index<=len(taskList):
        del taskList[idex]
        print("Item Removed")
      else:
        print("Invalid Task")
    else:
      print("No tasks in list")  

  elif request == 'c':
    if (debug_mode):
      print("c")
      
    if taskList:
      index = int(input("Enter the index you want to mark as complete"))-1
      if 0<=index<=len(taskList):
        taskList[index]['complete'] = True
        print("Marked as complete")
      else:
        print("Invalid Task Name")
      
  elif request == 'q':
    if (debug_mode):
      print("q")
    
    print("Quitting")
    break
  else:
      print("Invalid Input - Try again")

    