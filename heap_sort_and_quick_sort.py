jimport random
import matplotlib.pyplot as plt

# QuickSort
def quicksort_best(my_list):
    def partition_best(my_list, left, right):
        middle = (left + right) // 2
        pivot_index = max(left, min(right, middle))
        pivot = my_list[pivot_index]

        my_list[pivot_index], my_list[left] = my_list[left], my_list[pivot_index]

        storedindex = left + 1
        comparisons = 0
        assignments = 0

        for item in range(left + 1, right + 1):
            comparisons += 1
            if my_list[item] <= pivot:
                assignments += 1
                my_list[storedindex], my_list[item] = my_list[item], my_list[storedindex]
                storedindex += 1

        assignments += 3
        my_list[left], my_list[storedindex - 1] = my_list[storedindex - 1], my_list[left]
        return storedindex - 1, comparisons, assignments

    stack = [(0, len(my_list) - 1)]

    comparisons = 0
    assignments = 0

    while stack:
        left, right = stack.pop()
        if left < right:
            pivot_index, comp, assign = partition_best(my_list, left, right)
            comparisons += comp
            assignments += assign

            if pivot_index - left < right - pivot_index:
                stack.append((left, pivot_index - 1))
                stack.append((pivot_index + 1, right))
            else:
                stack.append((pivot_index + 1, right))
                stack.append((left, pivot_index - 1))

    return comparisons, assignments

def quicksort(my_list):
    def partition(my_list, left, right):
        pivot = my_list[left]
        storedindex = left + 1
        comparisons = 0
        assignments = 0

        for item in range(left + 1, right + 1):
            comparisons += 1
            if my_list[item] <= pivot:
                assignments += 1
                my_list[storedindex], my_list[item] = my_list[item], my_list[storedindex]
                storedindex += 1

        assignments += 3
        my_list[left], my_list[storedindex - 1] = my_list[storedindex - 1], my_list[left]
        return storedindex - 1, comparisons, assignments

    stack = [(0, len(my_list) - 1)]

    comparisons = 0
    assignments = 0

    while stack:
        left, right = stack.pop()
        if left < right:
            pivot_index, comp, assign = partition(my_list, left, right)
            comparisons += comp
            assignments += assign

            if pivot_index - left < right - pivot_index:
                stack.append((left, pivot_index - 1))
                stack.append((pivot_index + 1, right))
            else:
                stack.append((pivot_index + 1, right))
                stack.append((left, pivot_index - 1))

    return comparisons, assignments


# Heap Sort
def heapify(my_list, length_mylist, current):
    comparisons = 0  # Initialize the comparison count
    assignments = 0  # Initialize the assignment count
    largest = current
    left = 2 * current + 1
    right = 2 * current + 2

    if left < length_mylist:
        comparisons += 1  # Increment comparison count
        if my_list[left] > my_list[largest]:
            largest = left

    if right < length_mylist:
        comparisons += 1  # Increment comparison count
        if my_list[right] > my_list[largest]:
            largest = right

    if largest != current:
        my_list[current], my_list[largest] = my_list[largest], my_list[current]
        assignments += 2  # Increment assignment count for swap
        comp, assign = heapify(my_list, length_mylist, largest)
        comparisons += comp
        assignments += assign

    return comparisons, assignments

def build_heap_bottom_up(my_list):
    length_mylist = len(my_list)
    comparisons = 0  # Initialize the comparison count
    assignments = 0  # Initialize the assignment count

    for i in range(length_mylist // 2 - 1, -1, -1):
        comp, assign = heapify(my_list, length_mylist, i)
        comparisons += comp
        assignments += assign

    return comparisons, assignments

def heap_sort(my_list):
    comparisons, assignments = 0, 0  # Initialize counters

    length_of_mylist = len(my_list)

    comp_1, assign_1 = build_heap_bottom_up(my_list)
    comparisons += comp_1
    assignments += assign_1

    for i in range(length_of_mylist - 1, 0, -1):
        comparisons += 1  # Increment comparison count
        my_list[i], my_list[0] = my_list[0], my_list[i]
        assignments += 3  # Increment assignment count for swap
        comp_2, assign_2 = heapify(my_list, i, 0)
        comparisons += comp_2
        assignments += assign_2

    return comparisons + assignments  # Return the total number of operations

# Function to generate input data for a given dimension
def generate_input_data(dim, scenario='random'):
    if scenario == 'best':
        return list(range(dim, 0, -1))
    elif scenario == 'worst':
        return list(range(dim))
    else:  # Random scenario
        return [random.randint(0, 1000) for _ in range(dim)]

# Function to measure the average number of operations for a given sorting method
def measure_average_operations(sort_func, input_data, repetitions=5):
    total_operations = 0
    for _ in range(repetitions):
        input_copy = input_data.copy()
        result = sort_func(input_copy)
        if isinstance(result, int):
            total_operations += result
        else:
            comparisons, assignments = result
            total_operations += comparisons + assignments
    return total_operations / repetitions

# Main script
n_values = list(range(100, 10001, 100))
quick_sort_random_ops = []
quick_sort_best_ops = []
quick_sort_worst_ops = []
heap_sort_random_ops = []
heap_sort_best_ops = []
heap_sort_worst_ops = []

for n in n_values:
    random_input = generate_input_data(n, 'random')
    best_input = generate_input_data(n, 'best')
    worst_input = generate_input_data(n, 'worst')
    
    # Measure the average operations for QuickSort
    quick_sort_random_avg_ops = measure_average_operations(quicksort, random_input)
    quick_sort_best_avg_ops = measure_average_operations(quicksort_best, best_input)
    quick_sort_worst_avg_ops = measure_average_operations(quicksort, worst_input)
    
    quick_sort_random_ops.append(quick_sort_random_avg_ops)
    quick_sort_best_ops.append(quick_sort_best_avg_ops)
    quick_sort_worst_ops.append(quick_sort_worst_avg_ops)
    
    # Measure the average operations for Heap Sort
    heap_sort_random_avg_ops = measure_average_operations(heap_sort, random_input)
    heap_sort_best_avg_ops = measure_average_operations(heap_sort, best_input)
    heap_sort_worst_avg_ops = measure_average_operations(heap_sort, worst_input)
    
    heap_sort_random_ops.append(heap_sort_random_avg_ops)
    heap_sort_best_ops.append(heap_sort_best_avg_ops)
    heap_sort_worst_ops.append(heap_sort_worst_avg_ops)

# Create a chart for the random scenario
plt.figure(figsize=(18, 10))

plt.subplot(2, 3, 1)  
plt.plot(n_values, heap_sort_best_ops, label='Heap Sort (Best)')
plt.xlabel('Input Dimension (n)')
plt.ylabel('Average Operations')
plt.legend()
plt.title('Comparison of Sorting Algorithms (Best-Case Scenario)')
plt.grid(True)

plt.subplot(2, 3, 2)  
plt.plot(n_values, heap_sort_random_ops, label='Heap Sort (Random)')
plt.xlabel('Input Dimension (n)')
plt.ylabel('Average Operations')
plt.legend()
plt.title('Comparison of Sorting Algorithms (Average Case - Random Scenario)')
plt.grid(True)


plt.subplot(2, 3, 3)  #
plt.plot(n_values, heap_sort_worst_ops, label='Heap Sort (Worst)')
plt.xlabel('Input Dimension (n)')
plt.ylabel('Average Operations')
plt.legend()
plt.title('Comparison of Sorting Algorithms (Worst-Case Scenario)')
plt.grid(True)


plt.subplot(2, 3, 4)  
plt.plot(n_values, quick_sort_best_ops, label='QuickSort (Best)')
plt.xlabel('Input Dimension (n)')
plt.ylabel('Average Operations')
plt.legend()
plt.title('Comparison of Sorting Algorithms (Best-Case Scenario)')
plt.grid(True)

plt.subplot(2, 3, 5)  
plt.plot(n_values, quick_sort_random_ops, label='QuickSort (Random)')
plt.xlabel('Input Dimension (n)')
plt.ylabel('Average Operations')
plt.legend()
plt.title('Comparison of Sorting Algorithms (Average Case - Random Scenario)')
plt.grid(True)

plt.subplot(2, 3, 6)  
plt.plot(n_values, quick_sort_worst_ops, label='QuickSort (Worst)')
plt.xlabel('Input Dimension (n)')
plt.ylabel('Average Operations')
plt.legend()
plt.title('Comparison of Sorting Algorithms (Worst-Case Scenario)')
plt.grid(True)

plt.tight_layout()
plt.show()
