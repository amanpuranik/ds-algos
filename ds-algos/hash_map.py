
#this function gives you the hash values via the sum of the ASCII values of the given key
def hash_map(key):
    h = 0
    for char in key:
        h+= ord(char)

    return h%100


class HashTable:

    #init an array, where each element in the array is None
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]


    def get_hash(self,key):
        h = 0
        for char in key:
            h+= ord(char)
        return h%self.Max


    #method names are built in python operators
    #this function will add a key-value pair to the hash map
    def __setitem__(self, key, value):

        h = self.get_hash(key) #gets the hash value for the given key
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    #this function will delete items from the hash map
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None




t = HashTable()

#adding key-value pairs
t["march 8"] = 21
t["march 7"] = 20
#printing the values based on the keys
print(t["march 7"])

del t["march 7"]

print(t.arr)



