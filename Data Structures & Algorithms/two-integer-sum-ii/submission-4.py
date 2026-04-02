class Solution:
    def binSearch(self, numbers: list[int], to_search: int, left: int, right: int):
        mid = (left + right)//2
        if left <= right:
            if to_search > numbers[mid]:
                return self.binSearch(numbers, to_search, mid+1, right)
            elif to_search < numbers[mid]:
                return self.binSearch(numbers, to_search, left, mid-1)
            else:
                return mid
        else:
            return 0
        
        
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        for i in range(len(numbers)):
            if (numbers[i] + numbers[self.binSearch(numbers, target - numbers[i], i+1, len(numbers)-1)]) == target:
                return ([i+1, self.binSearch(numbers, target - numbers[i], i+1, len(numbers)-1)+1])