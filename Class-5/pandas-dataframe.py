import numpy as np
import pandas as py

def getDataFromFile(filename):
    if (filename):
        df = py.read_csv(filename)
        print(df)