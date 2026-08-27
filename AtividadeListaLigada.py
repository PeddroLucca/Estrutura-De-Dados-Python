class Node:
    def __init__(self, data):
        self.data = data      # Valor do nó
        self.next = None      # Ponteiro para o próximo nó


class SingleLinkedList:
    def __init__(self):
        self.head = None      # Ponteiro para o início da lista
        self.tail = None      # Ponteiro para o final da lista (para facilitar append)
        self.size = 0         # Tamanho da lista

    def append(self, data):
        novo_no = Node(data)
        if self.head is None:
            # Lista vazia: novo nó é tanto head quanto tail
            self.head = novo_no
            self.tail = novo_no
        else:
            # Lista não vazia: liga o antigo tail ao novo nó
            self.tail.next = novo_no
            self.tail = novo_no
        self.size += 1


    def insert(self, index, data):
        novo_no = Node(data)

        if index <= 0 or self.head is None:
            novo_no.next = self.head
            self.head = novo_no
            if self.tail is None:  
               self.tail = novo_no
            self.size += 1
            return

        trav = self.head
        contador = 0
        while contador < index - 1 and trav.next is not None:
            trav = trav.next
            contador += 1

        novo_no.next = trav.next
        trav.next = novo_no

    
        if novo_no.next is None:
           self.tail = novo_no

        self.size += 1

    def __str__(self):
        """
        Retorna uma representação string da lista (ex: 5 -> 23 -> 7 -> 13).
        """
        elements = []
        trav = self.head  
        while trav:
            elements.append(str(trav.data))
            trav = trav.next
        return " -> ".join(elements)


# Criando a lista inicial: 5 -> 23 -> 7 -> 13
linked_list = SingleLinkedList()
linked_list.append(5)
linked_list.append(23)
linked_list.append(7)
linked_list.append(13)

print("Lista original:")
print(linked_list)

# Inserindo 11 na terceira posição (índice 2, entre 23 e 7)
linked_list.insert(2, 11)

print("\nLista após inserir 11 na terceira posição:")
print(linked_list)