class Node(object):
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def setData(self, newData):
        self.data = newData

    def getData(self):
        return self.data

    def setNext(self, newNext):
        self.nextNode = newNext

    def getNext(self):
        return self.nextNode


class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def prepend(self, newData):
        newNode = Node(newData, self.head)
        if not self.tail:
            self.tail = newNode
        self.head = newNode
        self.size += 1

    def append(self, newData):
        newNode = Node(newData)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.nextNode = newNode
            self.tail = newNode
        self.size += 1

    def find(self, d):
        currentNode = self.head
        while currentNode:
            if currentNode.data == d:
                return currentNode.data
            else:
                currentNode = currentNode.nextNode
        return None

    def delete(self, d):
        currentNode = self.head
        prevNode = None
        while currentNode:
            if currentNode.data == d:
                if prevNode:
                    if self.tail == currentNode:
                        prevNode.nextNode = None
                        self.tail = prevNode
                    else:
                        prevNode.nextNode = currentNode.nextNode
                else:
                    self.head = currentNode.nextNode
                self.size -= 1
                return True
            else:
                prevNode = currentNode
                currentNode = currentNode.nextNode
        return False


mylist = LinkedList()

mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist.head.data)  # => 'a'
print(mylist.tail.data)  # => 'c'
print(mylist.find(lambda data: data > 'b'))  # => 'c'
print(mylist.delete(1))
print(mylist.head.data)  # => 'b'
