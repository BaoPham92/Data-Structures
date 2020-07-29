class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node

    def add_to_tail(self,value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        
        head_value = self.head.value
        self.head = self.head.next
        return head_value


    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            
            current_node = current_node.next
        return False
    
    def get_max(self):
        if not self.head:
            return None
        max = self.head.value
        current = self.head.next
        while current: 
            if current.value > max:
                max = current.value
            current = current.next
        return max