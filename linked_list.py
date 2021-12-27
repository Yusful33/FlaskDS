class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None 
        # Testing Leveraging Git

    def print_ll(self):
        ll_string = ''
        node = self.head
        # Linked list is empty
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} ->"