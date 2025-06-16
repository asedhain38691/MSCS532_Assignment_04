import random

class Task:
    """
    Represents a single task with metadata used for scheduling.
    Lower priority value indicates higher scheduling priority.
    """
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # Defines less-than for heap comparisons
        return self.priority < other.priority

    def __repr__(self):
        return (f"Task(ID={self.task_id}, Priority={self.priority}, "
                f"Arrival={self.arrival_time}, Deadline={self.deadline})")


class MinHeapPriorityQueue:
    """
    Implements a priority queue using a binary min-heap.
    """
    def __init__(self):
        self.heap = []

    def insert(self, task):
        """
        Inserts a new task into the heap.
        Time Complexity: O(log n)
        """
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """
        Removes and returns the task with the highest priority (min-heap root).
        Time Complexity: O(log n)
        """
        if self.is_empty():
            return None
        min_task = self.heap[0]
        last = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = last
            self._heapify_down(0)
        return min_task

    def decrease_key(self, task_id, new_priority):
        """
        Decreases the priority of a given task, if found.
        Time Complexity: O(n) for search + O(log n) for heapify
        """
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                old_priority = task.priority
                task.priority = new_priority
                if new_priority < old_priority:
                    self._heapify_up(i)
                else:
                    self._heapify_down(i)
                return True
        return False  # Task not found

    def is_empty(self):
        """
        Checks whether the priority queue is empty.
        Time Complexity: O(1)
        """
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest


def simulate_task_scheduling():
    """
    Simulates scheduling of tasks using the priority queue.
    """
    pq = MinHeapPriorityQueue()

    # Generate random tasks
    for i in range(10):
        task_id = f"T{i+1}"
        priority = random.randint(1, 10)
        arrival_time = i  # Simulate sequential arrival
        deadline = arrival_time + random.randint(5, 15)
        task = Task(task_id, priority, arrival_time, deadline)
        pq.insert(task)
        print(f"Inserted: {task}")

    print("\n  Task Execution Order (By Priority) ")
    while not pq.is_empty():
        task = pq.extract_min()
        print(f"Executing: {task}")

if __name__ == "__main__":
    simulate_task_scheduling()
