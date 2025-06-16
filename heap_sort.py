import random
import time


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def generate_sorted_array(size):
    return list(range(size))

def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

def generate_repeated_array(size):
    return [42] * size


def benchmark(name, array_gen, sort_fn, num_runs=5, size=1000):
    total_time = 0.0
    for _ in range(num_runs):
        arr = array_gen(size)
        start = time.perf_counter()
        sort_fn(arr.copy())
        end = time.perf_counter()
        total_time += (end - start)
    
    avg_time = total_time / num_runs
    print(f"{name:<25} | {sort_fn.__name__:<10} | {avg_time:.6f} sec (avg over {num_runs})")


def run_all_benchmarks():
    sizes = [1000]
    input_types = [
        ("Random", generate_random_array),
        ("Sorted", generate_sorted_array),
        ("Reverse-sorted", generate_reverse_sorted_array),
        ("Repeated", generate_repeated_array),
    ]
    sort_functions = [heapsort]

    for size in sizes:
        print(f"\nArray Size: {size}")
        print(f"{'Input Type':<25} | {'Sort':<10} | Time")
        print("-" * 60)
        for name, gen_fn in input_types:
            for sort_fn in sort_functions:
                benchmark(name, gen_fn, sort_fn, num_runs=100, size=size)

if __name__ == "__main__":
    run_all_benchmarks()
