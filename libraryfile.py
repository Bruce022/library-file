class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def addAtFront(self, data):
        """Add a node at the front of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def addAtEnd(self, data):
        """Add a node at the end of the list."""
        new_node = Node(data)
        if not self.tail:  # If the list is empty
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def removeFromFront(self):
        """Remove a node from the front of the list."""
        if not self.head:  # If the list is empty
            print("List is empty!")
            return None
        removed_data = self.head.data
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.count -= 1
        return removed_data

    def removeFromEnd(self):
        """Remove a node from the end of the list."""
        if not self.tail:  # If the list is empty
            print("List is empty!")
            return None
        removed_data = self.tail.data
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.count -= 1
        return removed_data

    def print(self):
        """Print the elements of the list."""
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("List:", " <-> ".join(map(str, elements)))

    def size(self):
        """Return the size of the list."""
        return self.count

# Example usage
if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.addAtFront(10)
    dll.addAtFront(20)
    dll.addAtEnd(30)
    dll.print()  # Output: List: 20 <-> 10 <-> 30
    print("Size:", dll.size())  # Output: Size: 3
    print("Removed from front:", dll.removeFromFront())  # Output: Removed from front: 20
    dll.print()  # Output: List: 10 <-> 30
    print("Removed from end:", dll.removeFromEnd())  # Output: Removed from end: 30
    dll.print()  # Output: List: 10
    print("Size:", dll.size())  # Output: Size: 1
