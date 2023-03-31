import os
import time
def searchFile():
    filename="demo1.py"
    dir="jose123"
    f=[]
    for root,dir,file in os.walk(dir):
        if filename in file:
            f.append(os.path.join(root,filename))
    return f
start_time=time.time()
files=searchFile()
print(files)
end_time=time.time()
execution_time = end_time-start_time
print(f"Execution time: {execution_time:.5f} seconds")

