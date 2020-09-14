class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def print_list(self):
        output = ''
        current = self.head
        while current:
            output += f'{current.value} -> '
            current = current.next_node
        print(output)

    # def reverse_list(self, node, prev):
    #     # set initial values before iteration
    #     prev = None
    #     current = self.head

    #     # iterate through list and reverse previous and next values
    #     # create placeholder for next
    #     # set next to previous reversing the connection between the current and next node
    #     # set previous placeholder as current node to use in next iteration
    #     # set current node to the placeholder value for next to continue iteration
    #     while current is not None:
    #         next_node = current.next_node
    #         current.next_node = prev
    #         prev = current
    #         current = next_node

    #     # at the end of iteration prev placeholder's value will be the last node in regular order list
    #     # set this last node as the new head
    #     self.head = prev

    def reverse_list(self, node, prev):
        if self.head is None or self.head.next_node is None:
            return self.head
        if node.next_node:
            self.reverse_list(node.next_node, node)
        if node.next_node is None:
            self.head = node
        node.next_node = prev

ll = LinkedList()
for i in range(3):
    ll.add_to_head(i+1)

ll.print_list()

print('\n')
ll.reverse_list(ll.head, None)

ll.print_list()