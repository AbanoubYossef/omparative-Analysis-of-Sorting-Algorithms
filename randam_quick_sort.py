import random

# Function to perform the partitioning step of Quick Sort
def partition(my_list, left, right):
    pivot = my_list[left]  # Choose the leftmost element as the pivot
    m = left  # Initialize the pivot's final position

    for item in range(left + 1, right + 1):
        if my_list[item] < pivot:
            m += 1
            my_list[item], my_list[m] = my_list[m], my_list[item]  # Swap smaller elements to the left

    my_list[left], my_list[m] = my_list[m], my_list[left]  # Place the pivot in its correct position
    return m  # Return the pivot index

# Function to choose a random pivot and call the partition function
def rand_partition(my_list, left, right):
    random_pivot = random.randint(left, right)  # Choose a random pivot
    my_list[left], my_list[random_pivot] = my_list[random_pivot], my_list[left]  # Swap the pivot with the leftmost element
    return partition(my_list, left, right)

# Function to perform randomized Quick Sort
def randomized_quick_sort(my_list, left, right):
    if left < right:
        random_pivot = rand_partition(my_list, left, right)  # Randomly select a pivot and partition
        randomized_quick_sort(my_list, left, random_pivot - 1)  # Recursively sort the left subarray
        randomized_quick_sort(my_list, random_pivot + 1, right)  # Recursively sort the right subarray

# Define your list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Call the randomized Quick Sort function
randomized_quick_sort(my_list, 0, len(my_list) - 1)

# Print the sorted list
print("Sorted List:", my_list)
