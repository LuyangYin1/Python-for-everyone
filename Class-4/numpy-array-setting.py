import numpy as np

def getInput():
    name = input("enter your name")
    getbanktransactions(name)


def getbanktransactions(name):
    transactions = np.array([12.34,100.34,-5,0.89],dtype=np.float32)
    print("Welcome to Chase bank %s" %name)
    print("Your lase four bank transactions are %s" %transactions )



if __name__ == '__main__':  # starts the program 
    print ("we are starting the project")
    getInput()