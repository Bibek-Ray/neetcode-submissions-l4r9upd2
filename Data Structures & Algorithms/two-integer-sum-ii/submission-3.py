class Solution:
    def binSearch(self, numbers: list[int], to_search: int, left: int, right: int):
        mid = (left + right)//2
        if to_search > numbers[mid]:
            return self.binSearch(numbers, to_search, mid+1, right)
        elif to_search < numbers[mid]:
            return self.binSearch(numbers, to_search, left, mid-1)
        else:
            return mid
        
        
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        idx = []
        
        for i in range(len(numbers)):
            if (target - numbers[i]) in numbers:
                return [i+1, self.binSearch(numbers, target - numbers[i], i+1, len(numbers)-1)+1]