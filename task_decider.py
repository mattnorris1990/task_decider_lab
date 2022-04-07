from task import *


# def get_preferred_option(input_task_1, input_task_2):
# #  1 - 2
#     if input_task_1.name == "Wash Dishes" and input_task_2.name == "Cook Dinner":
#         return input_task_1.name
# # 1 - 3 
#     elif input_task_1.name == "Wash Dishes" and input_task_2.name == "Clean Windows":
#         return input_task_2.name
# # 1 - 4
#     elif input_task_1.name == "Wash Dishes" and input_task_2.name == "Do Ironing":
#         return input_task_2.name
# # 1 - 5
#     elif input_task_1.name == "Wash Dishes" and input_task_2.name == "Wash Clothes":
#         return input_task_1.name
# # 2 - 1
#     elif input_task_1.name == "Cook Dinner" and input_task_2.name == "Wash Dishes":
#         return input_task_2.name
# # 2 - 3
#     elif input_task_1.name == "Cook Dinner" and input_task_2.name == "Clean Windows":
#         return input_task_1.name
# # 2 - 4
#     elif input_task_1.name == "Cook Dinner" and input_task_2.name == "Do Ironing":
#         return input_task_1.name
# # 2 - 5
#     elif input_task_1.name == "Cook Dinner" and input_task_2.name == "Wash Clothes":
#         return input_task_2.name
# # 3 - 1 
#     elif input_task_1.name == "Clean Windows" and input_task_2.name == "Wash Dishes":
#         return input_task_1.name
# # 3 - 2
#     elif input_task_1.name == "Clean Windows" and input_task_2.name == "Cook Dinner":
#         return input_task_2.name
# # 3 - 4
#     elif input_task_1.name == "Clean Windows" and input_task_2.name == "Do Ironing":
#         return input_task_1.name
# # 3 - 5
#     elif input_task_1.name == "Clean Windows" and input_task_2.name == "Wash Clothes":
#         return input_task_2.name
# # 4 - 1
#     elif input_task_1.name == "Do Ironing" and input_task_2.name == "Wash Dishes":
#         return input_task_1.name
# # 4 - 2
#     elif input_task_1.name == "Do Ironing" and input_task_2.name == "Cook Dinner":
#         return input_task_2.name
# # 4 - 3
#     elif input_task_1.name == "Do Ironing" and input_task_2.name == "Clean Windows":
#         return input_task_2.name
# # 4 - 5
#     elif input_task_1.name == "Do Ironing" and input_task_2.name == "Wash Clothes":
#         return input_task_1.name
# # 5 - 1
#     elif input_task_1.name == "Wash Clothes" and input_task_2.name == "Wash Dishes":
#         return input_task_2.name
# # 5 - 2
#     elif input_task_1.name == "Wash Clothes" and input_task_2.name == "Cook Dinner":
#         return input_task_1.name
# # 5 - 3
#     elif input_task_1.name == "Wash Clothes" and input_task_2.name == "Clean Windows":
#         return input_task_1.name
# # 5 - 4
#     elif input_task_1.name == "Wash Clothes" and input_task_2.name == "Do Ironing":
#         return input_task_2.name
    
#     else:
#         return "not a task :("


# ALTERNATIVE SOLUTION

def get_preferred_option(input_task_1, input_task_2):
    if input_task_1.name == "Wash Dishes":
        if input_task_2.name == "Cook Dinner" or input_task_2.name == "Wash Clothes":
            return input_task_1.name
        else:
            return input_task_2.name

    if input_task_1.name == "Cook Dinner":
        if input_task_2.name == "Clean Windows" or input_task_2.name == "Do Ironing":
            return input_task_1.name
        else:
            return input_task_2.name    

    if input_task_1.name == "Clean Windows":
        if input_task_2.name == "Wash Dishes" or input_task_2.name == "Do Ironing":
            return input_task_1.name
        else:
            return input_task_2.name  

    if input_task_1.name == "Do Ironing":
        if input_task_2.name == "Wash Clothes" or input_task_2.name == "Wash Dishes":
            return input_task_1.name
        else:
            return input_task_2.name

    if input_task_1.name == "Wash Clothes":
        if input_task_2.name == "Clean Windows" or input_task_2.name == "Cook Dinner":
            return input_task_1.name
        else:
            return input_task_2.name
