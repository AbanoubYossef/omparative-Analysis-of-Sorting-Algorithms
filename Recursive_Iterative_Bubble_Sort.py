import random
import timeit
import matplotlib.pyplot as plt
import sys

# Increase the recursion limit
sys.setrecursionlimit(55500)

def iterative_bubble_sort(my_list):
    length_mylist = len(my_list)
    assignments = 0
    comparisons = 0
    for pass_num in range(length_mylist):
        swapped = False
        for current_index in range(0, length_mylist - pass_num - 1):
            comparisons += 1
            if my_list[current_index] > my_list[current_index + 1]:
                my_list[current_index], my_list[current_index + 1] = my_list[current_index + 1], my_list[current_index]
                assignments += 3  # Three assignments for swapping
                swapped = True
        if not swapped:
            break
    return comparisons, assignments

def recursive_bubble_sort(my_list, length_mylist=None):
    if length_mylist is None:
        length_mylist = len(my_list)

    if length_mylist <= 1:
        return 0, 0

    comparisons = 0
    assignments = 0
    swapped = False

    for element in range(length_mylist - 1):
        comparisons += 1
        if my_list[element] > my_list[element + 1]:
            my_list[element], my_list[element + 1] = my_list[element + 1], my_list[element]
            assignments += 3
            swapped = True

    if not swapped:
        return comparisons, assignments  # my_listay is already sorted
    
    comp, assign = recursive_bubble_sort(my_list, length_mylist-1)
    return comparisons + comp, assignments + assign

def measure_runtime(sort_function, my_list):
    return timeit.timeit(lambda: sort_function(my_list.copy()), number=1)

nr_tests = 100
sizes = list(range(100, 10001, 100))

iterative_total_operation_list = []
recursive_total_operation_list = []

iterative_runtimes = []
recursive_runtimes = []

for current_size in sizes:
    iterative_comparisons = 0
    iterative_assignments = 0
    recursive_comparisons = 0
    recursive_assignments = 0

    iterative_runtime = 0
    recursive_runtime = 0

    for i in range(nr_tests):
        my_list = [random.randint(1, 1000) for _ in range(current_size)]

        it_comp, it_assign = iterative_bubble_sort(my_list.copy())
        iterative_comparisons += it_comp
        iterative_assignments += it_assign
        iterative_runtime += measure_runtime(iterative_bubble_sort, my_list)

        rec_comp, rec_assign = recursive_bubble_sort(my_list.copy())
        recursive_comparisons += rec_comp
        recursive_assignments += rec_assign
        recursive_runtime += measure_runtime(recursive_bubble_sort, my_list)

    iterative_total_operation_list.append(iterative_comparisons + iterative_assignments)
    recursive_total_operation_list.append(recursive_comparisons + recursive_assignments)
    iterative_runtimes.append(iterative_runtime)
    recursive_runtimes.append(recursive_runtime)

# Create a chart for the number of operations
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)  
plt.plot(sizes, iterative_total_operation_list, label='Iterative Bubble Sort')
plt.xlabel('Input Size')
plt.ylabel('Total Operations')
plt.title('Comparative Analysis - Iterative Bubble Sort (Total Operations)')
plt.legend() 

plt.subplot(2, 2, 3)  
plt.plot(sizes, recursive_total_operation_list, label='Recursive Bubble Sort')
plt.xlabel('Input Size')
plt.ylabel('Total Operations')
plt.title('Comparative Analysis - Recursive Bubble Sort (Total Operations)')
plt.legend() 

# Create a chart for runtime
plt.subplot(2, 2, 2)  
plt.plot(sizes, recursive_runtimes, label='Recursive Bubble Sort')
plt.xlabel('Input Size')
plt.ylabel('Runtime (seconds)')
plt.title('Comparative Analysis - Recursive Bubble Sort Runtime')
plt.legend() 

plt.subplot(2, 2, 4)  
plt.plot(sizes, iterative_runtimes, label='Iterative Bubble Sort')
plt.xlabel('Input Size')
plt.ylabel('Runtime (seconds)')
plt.title('Comparative Analysis - Iterative Bubble Sort Runtime')
plt.legend() 

plt.tight_layout()
plt.show()

