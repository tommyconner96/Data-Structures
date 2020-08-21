
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next  # next node in the list


class LinkedList:
    def __init__(self):
        self.head: Node = None  # 1st node on the list
        self.tail: Node = None  # last node on the list
        self.length = 0

    def __str__(self):
        pass

    def __len__(self):
        return self.length

    # append / add --> add_to_tail
    def add_to_tail(self, value):
        # check if there is a tail
        # if no tail
        if self.tail is None:
            # create a new Node
            new_tail = Node(value, None)
            # set self.head and self.tail to the new Node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail:
        else:
            # Create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
            # Set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
            # Set self.tail to the new node
            self.tail = new_tail
        self.length += 1

    # remove head
    def remove_head(self):
        # If not head (empty list)
        if self.head is None:
            return None
        # List with one element:
        if self.head == self.tail:
            # Set self.head to current_head.next / None
            current_head = self.head
            self.head = None
            # Set self.tail to None
            self.tail = None
            # Decrement length by 1
            self.length -= 1
            return current_head.value
        # If head (General case):
        else:
            # 	Set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            #  Return current_head.value
            self.length -= 1
            return current_head.value

    # remove tail

    def remove_tail(self):
        if self.tail is None:
            return None
        elif self.head == self.tail:
            # save the current tail value
            current_tail = self.tail
            # set head and tail to none
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return current_tail.value
        else:
            current_head = self.head
            current_tail = self.tail
            while current_head.next != self.tail:
                current_head = current_head.next
            self.tail = current_head
            current_head.next = None
            self.length = self.length - 1
            return current_tail.value

    def add_to_head(self, value):
        # If no head / empty list:
        if self.head is None:
        # Create the new node with next = None
            new_node = Node(value, None)
        #  Set self.head = new node
            self.head = new_node
        # Set self.tail = new node
            self.tail = new_node
        # increment self.length
            self.length += 1
        else:
        # If head:
        # Create the new node
            new_node = Node(value, self.head)
        # New_node.next = self.head
        # Set self.head = new_node
            self.head = new_node
        # increment self.length
            self.length += 1
    def remove_at_index(self, index):
        # Remove at index i:
        # 0) Check that length > i. If not, return None
        if index >= self.length:
            return None
        if self.length == 1 and index == 0:
            target = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return target.value
        # Iterate through the loop i-1 times:
        prev_node = self.head
        for i in range(i - 1):
        # This will get us to prev_node points to the node before the target node
            prev_node = prev_node.next
        target = prev_node.next
        prev_node.next = target.next
        target.next = None
        self.length = self.length - 1
        return target.value
        