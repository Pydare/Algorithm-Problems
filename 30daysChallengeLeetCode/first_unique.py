class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums #nums is a list
        self.d = {}     #d is a hash-table
        self.setHashTable()
        
    def setHashTable(self):
        for i in range(len(self.nums)):
            if self.d.get(self.nums[i],None) is None:
                self.d[self.nums[i]] = 1
            else:
                self.d[self.nums[i]] += 1
            
    def showFirstUnique(self) -> int:
        for i in range(len(self.nums)):
            if self.d[self.nums[i]] == 1:
                return self.nums[i]
        else:
            return -1
        
    def add(self, value: int) -> None:
        self.nums.append(value)
        if self.d.get(value,None) is None:
            self.d[value] = 1
        else:
            self.d[value] += 1
        

obj = FirstUnique([2,3,5])
obj.add(5)
obj.add(2)
obj.add(3)
ans = obj.showFirstUnique()
print(ans)