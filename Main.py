class MyCircularQueue:
    def __init__(self, size: int):
        self.queue = [None]*size
        self.size = size
        self.front = -1
        self.rear = -1
        self.gap = 0

    def enqueue(self, value: int) -> bool:
        if self.gap > 0:
            self.rear = 0
        if not self.is_full():
            self.rear += 1
            self.queue[self.rear] = value
            return True
        return False

    def dequeue(self) -> bool:
        if not self.is_empty():
            self.front += 1
            self.queue[self.front] = None
            self.gap += 1
            return True
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
        return self.rear == -1

    def is_full(self):
        return self.rear == self.size - 1


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
print(data)
print(operations)
for i in range(len(operations)):
    if i == 0:
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
