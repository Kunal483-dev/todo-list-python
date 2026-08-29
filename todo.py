tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\n===== YOUR TASKS =====")

        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task)

            task_number = int(input("Enter task number to remove: "))
            removed_task = tasks.pop(task_number - 1)

            print("Removed:", removed_task)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")