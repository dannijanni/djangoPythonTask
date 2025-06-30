# from django.shortcuts import render

# # Create your views here.


# import os

# project_dir = r"F:\Assignement\Salik_Project_Code\Task_management_django\Task_management_django_backend"

# for root, _, files in os.walk(project_dir):
#     for file in files:
#         if file.endswith(".py"):
#             path = os.path.join(root, file)
#             with open(path, "rb") as f:
#                 if b'\x00' in f.read():
#                     print(f"Null byte found in: {path}")


file_path = r"F:\Assignement\Salik_Project_Code\Task_management_django\Task_management_django_backend\core\models.py"

with open(file_path, "rb") as f:
    content = f.read()

# Remove null bytes
cleaned = content.replace(b'\x00', b'')

with open(file_path, "wb") as f:
    f.write(cleaned)

print("Null bytes removed successfully.")
