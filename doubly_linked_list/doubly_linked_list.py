"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    def __len__(self):
        return self.length
    def __str__(self):
        s = ""
        cur_node = self.head
        while cur_node:
            s += f"{cur_node.value} -> "
            cur_node = cur_node.next
        s += "None"
        return s
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # Create a new node
        new_node = ListNode(value)
        # If empty list:
        if self.head is None:
        # Set self.head = new_node
            self.head = new_node
        # Set self.tail = new_node
            self.tail = new_node
        # Else:
        else:
        # Set self.head.prev = new_node
            self.head.prev = new_node
        # Set new_node.next to self.head
            new_node.next = self.head
            # Set self.head = new_node
            self.head = new_node
            # New_node.previous = none
            # just to be explicit
            new_node.prev = None
        # increment
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        old_head = self.head
        old_head.next = None
        old_head.prev = None
        self.delete(old_head)
        return old_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # Create a new node
        new_node = ListNode(value)
        # If empty list:
        if self.tail is None:
        # Set self.head = new_node
            self.head = new_node
        # Set self.tail = new_node
            self.tail = new_node
        # Else:
        else:
        # Set self.head.prev = new_node
            self.tail.next = new_node
        # Set new_node.next to self.head
            new_node.prev = self.tail
            # Set self.head = new_node
            self.tail = new_node
            # New_node.previous = none
            # just to be explicit
            new_node.next = None
        # increment
        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        tail = self.tail
        self.delete(tail)
        return tail.value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return None
        else:
            self.delete(node)
            self.add_to_head(node.value)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return None
        else:
            self.delete(node)
            self.add_to_tail(node.value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node: ListNode):
        # Check for empty pointers
        # Get previous node = node.prev
        previous_node = node.prev
        # Set prev_node.next to node.next
        if previous_node is None:
            # could just call self.remove_from_head()
            self.head = node.next
        else:
            previous_node.next = node.next
        # Next_node = node.next
        next_node = node.next
        # Set next_node.previous = previous_node
        if next_node is None:
            self.tail = node.prev
        else:
            next_node.prev = previous_node
        # Decrement length
        self.length -= 1
        # Set node.prev = None
        node.prev = None
        # Set node.next = None
        node.next = None
        # Return node.value
        return node.value
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # If length == 0 return None
        if self.length == 0:
            return None
        # If length == 1 return self.head.value
        if self.length == 1:
            return self.head.value
        # Current_max starts out as self.head.value
        current_max = self.head.value
        # Iterate through the list
        current_node = self.head
        # Stop when current_node is None
        while current_node is not None:
        # Compare current_max to each value and update current_max if value > current_max
            if current_max < current_node.value:
                current_max = current_node.value
        # Move current_node forward
            current_node = current_node.next
        # Return current_max
        return current_max