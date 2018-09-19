# ---- app.py ----
# This file contains the entry point to your tasks
# and the logic to manage it

from src.tasks import todo_list, create_task, delete_task, delete_all_tasks, mark_as_finished  # import other functions as well
from src.accounts import accounts, add_account, login  # import the function as well


if __name__ == "__main__":
    """
        Allow a person to input a name and a password

        E.g
    """

    """
        Let the person sign in. If there details do not exist,
        create an account for them

        E.g 
    """

    while True:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        if not(name is "" or password is ""):
            if not(name.isdigit() or password.isdigit()):
                if not(name in accounts.values() or password in accounts.keys()):
                    account = add_account(name, password)
                    print(account)
                    print("")
                    break
                account = [[password, name]for k, v in accounts.items() if k == password and v == name]
                if account:
                    user = login(name, password)
                    print(user)
                    print("")
                    break
                print("Please input correct password and name to login")
            print("Dont use numbers")


    """
        Provide options:
            1. creating a task
            2. deleting a task 
            3. deleting all tasks
            4. Marking a task finished

        E.g
    """
    while True:
        print("Select Option:")
        print("1. Create Task")
        print("2. deleting a task")
        print("3. deleting all tasks")
        print("4. Marking a task finished")
        print("5. Exit")
        selection = input("selection: ")

        if selection is '1':
            while True:
                prompt = input("Do you want to add task yes/no: ")
                if prompt == 'yes':
                    task = input("enter task to add: ")
                    task = create_task(task)
                    print(task)
                    print("")
                if prompt == 'no':
                    break

        if selection is '2':
            while True:
                prompt = input("Do you want to delete task yes/no: ")
                if prompt == 'yes':
                    task = input("enter task to delete: ")
                    task = delete_task(task)
                    print(task)
                    print("")
                if prompt == 'no':
                    break

        if selection is '3':
            prompt = input("Are you sure want to delete the todo list, yes/no? : ")
            if prompt == 'yes':
                tasks = delete_all_tasks()
                print(tasks)
            if prompt is 'no':
                print("Your tasks are still safe")
                print("")

        if selection is '4':
            while True:
                prompt = input("Do you want to mark a task as finished, yes/no: ")
                if prompt == 'yes':
                    task = input("enter task to mark: ")
                    task = mark_as_finished(task)
                    print(task)
                    print("")
                if prompt == 'no':
                    break

        if selection is '5':
            print("You are Logging out.............")
            break

# Write code that implements the selected option

"""
The above should appear as
    Select Options:
        1. Create Task
        2 .... 
        3 ....
        4 ....

    selection:
"""

