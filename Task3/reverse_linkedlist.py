class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

if __name__ == "__main__":
    # Create a LinkedList instance
    linked_list = LinkedList()
    
    # Take input from the user
    elements = list(map(int, input("Enter the elements of the linked list separated by spaces: ").split()))
    
    # Append elements to the linked list
    for elem in elements:
        linked_list.append(elem)
    
    # Print the original linked list
    print("Original linked list:")
    linked_list.print_list()
    
    # Reverse the linked list
    linked_list.reverse()
    
    # Print the reversed linked list
    print("Reversed linked list:")
    linked_list.print_list()
