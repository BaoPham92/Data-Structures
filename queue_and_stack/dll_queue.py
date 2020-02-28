import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# * FIFO - (First In First Out)
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        if value:
            self.storage.add_to_head(value)
        else:
            raise Exception('No valid value')

    def dequeue(self):
        if self.storage.tail != None:
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.storage.length
