# Create doubly link list


class Node:
    def __init__(self, data=None, prenode=None, nextnode=None):
        self.data = data
        self.prenode = prenode
        self.nextnode = nextnode


last = Node(1)
head = last

for i in range(2, 5, 1):
    node = Node(i)
    node.prenode = last
    last.nextnode = node
    last = node

print(head.nextNode.preNode.data)


#node1=Node(1)
#node2=Node(2)
#node3=Node(3)
#node1.nextNode=node2
#node2.nextNode=node3
#node2.preNode=node1
#node3.preNode=node2
#print(node1.nextNode.preNode.data)
