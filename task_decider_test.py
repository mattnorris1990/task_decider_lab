import unittest

from task import *
from task_decider import *

class TestTaskDecider(unittest.TestCase):
    def setUp(self):
        self.task_list = [
            {"name" : "Wash the Dishes",
            "duration" : .25},

            {"name" : "Cook Dinner",
            "duration" : .5},
            
            {"name" : "Clean Windows",
            "duration" : .75}
        ]

        self.task_1 = Task(self.task_list[0]["name"], self.task_list[0]["duration"])
        self.task_2 = Task(self.task_list[1]["name"], self.task_list[1]["duration"])

    def test_function_returns_task_name(self):
        self.assertEqual("Wash the Dishes", self.task_1.name)

    def test_function_returns_task_duration(self):
        self.assertEqual(.25, self.task_1.duration)

    def test_module_returns_task(self):
        self.assertEqual("Wash the Dishes", get_preferred_option(self.task_1.name, self.task_2.name))