import numpy as np
import pandas as pd
import os as os
# import wget 

# url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
# file = wget.download(url)
#url2 = 'https://www.youtube.com/watch?v=2aclOPvhbn0'
# url2 = 'https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2lCZWtHWlUxcGVGWWpWV3lLMUhILXUxSUV0UXxBQ3Jtc0tsWE5ScWthX0EwbzBiMUxxS1FnNGlPck53UnY3WXl4eUN6akszaG5YM2NST1l0WFNwdklKemFJU09RczlWdjQ3S2tEMnBSaWFoaUNtZE13bUsyOThqV1dONFdKenc1STZPOVRILXJwdkQzWkUzVjFqRQ&q=https%3A%2F%2Fbit.ly%2F3MsE6Dd&v=ElRVZ09939k'
## os.chdir("C:/Users/abamba/Documents/Python/Class-5")
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

# # Deleting and Renaming the files 

# sleep(50)
# os.rename('file_to_write.txt',"output.csv")
# os.remove("file_to_write.txt")
os.chdir(test)
# getting the file from internet 
# import wget
# url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
# file = wget.download(url)

# # # getting the file from internet
# url2 = 'https://www.youtube.com/watch?v=2aclOPvhbn0'   
# file = wget.download(url2)

