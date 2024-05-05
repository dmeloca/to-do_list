from Modules.task import Task
from datetime import datetime
class ToDo:
    def __init__(self, tasks: list):
        self.tasks = tasks
    
    def get_tasks(self):
        counter = 1
        if len(self.tasks) == 0:
            print("[!] No tasks. Please type 'C' to create one.")
        else:
            for task in self.tasks:
                status_icon = "[]" if task.get_status() else "[ ]"
                print(f"{counter}. {status_icon} {task.get_name()}\n    |- deadline: {task.get_deadline()}")
                counter += 1
    
    def add_task(self, new_task):
        self.tasks.append(new_task)
    
    def delete_task(self, index_tak):
        if 0 <= index_tak < len(self.tasks):
            self.tasks.pop(index_tak)
        else:
            print("[!] Invalid task index.")
        
    def save_tasks(self, file_path):
        with open(file_path, 'w') as f:
            for task in self.tasks:
                f.write(f"{task._name},{task._end},{task._status}\n")
    
    def load_tasks(self, file_path):
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    name, end, status_str = line.strip().split(',')
                    status = True if status_str.strip().lower() == 'true' else False
                    task = Task(name, end, status)
                    if task.is_deadline_passed(): 
                        self.tasks.append(task)
                    else:
                        continue
                    
        except FileNotFoundError:
            print("[!] File not found.")
            self.tasks = []
