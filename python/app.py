from tasks import todo_list
from tasks import *
from accounts import accounts
from accounts import *

if __name__ == "__main__":
    print ("Welcome to my app") 
    print ()
    print ("Please signin")
    print ()
    name = input("Enter your name:")
    password = input("Enter your password:")
    if name not in accounts or accounts[key] is not password:
      print ("You don't have an account please select 1 and signup") 
      print ()
      print ("1. signup")
      print ()
      select = (input("select: "))
      while select.isdigit(): 
        if select is 1:
          name = str(input("Enter your name:"))
          password = str(input("Enter your password"))
          add_account(name, password)
          print ()
          print ("You have successfully opened an account")
          print ()
          print ("Please navigate through and do what you ought to do by chosing.............")
          print ()
          print ("Choices")
          print ()
          print ("1. My account")
          print ("2. login")
          # print ("3. My todo_lists")
          print ()
          choice = int(input("select your choice: "))
          if choice is 2:
            login(name, password)
            while login(name, password):
              print ("\nSelect Option:")
              print ("1. Create task ")
              print ("2. delete task ")
              print ("3. delete all tasks ")
              print ("4. mark task finished\n ")
              select = int(input("selection: "))
              if select is 1:
                task = str(input("Enter task to be added"))
                create_task(task)
                continue
              elif select is 2:
                task = str(input("Enter task to be removed"))
                delete_task(task)
                continue
              elif select is 3:
                delete_all_tasks()
                continue
              elif select is 4:
                task = str(input("Enter task to be removed"))
                mark_as_finished(task)
                continue
              else:
                print ("Invalid input")
          elif choice is 1:
            print (todo_list)
          else:
            print ("Invalid input")

      else:
        print ("Invalid input")
    else:
      login(name, password)
      while login(name, password):
        print ("\nSelect Option:")
        print ("1. Create task ")
        print ("2. delete task ")
        print ("3. delete all tasks ")
        print ("4. mark task finished\n ")
        select = int(input("selection: "))
        if select is 1:
          task = str(input("Enter task to be added"))
          create_task(task)
          continue
        elif select is 2:
          task = str(input("Enter task to be removed"))
          delete_task(task)
          continue
        elif select is 3:
          delete_all_tasks()
          continue
        elif select is 4:
          task = str(input("Enter task to be removed"))
          mark_as_finished(task)
          continue
        else:
          print ("Invalid input")
      # elif choice is 1:
      #  print (todo_list)
      else:
        print ("Invalid input")

