from typing import Union

class StackNode:
    def __init__(self, child:Union[None, StackNode] = None, value=None):
        self.child = child
        self.value = value

class QueueNode:
    def __init__(self, parent:Union[None, StackNode] = None, value=None):
        self.parent = parent
        self.value = value

class Stack:

    def __init__(self):
        self.root_node = None
        self.length = 0

    def push(self, node:StackNode) -> None:
        if self.root_node != None:
            node.child = self.root_node
        self.root_node = node
        self.length += 1

    def pop(self) -> Union[StackNode, None]:
        if self.root_node != None:
            newRoot = self.root_node.child
            poped = self.root_node
            self.root_node = poped
            self.length -= 1
            return poped

    def inverse(self) -> None:
        curr_node = self.root_node
        node_stack = Stack()
        while curr_node != None:
            node_stack.push(curr_node)
            curr_node = curr_node.child
        self.root_node = None
        while node_stack.length != 0:
            self.push(node_stack.pop())

    def afficher(self) -> None:
        curr_node = self.root_node
        while curr_node != None:
            print(curr_node.value)
            curr_node = curr_node.child

class Queue:

    def __init__(self):
        self.last_node = None
        self.root_node = None
        self.__length = 0

    def enqueue(self, node:Node) -> None:
        if self.last_node == None:
            self.root_node = node
            self.last_node = node
            self.__length += 1
            return
        parent = self.last_node
        node.parent = self.last_node
        self.last_node = node
        self.__length += 1

    def dequeue(self) -> Union[QueueNode, None]:
        node = self.last_node
        if self.last_node != None:
            self.last_node = node.parent
            self.__length -= 1
        return node

    @property
    def length(self):
        return self.__length



