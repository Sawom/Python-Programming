class queue:
    def __init__(self):
        self.item = []

    def enqueue(self,item):
        self.item.append(item)

    def dequeue(self):
        return self.item.pop(0)

    def is_empty(self):
        if self.item == []:
            return True
        return False

if __name__ == "__main__":
    q = queue()
    q.enqueue("tamim")
    q.enqueue("sakib")
    q.enqueue("riad")
    q.enqueue("mashrafee")
    q.enqueue("sawom")
    q.dequeue()
    q.dequeue()

    while not q.is_empty():
        item = q.dequeue()
        print(item)