tasks = []

# Load tasks from file
file = open("tasks.txt", "r")

for line in file:
    tasks.append(line.strip())

file.close()


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

        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()

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

            try:
                task_number = int(input("Enter task number to remove: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)

                file = open("tasks.txt", "w")

                for task in tasks:
                    file.write(task + "\n")

                file.close()

                print("Removed:", removed_task)
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")