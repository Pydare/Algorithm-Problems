import os

os.chdir(r'C:\Users\Deron Doherty\Videos\Pandas')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name.split('Python Pandas Tutorial'))