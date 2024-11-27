class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self, data_list):
        for data in data_list:
            self.add_node_end(data)

    def add_node_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add_node_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_node_at_index(self, index, data):
        if index == 0:
            self.add_node_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if not current:
            print("Index out of bounds")
            return
        new_node.next = current.next
        current.next = new_node

    def remove_node_beginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def remove_node_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def remove_node_at_index(self, index):
        if not self.head:
            print("List is empty")
            return
        if index == 0:
            self.remove_node_beginning()
            return
        current = self.head
        count = 0
        while current.next and count < index - 1:
            current = current.next
            count += 1
        if not current.next:
            print("Index out of bounds")
            return
        current.next = current.next.next

    def print_linked_list(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Menu-driven program
linked_list = LinkedList()

while True:
    print("\nMenu:")
    print("1. Create linked list")
    print("2. Add node at the beginning")
    print("3. Add node at the end")
    print("4. Add node at a specific index")
    print("5. Remove node from the beginning")
    print("6. Remove node from the end")
    print("7. Remove node from a specific index")
    print("8. Display linked list")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data_list = list(map(int, input("Enter elements separated by space: ").split()))
        linked_list.create_linked_list(data_list)
    elif choice == 2:
        data = int(input("Enter data: "))
        linked_list.add_node_beginning(data)
    elif choice == 3:
        data = int(input("Enter data: "))
        linked_list.add_node_end(data)
    elif choice == 4:
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))
        linked_list.add_node_at_index(index, data)
    elif choice == 5:
        linked_list.remove_node_beginning()
    elif choice == 6:
        linked_list.remove_node_end()
    elif choice == 7:
        index = int(input("Enter index: "))
        linked_list.remove_node_at_index(index)
    elif choice == 8:
        linked_list.print_linked_list()
    elif choice == 9:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
