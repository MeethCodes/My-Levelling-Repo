class linkedListNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode
    
class linkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode
    
    def delete_node(self,target):
        if self.head is None:
            return
        currentNode = self.head
        if currentNode.value == target:
            self.head = currentNode.nextNode
            return
        while currentNode.nextNode is not None:
            if currentNode.nextNode.value == target:
                currentNode.nextNode = currentNode.nextNode.nextNode
                return
            currentNode = currentNode.nextNode

    def print_ll(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "-->", end=" ")
            currentNode = currentNode.nextNode
        print("None")
lol = linkedList()
lol.print_ll()
lol.insert(3)
lol.print_ll()
lol.insert(23)
lol.print_ll()
lol.insert(12)
lol.print_ll()
lol.delete_node(12)
lol.print_ll()
        

        