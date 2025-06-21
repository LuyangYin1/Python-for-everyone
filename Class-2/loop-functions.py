def sum_and_product(arr):
    sum = 0
    product = 1
    for num in arr:
        sum += num
        product *= num
    return sum, product


arr = [12, 23, 34, 2, 56, 90]
print(sum_and_product(arr))  # sum and product
# arr.add(10)
print(sum_and_product(arr))
print(type(sum_and_product(arr)))  # tuple
