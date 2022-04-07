from task import *

# def get_preferred_option(input_task_1, input_task_2):
#     return input_task_1, input_task_2


def get_preferred_option(input_task_1, input_task_2):
    if input_task_1.name == "Wash the Dishes" and input_task_2.name == "Cook Dinner":
        return input_task_1.name

    elif input_task_1.name == "Wash the Dishes" and input_task_2.name == "Clean Windows":
        return input_task_2.name
