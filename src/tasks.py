# --- tasks.py ---
# This file contains code that manages your todo_list
todo_list = ['fight win', 'lose']

# Write a function creates a task


def create_task(task):
    if not task:
        return "Please fill missing fields"
    if task.isdigit():
        return "Please input proper name for task"
    for item in todo_list:
        if task in item:
            return "{} already exists in the Todo list here {}".format(task, todo_list)
    print("The Todo list before we add {} is this {}".format(task, todo_list))
    todo_list.append(task)
    return "{} has been added and new Todo list is this {}".format(task, todo_list)

# Write a function deletes a task


def delete_task(task):
    """
    Removes the specified task from the todo_list
    """
    if not todo_list:
        return "Todo List is empty"
    if not task:
        return "Please fill missing fields"
    if task.isdigit():
        return "Please input proper name for task"
    if task not in todo_list:
        return "{} does not exist in the Todo list here {}".format(task, todo_list)
    deleted_task = todo_list.pop(todo_list.index(task))
    return "{} has been deleted and now the Todo list is this {}".format(deleted_task, todo_list)

# Write a function that marks a task finished


def mark_as_finished(task):
    """
    Append the string label '[finished]' at the end of the task
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    if not todo_list:
        return "Todo List is empty"
    if task not in todo_list:
        return "{} does not exist in the Todo list here {}".format(task, todo_list)
    not_finished = []
    for item in todo_list:
        if '[finished]' not in item:
            not_finished.append(item)
    if task in not_finished:
        finished_task = todo_list.pop(todo_list.index(task)) + '[finished]'
        todo_list.append(finished_task)
        return "{} has been marked as Finished".format(task)


# Write a function deletes all tasks


def delete_all_tasks():
    """
    Empty the the todo_list
    """
    if not todo_list:
        return "There are currently no tasks"
    todo_list.clear()
    return "All tasks successfully deleted and list has {} tasks".format(len(todo_list))


