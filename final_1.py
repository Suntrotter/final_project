class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_insert(self, new_node):
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def merge_sorted_lists(self, other_list):
        merged_list = LinkedList()
        current_self = self.head
        current_other = other_list.head
        while current_self or current_other:
            if not current_self:
                merged_list.sorted_insert(Node(current_other.data))
                current_other = current_other.next
            elif not current_other:
                merged_list.sorted_insert(Node(current_self.data))
                current_self = current_self.next
            elif current_self.data <= current_other.data:
                merged_list.sorted_insert(Node(current_self.data))
                current_self = current_self.next
            else:
                merged_list.sorted_insert(Node(current_other.data))
                current_other = current_other.next
        return merged_list


# Example usage:
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

print("List 1:")
list1.print_list()
print("List 2:")
list2.print_list()

merged_list = list1.merge_sorted_lists(list2)
print("Merged sorted list:")
merged_list.print_list()
