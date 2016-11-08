class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def printAllVals(self):
        currentNode = self.head
        while(currentNode.next is not None):
            print currentNode.value
            currentNode = currentNode.next
        print currentNode.value
        return self

    def addBack(self, val):
        currentNode = self.head
        while(currentNode.next is not None):
            currentNode = currentNode.next
        currentNode.next = Node(val)
        return self

    def addFront(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        return self

    def insertBefore(self, nextVal, val):
        currentNode = self.head
        while(currentNode.next is not None):
            if (currentNode.next.value == nextVal):
                newNode = Node(val)
                newNode.next = currentNode.next
                currentNode.next = newNode
                return self
            currentNode = currentNode.next
        return self

    def insertAfter(self, preVal, val):
        currentNode = self.head
        while (currentNode.next is not None):
            if (currentNode.value == preVal):
                newNode = Node(val)
                newNode.next = currentNode.next
                currentNode.next = newNode
                return self
            currentNode = currentNode.next
        return self

    def removeNode(self, val):
        currentNode = self.head
        while (currentNode.next is not None):
            if (currentNode.next.value == val):
                if (currentNode.next.next.value is None):
                    currentNode.next = None
                else:
                    currentNode.next = currentNode.next.next
            currentNode = currentNode.next
        return self

    def reverseList(self):
        prev = None
        currentNode = self.head
        while (currentNode is not None):
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next
        self.head = prev


list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')

list.reverseList()
list.printAllVals()
