class Solution:
    def search(self, nums, target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        start, end = 0, n-1
        
        while start <= end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                return True
            if not self.is_binary_search_helpful(nums,start,nums[mid]):
                start += 1
                continue
            #which array does pivot belong to
            pivot_array = self.exists_in_first(nums,start,nums[mid])
            
            #which array does target belong to
            target_array = self.exists_in_first(nums,start,target)
            
            #If pivot and target exist in different sorted arrays, recall that xor is true when both                 operands are distinct
            if pivot_array ^ target_array:
                if pivot_array:
                    #pivot is in first, target is in second
                    start = mid+1
                else:
                    end = mid-1
                    
            else:
                #If pivot and target exist in same sorted array
                if nums[mid] < target:
                    start = mid+1
                else:
                    end = mid-1
                    
        return False
    
    #returns true if we can reduce the search space in current binary search space
    def is_binary_search_helpful(self,arr,start, element):
        return arr[start] != element
    
    #returns true if element exists in first array, false if it exists in second
    def exists_in_first(self,arr,start,element):
        return arr[start] <= element
