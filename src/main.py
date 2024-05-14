from Modules.todo import ToDo
from Modules.task import Task
import datetime

value_error_message = "[!] Please insert an integer number."
index_error_message = "[!] The task with the given index does not exist."
today_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
def is_date_formatted_correctly(deadline:str):
    try:
        datetime.datetime.strptime(deadline,  "%Y-%m-%d %H:%M")
        return True
    except ValueError:
        return False    
    
def create_task(to_do: ToDo):
    name_new_task = input("[?] Please insert the new task name: ")
    try:
        end_new_task = input("[?] Please insert when the task's deadline (format: YYYY-MM-DD hh:mm): ")
        if is_date_formatted_correctly(end_new_task):

            new_task = Task(name_new_task, end_new_task, False)
            to_do.add_task(new_task)
            print(f"[!] {name_new_task} added!")
            to_do.get_tasks()
        else:
            print("[!] the date is not valid")
    except ValueError:
        print(value_error_message)

def date_change_task(to_do: ToDo) -> None:
    try:
        index_task = int(input("[?] Please insert the index of the task you want to change deadline: "))
        date = input("[?] Insert the new dead line (format: YYYY-MM-DD hh:mm) ")
        if is_date_formatted_correctly(date):
            to_do.tasks[index_task-1].change_date(date)  # Adjust index to 0-based
            to_do.get_tasks()
        else:
            print("[!] The date is not valid")
    except ValueError:
        print(value_error_message)
    except IndexError:
        print(index_error_message)

def delete_task(to_do: ToDo):
    try:
        index_task = int(input("[?] Please insert the index of the task you want to delete: "))
        to_do.delete_task(index_task - 1)  # Adjust index to 0-based
        to_do.get_tasks()
    except ValueError:
        print(value_error_message)
    except IndexError:
        print(index_error_message)

def change_task_status(to_do: ToDo):
    try:
        index_task = int(input("[?] Please insert the index of the task you want to change its status: "))
        to_do.tasks[index_task - 1].change_status()  # Adjust index to 0-based
        to_do.get_tasks()
    except ValueError:
        print(value_error_message)
    except IndexError:
        print(index_error_message)

def main():
    to_do_list = ToDo([])
    to_do_list.load_tasks('list.txt')
    print("="*35)
    print("|           TO-DO LIST            |")
    print("="*35)
    to_do_list.get_tasks()
    print("="*35)
    print(f"[-]Today is: {today_date}")
    while True:
        user_choice = input("[?] What do you want to do:\n |-(C)reate a new task\n |-(D)elete a task\n |-(M)ark as done or not done\n |-Ch(A)nge deadline\n |-(E)xit and save: ")
        if user_choice.lower() == 'c':
            create_task(to_do_list)
        elif user_choice.lower() == 'd':
            delete_task(to_do_list)
        elif user_choice.lower() == 'm':
            change_task_status(to_do_list)
        elif user_choice.lower() == 'a':
            date_change_task(to_do_list)
        elif user_choice.lower() == 'e':
            to_do_list.save_tasks('list.txt')
            print("[!] The tasks were saved.")
            exit(0)
        else:
            print("[!] Invalid option.")

if __name__ == "__main__":
    main()
