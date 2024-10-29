#LIFO - Last In First Out - елемент заходить останным але виходить першим
# - Приклад - труба з монетками
from fileinput import close


class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f"{self.stack}"

    def push(self, stack_item):
        self.stack.append(stack_item)

    def get(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        if len(self.stack) > 0:
            return False
        #else:
            #return True
        return True

new_stack = Stack()
new_stack.push("asd")
new_stack.push("kopokokopoko")
new_stack.push("an item")

print(new_stack)

new_stack.get()
print(new_stack.peek())
print(new_stack)
print(new_stack.size())
new_stack.get()
new_stack.get()
print(new_stack.is_empty())

# EnQueue - вступ у чергу
# DeQueue - виступ з черги

class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return f"{self.queue}"

    def push(self, queue_item):
        self.queue.append(queue_item)

    def get(self):
        self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        if len(self.queue) > 0:
            return False

        return True

    def size(self):
        return len(self.queue)

first_queue = ['1', '2', '3', '4']
new_Queue = Queue()
new_Queue.push(first_queue)
new_Queue.push("pokpok")
new_Queue.push("aoisdoasda")
print(new_Queue)
new_Queue.get()
print(new_Queue)