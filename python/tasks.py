todo_list = []
#function that creates tasks
def create_task(task):
    """
    Adds the task (string value) to todo_list
    """
    
    return todo_list.append(task)

#function that deletes the task
def delete_task(task):
    """
    Removes the specified task from the todo_list
    """
    return todo_list.remove(task)

#function that marks a task finiished
def mark_as_finished(task):
    """
    Appends the string lable '[finished]' at the end of the task
    """
    return task + " [finished]"

#function that deletes all tasks
def delete_all_tasks():
    """
    deletes all tasks from the todo_list
    """
    return todo_list.clear()
