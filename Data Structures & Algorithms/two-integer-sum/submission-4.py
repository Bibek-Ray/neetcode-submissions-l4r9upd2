class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idx_lst = []
        dct = {}
        for idx, val in enumerate(nums):
            dct[idx] = val
        new_lst = list(dct.items())
        for i in range(0, len(new_lst)):
            for j in range(i+1, len(new_lst)):
                if target-new_lst[i][1] == new_lst[j][1]:
                    idx_lst.append(i)
                    idx_lst.append(j)
                    break
        return idx_lst