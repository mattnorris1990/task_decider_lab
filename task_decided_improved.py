from task import *

def get_preferred_option(input_task_1, input_task_2):
    if input_task_1 == "Wash Dishes":
        if input_task_2 == "Cook Dinner" or "Wash Clothes":
            return input_task_1.name
        else:
            return input_task_2.name

    if input_task_1 == "Cook Dinner":
        if input_task_2 == "Clean Windows" or "Do Ironing":
            return input_task_1.name
        else:
            return input_task_2.name    

    if input_task_1 == "Clean Windows":
        if input_task_2 == "Wash Dishes" or "Do Ironing":
            return input_task_1.name
        else:
            return input_task_2.name  

    if input_task_1 == "Do Ironing":
        if input_task_2 == "Wash Clothes" or "Wash Dishes":
            return input_task_1.name
        else:
            return input_task_2.name

    if input_task_1 == "Wash Clothes":
        if input_task_2 == "Clean Windows" or "Cook Dinner":
            return input_task_1.name
        else:
            return input_task_2.name

