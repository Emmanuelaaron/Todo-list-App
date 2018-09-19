from tasks import todo_list
from tasks import *
from accounts import accounts
from accounts import *

if __name__ == "__main__":
    name = input("Enter your name:")
    password = input("Enter your password:")
    for key in accounts:
        if key is name and accounts[key] is password:
            login(name, password)
        else:
            add_account(name, password)
    print ("Select Option:")
    print ("1. Create task ")
    print ("2. delete task")
    print ("3. delete all tasks")
    print ("4. mark task finished")
    select = input("selection: ")


