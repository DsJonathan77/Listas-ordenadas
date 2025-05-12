
class Node:
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco
        self.next = None

class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, descricao, preco):
        new_node = Node(descricao, preco)
        current = self.head
        previous = None

        while current is not None and current.descricao < descricao:
            previous = current
            current = current.next

        if previous is None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = current
            previous.next = new_node

    def search(self, descricao):
        current = self.head
        while current is not None and current.descricao <= descricao:
            if current.descricao == descricao:
                return current
            current = current.next
        return None

    def remove(self, descricao):
        current = self.head
        previous = None
        while current is not None:
            if current.descricao == descricao:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(f"{current.descricao}: R${current.preco:.2f}")
            current = current.next
