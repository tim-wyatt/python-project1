from llnode import node


class linkedlist:

    def __init__(self):
        self.head = None
        cur_node = None
        size = 0

    def addNode(self, data):
        newNode = node()
        self.setData(data)
        newNode.next = self.cur_node
        self.cur_node = newNode
        self.incrementListSize

    def incrementListSize(self):
        self.size += 1

    def decrementListSize(self):
        self.size -= 1

    def getListSize(self):
        return self.size
