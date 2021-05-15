#this folder will tackle the problem of collisions

class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)] #init an array will solve collisions

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash+=ord(char)
        return hash % self.max

    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        in_arr = False

        #enumerate and see if key already exists in the list
        for index, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][index] = (key,value)
                in_arr = True

            if not in_arr:
                self.arr[h].append((key,value))





        self.arr[h].append((key,value))


    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]): #locates the list in the map and goes through said list
            if kv[0] == key:
                del self.arr[h][index]






#march 6 and march 17 have same index


ht = HashTable()
ht.__setitem__("march 6", 230)
ht.__setitem__("march 17", 231)

print(ht["march 6"]) # will just give me a value of 230 instead of 2d array

#2d array in some parts of the map
print(ht.arr)

ht.__delitem__("march 17")

print(ht.arr)






