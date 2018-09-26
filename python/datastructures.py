Todo_lists = []

def create_todo_list():
    todo_ = input("Enter list name ")
    task1 = str(input("Enter task"))
    detail1 = str(input("Enter details"))
    task2 = str(input("Enter task"))
    detail2 = str(input("Enter details"))
    task3 = str(input("Enter task"))     
    detail3 = str(input("Enter details"))
    task4 = str(input("Enter task")) 
    detail4 = str(input("Enter details"))
    todo_ ={}
    todo_[task1] = detail1
    todo_[task2] = detail2
    todo_[task3] = detail3
    todo_[task4] = detail4
    Todo_lists.append(todo_)
    return Todo_lists

print (create_todo_list())
