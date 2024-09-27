class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

if __name__ == '__main__':
    q = int(input().strip())  # Membaca jumlah query
    queue = Queue()  # Membuat objek Queue

    for _ in range(q):
        query = input().split()
        query_type = int(query[0])

        if query_type == 1:
            # Query type 1: Enqueue
            x = int(query[1])
            queue.enqueue(x)
        elif query_type == 2:
            # Query type 2: Dequeue
            queue.dequeue()
        elif query_type == 3:
            # Query type 3: Print the element at the front of the queue
            print(queue.front())
