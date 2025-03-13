try:
    # print(10/0)
    text = "Hello"
    number = int(text)
except ValueError:
    print("Code for Value Error")
except ZeroDivisionError:
    print("code for zero division")
except:
    print("code for other exceptions")
finally:
    print("Always Executed!")