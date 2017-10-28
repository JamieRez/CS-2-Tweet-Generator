class Hashtable(object):
    def __init__(self):
        self.keys = []
        self.values = []
        self.size = 0


    def set(self, key, value):
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            self.values[self.keys.index(key)] = value
        self.size += 1


    def get(self, key):
        return self.values[self.keys.index(key)]


    def delete(self, key):
        del self.values[self.keys.index(key)]
        self.size -= 1


myHash = Hashtable()
myHash.set("Fruit", "Apple")
myHash.set("Candy", "Chocolate")
myHash.set("Color", "Red")
myHash.set("Flower", "Rose")
myHash.set("Fruit", "Orange")
print(myHash.get("Fruit"))
