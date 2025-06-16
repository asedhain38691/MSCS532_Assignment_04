# Heap Sort Benchmark Suite

This project benchmarks heap sort algorithm:

The benchmarks compare performance across different types of input arrays to analyze best-case, average-case, and worst-case behaviors.

---

## 📂 Benchmark Scenarios

The benchmark tests against the following input types:

1. **Random Array** — Elements are randomly shuffled integers.
2. **Sorted Array** — Increasing order; worst-case for deterministic Quicksort.
3. **Reverse-Sorted Array** — Decreasing order; also worst-case for deterministic Quicksort.
4. **Repeated Elements** — All elements are the same.

Each benchmark was run 100 times on arrays of size 1000.

---

## 📈 Summary of Results

| Input Type       | Heapsort (ms) | Quicksort (ms)         | Merge Sort (ms) |
|------------------|----------------|--------------------------|------------------|
| Random           | 0.919          | ~0.6                     | ~0.8             |
| Sorted           | 0.977          | ~1.5 (worst case)        | ~0.8             |
| Reverse-sorted   | 0.795          | ~1.5 (worst case)        | ~0.8             |
| Repeated         | 0.140          | ~0.7                     | ~0.8             |


> **Interpretation:**
> Quicksort: Faster than Heapsort in random input scenarios due to lower constant factors. However, without randomized pivot selection, its performance degrades on sorted or reverse-sorted inputs O(n^2 ). This was observed in the higher runtimes.
> Merge Sort: Consistent O(n log n ) performance across all distributions. It is not in-place (requires O(n) space), which can be a disadvantage for memory-constrained systems.
> Heapsort: Maintains consistent performance across all input types, validating the theoretical guarantee of O(n log n ) in all cases. However, it tends to be slower in practice due to the overhead of repeated swaps and poorer cache performance.


---

## 🚀 How to Run

```
python3 heap_sort.py
```


# Priority Query Scheduling


## 🚀 How to Run

```
python3 priority_queue.py
```
