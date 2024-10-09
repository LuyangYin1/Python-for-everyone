import numpy as np
import pandas as pd
from os import remove, rename


print("1. Reading the file without pandas")
file = "weather.csv"
with open(file, "r") as file:
    print(file.read())
file.close()

print("2. Read from the file into data frame")
filename = 'weather.csv'
df = pd.read_csv(filename)

print("3. writing the file ")
# to write the file we use 'w' 
file_write = open('file_to_write','w')
print(file_write.write(str(df)))
file_write.flush()
file_write.close()

# Deleting and Renaming the files 
remove("new-file.txt")
rename("file-to-write.txt","output.csv")
