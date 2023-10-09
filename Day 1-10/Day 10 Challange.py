todo_list = []

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added successfully!")
    elif choice == "2":
        if todo_list:
            print("Your To-Do List:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is empty!")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
