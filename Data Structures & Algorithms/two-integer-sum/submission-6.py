class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idx_lst = []
        dct = {}
        for idx, val in enumerate(nums):
            dct[idx] = val
        for key, val in dct.items():
            for k, v in dct.items():
                if target-val == v and key != k:
                    idx_lst.append(key)
                    break
                
        return idx_lst