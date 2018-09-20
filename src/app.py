# ---- app.py ----
# This file contains the entry point to your tasks
# and the logic to manage it

from src.tasks import get_tasks, create_task, delete_task, delete_all_tasks, mark_as_finished  # import other functions as well
from src.accounts import login_prompt  # import the function as well


selections = "\n" \
  "Select Option:\n" \
  "1. Create Task\n"\
  "2. deleting a task\n"\
  "3. deleting all tasks\n"\
  "4. Marking a task finished\n"\
  "5. View Tasks\n"\
  "6. Log out\n"\
  "7. Exit"


def new_line():
    print("")


def select():
    new_line()
    print(selections)
    new_line()
    selection = input("Choose an option [Should be a number]: ")

    if selection is '1':
        while True:
            new_line()
            prompt = input("Do you want to add task yes/no: ")
            if prompt == 'yes':
                get_tasks()
                task = input("enter task to add: ")
                task = create_task(task)
                print(task)
            if prompt == 'no':
                return select()

    elif selection is '2':
        while True:
            new_line()
            prompt = input("Do you want to delete a task, yes/no: ")
            if prompt == 'yes':
                get_tasks()
                new_line()
                num = input("enter task number: ")
                task = delete_task(num)
                print(task)
            if prompt == 'no':
                return select()

    elif selection is '3':
        new_line()
        prompt = input("Are you sure want to delete the todo list, yes/no? : ")
        if prompt == 'yes':
            get_tasks()
            tasks = delete_all_tasks()
            print(tasks)
            print("")
        if prompt is 'no':
            print("Your tasks are still safe")
            return select()

    elif selection is '4':
        while True:
            new_line()
            prompt = input("Do you want to mark a task as finished, yes/no: ")
            if prompt == 'yes':
                get_tasks()
                task = input("enter task to mark: ")
                task = mark_as_finished(task)
                print(task)
                new_line()
            if prompt == 'no':
                return select()

    elif selection is '5':
        new_line()
        get_tasks()
        return select()

    elif selection is '6':
        new_line()
        print("You are Logging out.............")
        new_line()
        login_prompt()
        return select()

    elif selection is '7':
        new_line()
        print("Thank You, Until Next Time.............")
        return

    else:
        new_line()
        print("Wrong selection try the ones listed")
        return select()


if __name__ == "__main__":

    login_prompt()
    select()


