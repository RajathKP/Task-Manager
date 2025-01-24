import unittest
from datetime import datetime, timedelta
from Task import TaskManager,Task  # Assuming the task manager is implemented in task_manager.py

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """
        Set up a TaskManager instance for testing.
        """
        self.manager = TaskManager()
        self.future_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
        self.past_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    # Test Cases for Insertion
    def test_add_new_task(self):
        """
        Test adding a new task with valid information.
        """
        response = self.manager.add_task("Test Task", "This is a test task", 3, self.future_date)
        self.assertEqual(response, "Task 1 added successfully.")
        self.assertEqual(len(self.manager.tasks), 1)

    def test_add_task_with_no_title(self):
        """
        Test adding a task with no title.
        """
        response = self.manager.add_task("", "This is a test task", 3, self.future_date)
        self.assertEqual(response, "Error: Title required.")
        self.assertEqual(len(self.manager.tasks), 0)

    def test_add_task_with_past_deadline(self):
        """
        Test adding a task with a past deadline.
        """
        response = self.manager.add_task("Test Task", "This is a test task", 3, self.past_date)
        self.assertEqual(response, "Error: Deadline cannot be in the past.")
        self.assertEqual(len(self.manager.tasks), 0)

    # Test Cases for Deletion
    def test_delete_existing_task(self):
        """
        Test deleting an existing task.
        """
        self.manager.add_task("Test Task", "This is a test task", 3, self.future_date)
        response = self.manager.delete_task(1)
        self.assertEqual(response, "Task 1 deleted successfully.")
        self.assertEqual(len(self.manager.tasks), 0)

    # Test Cases for Sorting
    def test_sort_tasks_by_priority(self):
        """
        Test sorting tasks by priority.
        """
        self.manager.add_task("Low Priority Task", "Description", 1, self.future_date)
        self.manager.add_task("High Priority Task", "Description", 5, self.future_date)
        sorted_tasks = self.manager.view_tasks(sort_by="priority")
        self.assertTrue("High Priority Task" in sorted_tasks.splitlines()[0])

    def test_sort_tasks_by_deadline(self):
        """
        Test sorting tasks by deadline.
        """
        future_date_1 = (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d")
        future_date_2 = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
        self.manager.add_task("Task 1", "Description", 3, future_date_1)
        self.manager.add_task("Task 2", "Description", 3, future_date_2)
        sorted_tasks = self.manager.view_tasks(sort_by="deadline")
        self.assertTrue("Task 2" in sorted_tasks.splitlines()[0])

    # Test Cases for Searching
    def test_search_existing_task(self):
        """
        Test searching for an existing task.
        """
        self.manager.add_task("Test Task", "This is a test task", 3, self.future_date)
        response = self.manager.search_task(1)
        self.assertIn("Test Task", response)

    def test_search_nonexistent_task(self):
        """
        Test searching for a task that does not exist.
        """
        response = self.manager.search_task(99)
        self.assertEqual(response, "Error: Task not found.")

if __name__ == "__main__":
    unittest.main()
