
class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    #

    def add_child(self,data):
        if data == self.data: #check if value already exists in tree
            return

        if data <self.data: #should go on the left side then

            if self.left: #check if left tree has a value
                self.left.add_child(data) #if it has a value, use add_child method to add another child to the left
            else: #if it does not have a value
                self.left = BST(data)


        else:
            if self.right:
                self.right.add_child()
            else:
                self.right = BST(data) #if there is no right tree, init a new right tree with data


    #visit left, root then right
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data) #append the root

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


    #search for an element in the tree
    def search_element(self, val):
        if self.data == val:
            return True

        if val < self.data: #might be on left side
            if self.left:
                return self.left.search_element(val) #call method again; recursion
            else:
                return False


        if val > self.data: #might be on right side
            if self.right:
                return self.right.search_element(val)
            else:
                return False

    def max_element(self):
        if self.right is None:
            return self.data
        return self.right.max_element()#recursive

    def min_element(self):
        if self.left is None:
            return self.data
        return self.left.min_element() #recursive call

    def delete_val(self,val): #delete a value in the tree
        if val <self.data:
             if self.left:
                 self.left.delete_val(val)

        elif val >self.data:
            if self.right:
                self.right.delete_val(val) #recursive call


        else:
            if self.left is None and self.right is None: #only one single node exists
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.min_element()
            self.data = min_val #value is replaced with the the min of the right sub tree, thus deleting it
            self.right = self.right.delete_val(min_val)

        return self











def build_tree(data):
    root = BST(data[0])

    for i in range(1,len(data)):
        root.add_child(data[i])
    return root

if __name__ == '__main__':
    numbers = [12,3,1,20,5]
    numbers_tree = build_tree(numbers)

    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search_element(5))

    numbers_tree.delete_val(1)

    print(numbers_tree.in_order_traversal())













