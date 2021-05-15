#this class is meant for building the attributes of the tree
class TreeNode:

    #initalise various attributes of the tree
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

     #add child node
    def add_child(self,child):
        child.parent = self #the parent of the child is self
        self.children.append(child) #add to the self.children list


    #recursion in use here
    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Fruits") #will be stores in self.data of the treenode
                                  # fruits becomes the parent element

    apple = TreeNode("Apple") #apple becomes the child element now
    apple.add_child(TreeNode("green apple"))
    apple.add_child(TreeNode("red apple")) #these are children element of the apple node

    mango = TreeNode("Mango") #another child element of fruits
    mango.add_child(TreeNode("ripe mango"))
    mango.add_child(TreeNode("sweet mango"))

    #adding the apple and mango nodes as children to the root of the tree
    root.add_child(apple)
    root.add_child(mango) #this piece of code gives me the memory allocation

    root.print_tree()
if __name__ == '__main__':
    build_product_tree()









