class MyCircularQueue:
    def __init__(self, size: int):
        self.queue = [None]*size
        self.size = size
        self.front = -1
        self.rear = -1


    def enqueue(self, value: int) -> bool:
        if self.queue.count(None) != 0 and self.is_full() or (self.rear < self.size - 1):
            self.rear = (self.rear + 1) % self.size
        else:
            return False

        self.queue[self.rear] = value
        return True

    def dequeue(self) -> bool:
        self.front += 1
        if not self.is_empty():
            if self.front == self.size:
                self.front = 0
            self.queue[self.front] = None
            return True
        else:
            return False

    def get_front(self) -> int:
        if not self.is_empty():
            return self.queue[self.front]
        return -1

    def get_rear(self):
        if not self.is_empty():
            return self.queue[self.rear]
        return -1

    def is_empty(self):
        return self.rear == -1 and self.front == -1

    def is_full(self):
        return (self.front == self.rear and self.rear != -1) or self.rear == self.size-1


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    specific_operation = specific_operation.strip("[")
    specific_operation = specific_operation.strip("]")
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        item = item.strip("[")
        item = item.strip("]")
        if item == "":
            item = 0
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if operations[i] == "'MyCircularQueue'":
        result.append(None)
    elif operations[i] == "'enqueue'":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "'get_rear'":
        result.append(obj.get_rear())
    elif operations[i] == "'get_front'":
        result.append(obj.get_front())
    elif operations[i] == "'dequeue'":
        result.append(obj.dequeue())
    elif operations[i] == "'is_full'":
        result.append(obj.is_full())
    elif operations[i] == "'is_empty'":
        result.append(obj.is_empty())

print(result)
