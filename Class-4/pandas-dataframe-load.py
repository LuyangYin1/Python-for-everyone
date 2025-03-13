import numpy as np
import pandas as pd 

def header(msg):
    print("1: Load hard coded data into df inside a function")
    df = pd.DataFrame(
        [['Jan',58,42,74,22,2.95],
        ['Feb',61,45,78,26,3.02],
        ['Mar',65,48,84,25,2.34],
        ['Apr',67,50,92,28,1.02],
        ['May',71,53,98,35,0.48],
        ['Jun',75,56,107,41,0.11],
        ['Jul',77,58,105,44,0.0]],
        index=[0,1,2,3,4,5,6],
        columns=['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
    print(df)
    return df 

def data_types(df):
    print(df.dtypes)
    print(df.index)
    print(df.columns)
    print(df.values)
    print(df.describe())
    print(df.describe(include='all'))   # includes all columns  
    print(df.mean())    # mean of all columns
    print(df.std())     # standard deviation of all columns 
    #print(df.sort_values('avg_high',ascending=False))


if __name__ == "__main__":
    print("1. Load hard coded data into df")
    header("hello world")
    print("2. Read from the file into data frame")
    filename = 'weather.csv'
    df = pd.read_csv(filename)
    print(df)
    print("3. print first 5 rows of data frame and last 3 rows of data frame")
    print(df.head())
    print(df.tail(3))
    print("4. get data types, index, columns, values")
    data_types(df)
    print("5. get statistical data")
    # slicing scalar value -- 
    print(df.iloc[3:5,0:2])
    #df['avg_high'] = np.average(df[:2])
    #print(df['avg_high'])
    # df['avg_day'] = (df[:2] + df['avg_low'])/2
    #print(df['avg_high'])