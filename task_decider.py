from task import *

# def get_preferred_option(input_task_1, input_task_2):
#     return input_task_1, input_task_2


def get_preferred_option(input_task_1, input_task_2):
#  1 - 2
    if input_task_1.name == "Wash Dishes" and input_task_2.name == "Cook Dinner":
        return input_task_1.name
# 1 - 3 
    elif input_task_1.name == "Wash Dishes" and input_task_2.name == "Clean Windows":
        return input_task_2.name
# 2 - 1
    elif input_task_1.name == "Cook Dinner" and input_task_2.name == "Wash Dishes":
        return input_task_2.name
# 2 - 3
    elif input_task_1.name == "Cook Dinner" and input_task_2.name == "Clean Windows":
        return input_task_1.name
# 3 - 1 
    elif input_task_1.name == "Clean Windows" and input_task_2.name == "Wash Dishes":
        return input_task_1.name
# 3 - 2
    elif input_task_1.name == "Clean Windows" and input_task_2.name == "Cook Dinner":
        return input_task_2.name
