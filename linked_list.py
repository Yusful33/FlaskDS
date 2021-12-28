class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None 
        # Testing Leveraging Git
    def to_list(self):
        l = []
        if self.head is None:
            return l

        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l
    # Visual representation of the linked list
    def print_ll(self):
        ll_string = ''
        node = self.head
        # Linked list is empty
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} -> "
            node = node.next_node
        # always be an empty node at the end of the string
        ll_string += "None"
        print(ll_string)

    # Both insert at beginning and end are O(1)
    def insert_beginning(self, data):
        # If linked list is empty and keep track of linked list
        if self.head is None:
            # assigning head and last node to be the same
            self.head = Node(data, None)
            self.last_node = self.head
        new_node = Node(data, self.head)
        self.head = new_node 
    
    def insert_at_end(self, data):
        if self.head is None:
            # Will take O(n) time
            self.insert_beginning(data)
        
        # Is Unnecessary because we are keeping track of the last node
        # if self.last_node is None:
        #     print("last node is None")
        #     node = self.head
        #     # while node.next_node:
        #     #     print("iter", node.data)
        #     #     node = node.next_node

        #     node.next_node = Node(data, None)
        #     self.last_node = node.next_node
        # else:
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node
    
    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None

# ll = LinkedList()
# ll.insert_beginning("data")
# ll.insert_beginning("data")
# ll.insert_beginning("data")
# ll.insert_beginning("data")
# ll.insert_beginning("data")
# ll.insert_beginning("data")
# ll.insert_beginning("data")

# ll.insert_at_end("end")
# ll.insert_at_end("end2")
# ll.print_ll()

# ll = LinkedList()
# ll.insert_beginning("data")
# ll.insert_beginning("not data")
# ll.print_ll()

# Visual Representation
# ll = LinkedList()
# node4 = Node("data4", None)
# node3 = Node("data3", node4)
# node2 = Node("data2", node3)
# node1 = Node("data1", node2)

# ll.head = node1 
# ll.print_ll()