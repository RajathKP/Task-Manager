from datetime import datetime

# Task class to represent a task
class Task:
    def __init__(self, task_id, title, description, priority, deadline, status="Pending"):
        """
        Represents a single task with attributes for ID, title, description, priority, deadline, and status.
        """
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.status = status

    def __str__(self):
        """
        String representation of the Task object for display.
        """
        return (f"ID: {self.task_id}, Title: {self.title}, Priority: {self.priority}, "
                f"Deadline: {self.deadline}, Status: {self.status}")


# TaskManager class to handle operations
class TaskManager:
    def __init__(self):

        self.tasks = {}

    def add_task(self, title, description, priority, deadline):

        # Add a new task to the manager.

        try:
            task_id = len(self.tasks) + 1
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
            if deadline_date < datetime.now():
                return "Error: Deadline cannot be in the past."
            new_task = Task(task_id, title, description, priority, deadline)
            self.tasks[task_id] = new_task
            return f"Task {task_id} added successfully."
        except ValueError:
            return "Error: Invalid deadline format. Use YYYY-MM-DD."

    # Delete a task by its ID.
    def delete_task(self, task_id):

        if task_id in self.tasks:
            del self.tasks[task_id]
            return f"Task {task_id} deleted successfully."
        return "Error: Task not found."

    # View all tasks, optionally sorted by priority or deadline.
    def view_tasks(self, sort_by=None):

        if not self.tasks:
            return "No tasks available."
        task_list = list(self.tasks.values())
        if sort_by == "priority":
            task_list.sort(key=lambda task: task.priority, reverse=True)
        elif sort_by == "deadline":
            task_list.sort(key=lambda task: datetime.strptime(task.deadline, "%Y-%m-%d"))
        return "\n".join(str(task) for task in task_list)

    # Search for a task by ID.
    def search_task(self, task_id):

        if task_id in self.tasks:
            return str(self.tasks[task_id])
        return "Error: Task not found."

    def complete_task(self, task_id):
        """
        Mark a task as completed.
        """
        if task_id in self.tasks:
            self.tasks[task_id].status = "Completed"
            return f"Task {task_id} marked as completed."
        return "Error: Task not found."

# CLI Functionality
def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Search Task")
        print("5. Complete Task")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            try:
                priority = str(input("Enter task priority (Low,Medium,High): "))
            except ValueError:
                print("Error: Please enter valid priority level ")
                continue
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            print(manager.add_task(title, description, priority, deadline))

        elif choice == "2":
            try:
                task_id = int(input("Enter task ID to delete: "))
                print(manager.delete_task(task_id))
            except ValueError:
                print("Error: Task ID must be a number.")

        elif choice == "3":
            print("\n1. View All Tasks")
            print("2. View Tasks Sorted by Priority")
            print("3. View Tasks Sorted by Deadline")
            sub_choice = input("Enter your choice (1-3): ")
            if sub_choice == "1":
                print(manager.view_tasks())
            elif sub_choice == "2":
                print(manager.view_tasks(sort_by="priority"))
            elif sub_choice == "3":
                print(manager.view_tasks(sort_by="deadline"))
            else:
                print("Invalid choice.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to search: "))
                print(manager.search_task(task_id))
            except ValueError:
                print("Error: Task ID must be a number.")

        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                print(manager.complete_task(task_id))
            except ValueError:
                print("Error: Task ID must be a number.")

        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the CLI application
if __name__ == "__main__":
    main()
