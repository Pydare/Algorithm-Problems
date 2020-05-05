class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = 0
        self.values = dict()   # Key: [value, HowRecentAccessed]
        
    def get(self, key: int) -> int:
        
        if key in self.values.keys():
            val = self.values[key]
            val[1] = self.counter+1
            self.counter +=1
            self.values[key] = val
            return val[0]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if len(self.values) < self.capacity or key in self.values.keys():
            val = [value, self.counter]
            self.counter +=1
            self.values[key] = val
        else:
            mn = min(self.values.items(), key = lambda x: x[1][1])[0]
            del self.values[mn]
            val = [value, self.counter]
            self.counter +=1
            self.values[key] = val
        

cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
cache.get(1)
cache.put(3, 3)
r = cache.get(2)
print(r)