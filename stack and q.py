#LIFO - Last In First Out - елемент заходить останным але виходить першим
# - Приклад - труба з монетками

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f"{self.stack}"

    def push(self, stack_item):
        """
        :param stack_item: object to add at the end of the list
        :return: list with new object with index -1
        """
        self.stack.append(stack_item)

    def get(self):
        """
        :return: pop the last item (returns and deletes)
        """
        self.stack.pop()

    def peek(self):
        """
        :return: only RETURNS last item, NOT delete
        """
        return self.stack[-1]

    def size(self):
        """
        :return: size of stack (number of units)
        """
        return len(self.stack)

    def is_empty(self):
        """
        :return: True if stack is empty, False if not
        """
        if len(self.stack) > 0:
            return False
        #else:
            #return True
        return True

#FiFo - First in, First out
#ПРИклад - черга кудись

# EnQueue - вступ у чергу
# DeQueue - виступ з черги

class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return f"{self.queue}"

    def push(self, queue_item):
        """
        :param queue_item: object to add at the end of the list
        :return: object in list with index -1
        """
        self.queue.append(queue_item)

    def get(self):
        """
        :return: pop FIRST item (return and delete
        """
        self.queue.pop(0)

    def peek(self):
        """
        :return: ONLY RETURN first item (dont delete)
        """
        return self.queue[0]

    def is_empty(self):
        """
        :return: True if empty, False if not
        """
        if len(self.queue) > 0:
            return False

        return True

    def size(self):
        """
        :return: size, or lenth, or number of objects in Queue
        """
        return len(self.queue)



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

first_queue = ['1', '2', '3', '4']
new_Queue = Queue()
new_Queue.push(first_queue)
new_Queue.push("pokpok")
new_Queue.push("aoisdoasda")
print(new_Queue)
new_Queue.get()
print(new_Queue)

