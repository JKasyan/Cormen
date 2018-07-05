
class PriorityQueue:
    def __init__(self, s):
        self.heap = []
        self.heap_size = 0
        self.s = s

    def insert(self, el):
        self.heap.append(el)
        self.heap_size += 1
        i = self.heap_size - 1
        p = (i - 1) // 2
        while p >= 0 and self.s(self.heap[p], self.heap[i]):
            t = self.heap[i]
            self.heap[i] = self.heap[p]
            self.heap[p] = t
            i = p
            p = i // 2

    def peek(self):
        return self.heap[0]

    def pop(self):
        root = self.heap[0]
        last = self.heap.pop()
        self.heap_size -= 1
        self.heap[0] = last
        self.heapify(0)
        return root

    def heapify(self, i):
        left = 2 * i + 1
        right = left + 1
        if left < self.heap_size and self.s(self.heap[i], self.heap[left]):
            largest = left
        else:
            largest = i
        if right < self.heap_size and self.s(self.heap[largest], self.heap[right]):
            largest = right
        if largest != i:
            t = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = t
            self.heapify(i)

    def __len__(self):
        return self.heap_size

    def __str__(self):
        return str(self.heap)
