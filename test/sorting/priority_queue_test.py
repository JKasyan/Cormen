import unittest
from sorting.priority_queue import PriorityQueue


class PriorityQueueTest(unittest.TestCase):

    def test_init_priority_queue(self):
        pq = PriorityQueue(lambda x, y: x > y)
        self.assertEqual(0, pq.heap_size)
        self.assertEqual(0, len(pq.heap))
        self.assertEqual(0, len(pq))

    def max_priority_queue_insert_test(self):
        pq = PriorityQueue(lambda x, y: x > y)
        pq.insert(1)
        self.assertEqual(1, len(pq))

        pq.insert(5)
        self.assertEqual(2, len(pq))
        self.assertEqual(5, pq.heap[0])

        pq.insert(4)
        self.assertEqual(3, len(pq))
        self.assertEqual(5, pq.heap[0])