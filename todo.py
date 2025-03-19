import json
import os
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json','r') as file:
            return json.load(file)
    return[]
def save_tasks(tasks):
    with open('tasks.json','w') as file:
        json.dump(tasks,file,indent=4)
def display_tasks(tasks):
    if tasks:
        print("\nYour To-Do-List:")
        for i, task in enumerate(tasks,1):
            print(f"{i}.{task}")
    else:
        print("No tasks to display.")
def add_task(tasks,task):
    tasks.append(task)
    save_tasks(tasks)
def delete_task(tasks,task_index):
    if 0<task_index<=len(tasks):
        tasks.pop(task_index-1)
        save_tasks(tasks)
    else:
        print("Invalid number!")
def main():
    tasks=load_tasks()
    while True:
        print("\n1.View Tasks")
        print("2.Add Task")
        print("3. Delete task")
        print("4. Exit")
        choice=input("Choose an option:")
        if choice=='1':
            display_tasks(tasks)
        elif choice=='2':
            task=input("enter task to add:")
            add_task(tasks,task)
        elif choice=='3':
            display_tasks(tasks)
            task_index=int(input("enter task number to delete:"))
            delete_task(tasks,task_index)
        elif choice=='4':
            print("Exiting program...")
            break
        else:
            print("Invalid option,please try again")
if __name__=="__main__":
    main()


