class Node:

    #next reference and prev reference
    def __init__(self,data,next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class LikedList:

    def __init__(self):
        self.head = None


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

    #prints list in forward direction
    def print_forward(self):
        itr = self.head
        while itr:
            print(str(itr.data))
            itr = itr.next

    def print_backward(self):

        if self.head is None:
            print("Linked list is empty")
            return

        last = self.get_last_node()
        itr = last
        while itr:
            print(str(itr.data))
            itr = itr.prev



    #gets the last node in the list
    def get_last_node(self):
        itr=self.head
        while itr.next:
            itr=itr.next

        return itr


    #this method takes list of values and creats a linked list
    def insert_values(self,data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)


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







if __name__ == '__main__':
    ll = LikedList()
    ll.insert_values(["4","1","2"])

    ll.print_backward()








