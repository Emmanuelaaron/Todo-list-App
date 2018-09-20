from tasks import todo_list
from tasks import *
from accounts import accounts
from accounts import *

if __name__ == "__main__":
    name = input("Enter your name:")
    password = input("Enter your password:")
    add_account(name, password)
    while login(name, password):
        print ("\nSelect Option")
        print ("1. Creat task")
        print ("2. delete task")
        print ("3. delete all tasks")
        print ("4. mark task finished\n")
        select = int(input("Selection: "))
        if select is 1:
            task = str(input("Enter task to be added"))
            print (create_task(task))
            continue
        elif select is 2:
            task = str(input("Enter task to be removed"))
            print (delete_task(task))
            continue
        elif select is 3:
            print (delete_all_tasks())
            continue
        elif select is 4:
            task = str(input("Enter task finished"))
            print (mark_as_finished(task))
            continue
        else:
            exit

