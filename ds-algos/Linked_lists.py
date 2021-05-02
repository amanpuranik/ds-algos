#this class represents an individual element in the linkedlist
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next #pointer to next element


class LinkedList:
    def __init__(self):
        self.head = None #points to head of linkedlist; starting point

    def insert_at_start(self,data):
        node = Node(data,self.head)
        self.head=node


    def print(self):

        #if linkedlist is blank
        if self.head is None:
            print("empty linked list")

        itr = self.head  #allows us to traverse the list starting from the head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            print(str(itr.data)) # will convert data values in list to strings and print them
            itr = itr.next #moves on to the next node

        print(llstr)


    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head

        #loop that goes through each element in the list
        while itr.next:
            itr=itr.next

        #here, there is no next element, so the reference is set to None
        itr.next = Node(data,None)

    #this method takes list of values and creats a linked list
    def insert_values(self,data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)


    #shows the length of the linked list
    def length_ll(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next # move on to the next node


    #removes element from LL based on index
    def remove_ll(self,index):
        if index == 0:
            self.head = self.head.next # the head now becomes the next element
            return

        count = 0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next #skip the linker to the next value, thus removing it
                break

            itr = itr.next
            count+=1


    # insert element into linkedlist based on the index
    def insert_LL(self,index,data):
        count = 0
        itr = self.head
        while itr:
            if count == index-1: #we want to modify the 'next' pointer of the previous element
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1







if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_values(["1","2","3"])
    ll.insert_LL(3,"4")

   # ll.remove_ll(1)

    ll.print()
