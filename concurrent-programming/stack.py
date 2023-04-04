import threading


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.lock = threading.Lock()

    def push(self, data):
        with self.lock:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        with self.lock:
            if self.head is None:
                return None
            data = self.head.data
            self.head = self.head.next
            return data

    def isEmpty(self):
        with self.lock:
            return self.head is None


if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.isEmpty())
    print(stack.pop())
    print(stack.isEmpty())
