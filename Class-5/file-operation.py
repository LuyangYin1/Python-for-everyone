import numpy as np
import pandas as pd
import os as os

test = os.getcwd()
print(test + " is the current working directory")

print("1. Reading the file without pandas")
file = "weather.csv"
with open(file, "r") as file:
     print(file.read())
    
file.close()

print("2. Read from the file into data frame")
filename = 'weather.csv'
df = pd.read_csv(filename)
print(df.head())
print("3. writing the file ")
# # to write the file we use 'w' 
file_write = open('file_to_write.txt','w')
print(file_write.write(str(df)))
file_write.flush()
file_write.close()

os.chdir(test)


