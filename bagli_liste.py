class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size=16

    def ekle(self, piece):
        new_node = Node(piece)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def sil(self, piece):
        current = self.head
        if current is not None and current.data == piece:
            self.head = current.next
            current = None
            return
        while current is not None:
            if current.data == piece:
                break
            prev = current
            current = current.next
        if current == None:
            return
        prev.next = current.next
        current = None

    def get_piece(self, row, col):
        current = self.head
        while current is not None:
            if current.data["row"] == row and current.data["col"] == col:
                return current.data
            current = current.next
        return None

    def is_solved(self):
        current = self.head
        while current is not None:
            if current.data["value"] != current.data["solution"]:
                return False
            current = current.next
        return True
