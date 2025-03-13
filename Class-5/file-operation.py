import numpy as np
import pandas as pd
from os import remove, rename
# import wget 

# url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
# file = wget.download(url)
#url2 = 'https://www.youtube.com/watch?v=2aclOPvhbn0'
# url2 = 'https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2lCZWtHWlUxcGVGWWpWV3lLMUhILXUxSUV0UXxBQ3Jtc0tsWE5ScWthX0EwbzBiMUxxS1FnNGlPck53UnY3WXl4eUN6akszaG5YM2NST1l0WFNwdklKemFJU09RczlWdjQ3S2tEMnBSaWFoaUNtZE13bUsyOThqV1dONFdKenc1STZPOVRILXJwdkQzWkUzVjFqRQ&q=https%3A%2F%2Fbit.ly%2F3MsE6Dd&v=ElRVZ09939k'
#file = wget.download(url2)


print("1. Reading the file without pandas")
file = "weather.csv"
with open(file, "r",1,4096) as file:
     print(file.read())
    
file.close()

print("2. Read from the file into data frame")
filename = 'weather.csv'
df = pd.read_csv(filename)
print(df.head())
print("3. writing the file ")
# # to write the file we use 'w' 
file_write = open('file_to_write','w')
print(file_write.write(str(df)))
file_write.flush()
file_write.close()

# # Deleting and Renaming the files 
remove("new-file.txt")
rename("file-to-write.txt","output.csv")

# getting the file from internet 
import wget
url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
file = wget.download(url)

# # getting the file from internet
url2 = 'https://www.youtube.com/watch?v=2aclOPvhbn0'   
file = wget.download(url2)

