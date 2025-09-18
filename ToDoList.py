# TO DO LIST

def show_menu():
    print("\n___ To Do List MENU___")
    print("1. add task")
    print("2. view task")
    print("3. remove task")
    print("4. exit")

while True:
    show_menu()
    choice = input("enter your choice (1-4):")

    if choice == "1":
        task = input("enter new task :")
        task.append(task)
        print(f" task '{task}' added successfully")

    elif choice == "2":
        if not task:
            print("no task in the list.")
        else:

            print("\n your task:")
        for i, task in
            (task, start=1)
        print("no task in delete.")
    elif choice == "3":
        if not task:
            print("no task in delete")

        else:
            task_no =int(input("enter task number to delete:"))
            if 1 <= task_no <= len(task):
                removed = task.pop(task_no -1)
                print(f"task '{removed}' deleted successfully")
            else:
                print("invalid task number.")

    elif choice == "4":
        print("exiting to -do list. goodbye")
        break

    else:
         print("invalid choice please select 1-4.")