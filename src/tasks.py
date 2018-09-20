# --- tasks.py ---
# This file contains code that manages your todo_list
todo_list = {'1': 'fight win', '2': 'lose'}

# Write a function creates a task


def create_task(task):
    if not task.isalpha():
        return "Please input proper name for task"
    for item in list(todo_list.values()):
        if task in item:
            return "{} already exists in the Todo list".format(task)
    task_number = str(len(todo_list) + 1)
    todo_list[task_number] = task
    return "{} has been added and new Todo list".format(task)

# Write a function deletes a task


def delete_task(task_number):
    """
    Removes the specified task from the todo_list
    """
    if not todo_list:
        return "Todo List is empty"
    if not task_number:
        return "Please fill missing fields"
    try:
        deleted_task = todo_list.pop(task_number)
        return "{} has been deleted".format(deleted_task)
    except KeyError:
        return "This task number does not exist"

# Write a function that marks a task finished


def mark_as_finished(task_number):
    """
    Append the string label '[finished]' at the end of the task
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    if not todo_list:
        return "Todo List is empty"
    if not task_number:
        return "Please fill missing fields"
    not_finished = []
    try:
        for item in list(todo_list.values()):
            if '[finished]' not in item:
                not_finished.append(item)
        if todo_list[task_number] in not_finished:
            finished_task = todo_list.pop(task_number) + ' ' + '[finished]'
            todo_list[task_number] = finished_task
            return "{} has been marked as Finished".format(todo_list[task_number].replace('[finished]', ''))
        return "{} has already been marked as Finished".format(todo_list[task_number].replace('[finished]', ''))
    except KeyError:
        return "This task number does not exist"


# Write a function deletes all tasks


def delete_all_tasks():
    """
    Empty the the todo_list
    """
    if not todo_list:
        return "There are currently no tasks"
    todo_list.clear()
    return "All tasks successfully deleted"


def get_tasks():
    """
        Get the tasks in the todo_list
    """
    print("All the tasks")
    if not todo_list:
        print("There are currently no tasks")
    for k, v in todo_list.items():
        print("{}.  {}".format(k, v))


