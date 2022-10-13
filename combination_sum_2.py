from typing import List

class Solution:
    def find_combination(self, ind, arr, target, res, ds):
        if target == 0:
            res.append(ds.copy())
            return
        
        for i in range(ind, len(arr)):
            if i > ind and arr[i] == arr[i-1]:
                continue
            if arr[i] > target:
                break
            ds.append(arr[i])
            self.find_combination(i+1, arr, target-arr[i], res, ds)
            ds.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        data_structure = []
        self.find_combination(0, candidates, target, result, data_structure)
        return result

s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(s.combinationSum2(candidates, target))
