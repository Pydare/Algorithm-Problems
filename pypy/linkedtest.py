class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class Linkedlist:
    def __init__(self):
        self.start = None
    def insert(self, value):
        temp = Node(value)
        
        temp.link = self.start
        self.start = temp

    #add the contents of 2 linked lists 
    # and return the node of the result list
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        #while both list exist
        while (first is not None or second is not None):
            fdata = 0 if first is None else first.info
            sdata = 0 if second is None else second.info
            Sum = carry + fdata + sdata

            #update carry for next calculation
            carry = 1 if Sum >= 10 else 0

            #update sum if it is greater than 10
            Sum = Sum if Sum < 10 else Sum % 10 

            #create a new node with sum as data
            temp = Node(Sum)
            
            #if this is the first node, 
            #set it as the head of the resultant list
            if self.start is None:
                self.start = temp
            else:
                prev.link = temp
            
            #set prev for next insertion
            prev = temp

            #move first and second pointers to next nodes
            if first is not None:
                first = first.link
            if second is not None:
                second = second.link

        if carry > 0:
            temp.link = Node(carry)

    def printList(self):
        temp = self.start
        while (temp):
            print(temp.info),
            temp = temp.link

first = Linkedlist()
second = Linkedlist()

#create first list
first.insert(6)
first.insert(4)
first.insert(9)
first.insert(5)
first.insert(7)
print('The first list is ', first.printList())

#create second list
second.insert(4)
second.insert(8)
print('The second list is ', second.printList)

#add the two lists and see results
res = Linkedlist()
res.addTwoLists(first.start, second.start)
print('Result list is ')
res.printList()





    