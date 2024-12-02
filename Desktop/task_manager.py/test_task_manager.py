import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Initialise une instance de TaskManager pour chaque test"""
        self.manager = TaskManager("test_tasks.json")
        self.manager.tasks = []  # Réinitialise les tâches avant chaque test

    def test_add_task(self):
        """Teste l'ajout d'une tâche"""
        self.manager.add_task("Test task")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0]["description"], "Test task")
        self.assertFalse(self.manager.tasks[0]["completed"])

    def test_remove_task(self):
        """Teste la suppression d'une tâche"""
        self.manager.add_task("Task to remove")
        self.manager.remove_task(0)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_complete_task(self):
        """Teste la complétion d'une tâche"""
        self.manager.add_task("Task to complete")
        self.manager.complete_task(0)
        self.assertTrue(self.manager.tasks[0]["completed"])

    def test_list_tasks(self):
        """Teste la liste des tâches"""
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["description"], "Task 1")
        self.assertEqual(tasks[1]["description"], "Task 2")

    def tearDown(self):
        """Nettoie les fichiers après chaque test"""
        import os
        if os.path.exists("test_tasks.json"):
            os.remove("test_tasks.json")

if __name__ == "__main__":
    unittest.main()
