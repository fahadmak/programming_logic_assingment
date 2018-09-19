import unittest
from src.tasks import create_task, delete_all_tasks, delete_task, mark_as_finished


class TestTasks(unittest.TestCase):

    # Tests for create task
    def test_create_task(self):
        add_task = create_task("Brush your teeth")
        self.assertIn("Brush your teeth has been added", add_task)

    def test_if_task_exists(self):
        add_task = create_task("Edinburgh")
        add_task = create_task("Edinburgh")
        self.assertIn("Edinburgh already exists in the Todo list here ['Edinburgh']", add_task)

    def test_if_task_integer(self):
        add_task = create_task("7")
        self.assertIn("Please input proper name for task", add_task)

    def test_if_task_empty(self):
        add_task = create_task("")
        self.assertIn("Please fill missing fields", add_task)

    # Tests for delete task

    def test_delete_task(self):
        create_task("Free style")
        del_task = delete_task("Free style")
        self.assertIn("Free style has been removed", del_task)

    def test_delete_task_does_not_exist(self):
        del_task = delete_task("Swimming")
        self.assertIn('Swimming does not exist in the Todo list here []', del_task)

    # Tests for mark as finished

    def test_mark_as_finished(self):
        create_task("Bing")
        mark_as_finished("Bing")
        self.assertIn('[finished]', "Go to Nasser[finished]")

    def test_task_is_does_not_exist(self):
        marked = mark_as_finished("Bring man")
        self.assertIn('Bring man does not exist in the Todo list here []', marked)

    def test_delete_all_tasks(self):
        create_task("Free")
        create_task("style")
        del_tasks = delete_all_tasks()
        self.assertIn("All tasks successfully deleted", del_tasks)

    def test_no_tasks_to_delete(self):
        delete_all_tasks()
        del_tasks = delete_all_tasks()
        self.assertIn("There are currently no tasks", del_tasks)


