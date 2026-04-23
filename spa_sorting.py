import time
import random

# ----------------- Insertion Sort -----------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# ----------------- Merge Sort -----------------
def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # stable
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


# ----------------- Quick Sort (FIXED) -----------------
def partition(arr, low, high):
    # Random pivot to avoid worst case
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:   # IMPORTANT FIX
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# ----------------- Timing Function -----------------
def measure_time(sort_func, arr):
    arr_copy = arr.copy()
    start = time.time()

    if sort_func == quick_sort:
        sort_func(arr_copy, 0, len(arr_copy) - 1)
    else:
        sort_func(arr_copy)

    end = time.time()
    return (end - start) * 1000  # ms


# ----------------- Dataset Generator -----------------
def generate_datasets(size):
    random_list = random.sample(range(1, 100000), size)
    sorted_list = sorted(random_list)
    reverse_list = sorted_list[::-1]

    return random_list, sorted_list, reverse_list


# ----------------- MAIN -----------------
sizes = [100, 500, 1000]   # safe sizes (no crash)

with open("output.txt", "w") as f:

    # -------- Correctness Check --------
    test = [5, 2, 9, 1, 5, 6]

    temp = test.copy()
    insertion_sort(temp)
    f.write("Insertion Sort Test: " + str(temp) + "\n")

    temp = test.copy()
    merge_sort(temp)
    f.write("Merge Sort Test: " + str(temp) + "\n")

    temp = test.copy()
    quick_sort(temp, 0, len(temp)-1)
    f.write("Quick Sort Test: " + str(temp) + "\n\n")

    # -------- Experiments --------
    for size in sizes:
        random_list, sorted_list, reverse_list = generate_datasets(size)

        for name, dataset in [
            ("Random", random_list),
            ("Sorted", sorted_list),
            ("Reverse", reverse_list)
        ]:

            f.write(f"\nSize: {size}, Type: {name}\n")

            t1 = measure_time(insertion_sort, dataset)
            t2 = measure_time(merge_sort, dataset)
            t3 = measure_time(quick_sort, dataset)

            f.write(f"Insertion Sort: {t1:.2f} ms\n")
            f.write(f"Merge Sort: {t2:.2f} ms\n")
            f.write(f"Quick Sort: {t3:.2f} ms\n")

print("Program executed successfully. Check output3.txt")
