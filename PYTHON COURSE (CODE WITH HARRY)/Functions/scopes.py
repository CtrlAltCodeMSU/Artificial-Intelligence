# x = 10

# def my_function():
#     y = 20
#     print(x)  # Accessible
#     print(y)  # Accessible

# my_function()
# print(x)  # Accessible
# print(y)  # Error: y is not defined
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the pointer
        prev = current  # Move prev to the current node
        current = next_node  # Move to the next node
    head = prev  # Update the head to the new first node
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next

# Example usage:
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    print("Original Linked List:")
    print_linked_list(head)
    
    head = reverse_linked_list(head)
    
    print("Reversed Linked List:")
    print_linked_list(head)
