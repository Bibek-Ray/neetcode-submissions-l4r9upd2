from collections import defaultdict

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idx_lst = []
        diff_dct = defaultdict(list)
        k = 0
        dct = {}
        for idx, val in enumerate(nums):
            dct[idx] = val
            diff_dct[target - val].append(idx)
        for key, val in dct.items():
            if val in diff_dct.keys():
                if len(diff_dct[val]) != 2:
                    if val in diff_dct.keys() and diff_dct[val][0] != key:
                        idx_lst.append(key)
                else:
                    if val * 2 == target:
                        idx_lst.append(key)
 
        return idx_lst