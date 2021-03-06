import unittest

from task import *
from task_decider import *

class TestTaskDecider(unittest.TestCase):
    def setUp(self):
        self.task_list = [
            {"name" : "Wash Dishes",
            "duration" : .25},

            {"name" : "Cook Dinner",
            "duration" : .5},
            
            {"name" : "Clean Windows",
            "duration" : .75},
            {"name" : "Do Ironing",
            "duration" : 1.5},
            {"name" : "Wash Clothes",
            "duration" : 1.0}
        ]

        self.task_1 = Task(self.task_list[0]["name"], self.task_list[0]["duration"])
        
        self.task_2 = Task(self.task_list[1]["name"], self.task_list[1]["duration"])
        
        self.task_3 = Task(self.task_list[2]["name"], self.task_list[2]["duration"])
        
        self.task_4 = Task(self.task_list[3]["name"], self.task_list[3]["duration"])
        
        self.task_5 = Task(self.task_list[4]["name"], self.task_list[4]["duration"])

    # def test_function_returns_task_name(self):
    #     self.assertEqual("Wash the Dishes", self.task_1.name)

    # def test_function_returns_task_duration(self):
    #     self.assertEqual(.25, self.task_1.duration)

    # def test_module_returns_task(self):
    #     self.assertEqual("Wash the Dishes", get_preferred_option(self.task_1.name, self.task_2.name))

    # def test_module_returns_tasks(self):
    #     self.assertEqual(("Wash the Dishes", "Cook Dinner"), get_preferred_option(self.task_1.name, self.task_2.name))

    def test_wash_dishes_cook_dinner(self):
        self.assertEqual("Wash Dishes", get_preferred_option(self.task_1, self.task_2))

    def test_wash_dishes_clean_windows(self):
        self.assertEqual("Clean Windows", get_preferred_option(self.task_1, self.task_3))

    def test_cook_dinner_wash_dishes(self):
        self.assertEqual("Wash Dishes", get_preferred_option(self.task_2, self.task_1))

    def test_cook_dinner_clean_windows(self):
        self.assertEqual("Cook Dinner", get_preferred_option(self.task_2, self.task_3))

    def test_clean_windows_wash_dishes(self):
        self.assertEqual("Clean Windows", get_preferred_option(self.task_3, self.task_1))

    def test_clean_windows_cook_dinner(self):
        self.assertEqual("Cook Dinner", get_preferred_option(self.task_3, self.task_2))   

    def test_wash_dishes_do_ironing(self):
        self.assertEqual("Do Ironing", get_preferred_option(self.task_1, self.task_4)) 

    def test_wash_dishes_wash_clothes(self):
        self.assertEqual("Wash Dishes", get_preferred_option(self.task_1, self.task_5)) 

    def test_cook_dinner_iron_clothes(self):
        self.assertEqual("Cook Dinner", get_preferred_option(self.task_2, self.task_4)) 

    def test_cook_dinner_wash_clothes(self):
        self.assertEqual("Wash Clothes", get_preferred_option(self.task_2, self.task_5)) 

    def test_clean_windows_do_ironing(self):
        self.assertEqual("Clean Windows", get_preferred_option(self.task_3, self.task_4)) 

    def test_clean_windows_wash_clothes(self):
        self.assertEqual("Wash Clothes", get_preferred_option(self.task_3, self.task_5)) 

    def test_do_ironing_wash_dishes(self):
        self.assertEqual("Do Ironing", get_preferred_option(self.task_4, self.task_1)) 

    def test_do_ironing_cook_dinner(self):
        self.assertEqual("Cook Dinner", get_preferred_option(self.task_4, self.task_2)) 

    def test_do_ironing_clean_windows(self):
        self.assertEqual("Clean Windows", get_preferred_option(self.task_4, self.task_3)) 

    def test_do_ironing_wash_clothes(self):
        self.assertEqual("Do Ironing", get_preferred_option(self.task_4, self.task_5)) 

    def test_wash_clothes_wash_dishes(self):
        self.assertEqual("Wash Dishes", get_preferred_option(self.task_5, self.task_1)) 

    def test_wash_clothes_cook_dinner(self):
        self.assertEqual("Wash Clothes", get_preferred_option(self.task_5, self.task_2)) 

    def test_wash_clothes_clean_windows(self):
        self.assertEqual("Wash Clothes", get_preferred_option(self.task_5, self.task_3)) 

    def test_wash_clothes_do_ironing(self):
        self.assertEqual("Do Ironing", get_preferred_option(self.task_5, self.task_4)) 