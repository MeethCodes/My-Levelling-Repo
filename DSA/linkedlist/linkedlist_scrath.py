#nodes
#1. value - any value inside that node
#2. pointer to the next node

class linkedListNode:
    def __init__(self, value, nextNode= None):
        self.value = value
        self.nextNode = nextNode

node1 = linkedListNode("1")
node2 = linkedListNode("2")

node1.nextNode = node2

currentNode = node1

while True:
    if currentNode.value == None:
        print("empty list")
        break
    print(currentNode.value, "-->",end=" ")
    if currentNode.nextNode == None:
        print("list ends here")
        break
    currentNode = currentNode.nextNode



