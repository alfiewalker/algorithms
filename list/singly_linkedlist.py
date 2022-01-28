'''
Module for singly lined list definition
'''

class Node:
    '''
    Node for a singly linked list
    '''

    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class SinglyLinkedList:
    '''
    SinglyLinkedList class
    '''
    def __init__(self) -> None:
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail

    def add(self, val):
        '''
        adds a node to the head of the list
        '''
        new_node = Node(val)
        temp = self.head.next
        new_node.next = temp
        self.head.next = new_node

    def __str__(self) -> str:
        '''
        To string
        '''
        aggregate = ''
        current = self.head.next

        while current:
            if not aggregate:
                aggregate = current.val
            else:
                aggregate = f'{aggregate} -> {current.val}'
            current = current.next
        
        return aggregate
        

