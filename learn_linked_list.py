class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = None 

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next_node = b
b.next_node = c
c.next_node = d

# a -> b -> c -> d -> None

# def print_linked_list(head):
#     current = head
#     while current is not None:
#         print(current.val)
#         current = current.next_node

# print_linked_list(a)

# Recursively 
# def PrintLinkedList(head):
#     if head is None:
#         return None 
#     print(head.val)
#     #Re-running again
#     PrintLinkedList(head.next_node)

# PrintLinkedList(a)

# Traversing Through a Linked List
### Iteratively 
# def linked_list_values(head):
#     list_values = list()
#     while head is not None:
#         list_values.append(head.val)
#         head = head.next_node
#     return list_values

# values = linked_list_values(a)
# print(values)

### Recursively 
def LinkedListValues(Head):
    ListValues = list()
    FillValues(Head, ListValues)
    return ListValues

def FillValues(Head, ListValues):
    if Head is None:
        return None 
    ListValues.append(Head.val)
    #Recursively calling this function
    FillValues(Head.next_node, ListValues)

Values = LinkedListValues(a)
print(Values)