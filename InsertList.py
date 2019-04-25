class Node:
	def __init__(self, data=None, nextNode=None):
		self.data=data
		self.nextNode=nextNode
class LinkList:
	def __init__(self, head=None):
		self.head=head
	
	def createList(self,data):
		node=Node(data,self.head)
		self.head=node
	def printNode(self):
		cur = self.head
		while cur:
			print cur.data
			cur=cur.nextNode
	def insertList(self,pos,item):
		node=Node(item)
		ptr=self.head
		head=ptr
        	if pos==0:
			print "position zero doesn't exist"
                	return head
        	elif pos==1:
			print "first position"
                	node.nextNode=ptr
			self.head=node
                	return head
        	else:
                	for i in range(1,pos+1,1):
                        	if i<pos:
                                	#if ptr.nextNode==None and i+1==pos:
                                #       print "end of the list"
                                	if ptr.nextNode==None and i+1<pos:
                                        	print "out of index"
                                        	break

                                #if ptr.nextNode!=None:
                                	else:
                                        	#print "i value=" + str(i)
                                        	q=ptr
                                        	ptr=ptr.nextNode

                	q.nextNode=node
                	node.nextNode=ptr
               		return head
	
def main():
	myList=LinkList()
	for i in range(1,5,1):
		myList.createList(i)
	pos=1
	item=20
	ptr=myList.insertList(pos,item)
	myList.printNode()
#print ptr.nextNode.nextNode.nextNode.nextNode.data
#print pitr.data

main()
