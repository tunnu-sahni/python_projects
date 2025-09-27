# TO DO LIST
def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readline()
            if not tasks:
                print("\n no tasks found!\n")

            else:
                print("\n Your To Do List:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}.{task.scrip()}")
    except  FileNotFoundError:
            print("\n No tasks found!\n")

def add_task():
    task = input("enter new task:")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
        print("Task added successfully!")

def remove_task():
    show_tasks()
    try:
        task_no = int(input("enter task number to remove: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readline()
            if 0 < task_no <= len(tasks):
                removed = tasks.pop(task_no -1)
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print(f"removed task: {removed.scrip()}")

            else:
                print("invalid task number.")
    except ValueError:
            print("please enter a valid number.")

def main():
    while True:
        print("\n===== TO-DO LIST MENU=====")

        print("1. view tasks")
        print("2. add tasks")
        print("3. remove tasks")
        print("4. exit")

        choice = input("enter choice (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("exiting... have a productive day!")
            break
        else:
            print("invalid choice please try again.")

        if __name__ == "__main__":
            main()     