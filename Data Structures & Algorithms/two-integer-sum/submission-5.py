class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idx_lst = []
        dct = {}
        for idx, val in enumerate(nums):
            dct[idx] = val
        dct_up = dict(sorted(dct.items(), key = lambda item:item[1]))
        for key, val in dct.items():
            for k, v in dct_up.items():
                if target-val == v and key != k:
                    idx_lst.append(key)
                    break
                
        return idx_lst