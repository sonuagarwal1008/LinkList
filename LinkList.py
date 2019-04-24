class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()


myList = LinkedList()
#print("Inserting")
listData = [5,10,15,20,25,30,40,45,50]
for i in range(0,len(listData),1):
    myList.addNode(listData[i])




#print("Printing")
#myList.printNode()


#print(myList.head.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode.data)
#print(myList.head.nextNode.nextNode.nextNode.nextNode.nextNode.data)



print(myList.head.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode)
#myList.head.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode=myList.head.nextNode.nextNode.nextNode.nextNode.nextNode


print("loop detection")
def findLoop(myList):
    s=0
    sptr = myList.head
    fptr = myList.head

    while True:

        sptr=sptr.nextNode


        try:
            fptr = fptr.nextNode.nextNode
        except:
            if sptr == None:
                print("no loop detected")

        if sptr==fptr:
            print("loop detected")
            #print(sptr.data)
            #print(fptr.data)
            break

        else:

            s=s+1
    #print(s)

findLoop(myList)
def findLoop(myList):
    s=0
    sptr = myList.head
    fptr = myList.head

    while True:

        sptr=sptr.nextNode


        try:
            fptr = fptr.nextNode.nextNode
        except:
            if sptr == None:
                print("no loop detected")

        if sptr==fptr:
            print("loop detected")
            #print(sptr.data)
            #print(fptr.data)
            break

        else:

            s=s+1
    #print(s)

findLoop(myList)

