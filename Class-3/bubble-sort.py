from datetime import datetime


# Bubble Sort Implementation
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                temp = a[i]
                a[i] = a[i - 1]
                a[i - 1] = temp


def bubble_sort_optimized(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]  # Swap


# Optimized bubble sort function
# This function sorts a list in ascending order using the bubble sort algorithm.
names = ["pretzels", "carrots", "arugula", "bacon"]
time_unoptimized_start = datetime.now()
print("Time before sorting:", time_unoptimized_start)
bubble_sort(names)
time_unoptimized_end = datetime.now()
print("Time after sorting:", time_unoptimized_end)
print(
    "Time taken for unoptimized bubble sort:",
    time_unoptimized_end - time_unoptimized_start,
)
print(names)
# This function sorts a list in ascending order using the bubble sort algorithm.
# It uses a simple comparison and swapping mechanism to sort the elements.
time_optimized_start = datetime.now()
print("Time before sorting:", time_optimized_start)
bubble_sort_optimized(names)
time_optimized_end = datetime.now()
print("Time after sorting:", time_optimized_end)
print(names)
print(
    "Time taken for optimized bubble sort:", time_optimized_end - time_optimized_start
)
