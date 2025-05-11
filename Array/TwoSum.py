# Problem: https://neetcode.io/problems/two-integer-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexList = list(enumerate(nums))
        indexList = sorted(indexList, key=lambda x: x[1])
        print(indexList)
        i, j = 0, len(nums) - 1
        while i <= len(nums) - 1 and j >= 0:
            print(indexList[i][1], indexList[j][1])
            if indexList[i][1] + indexList[j][1] > target:
                j -= 1
            elif indexList[i][1] + indexList[j][1] < target:
                i += 1
            else:
                indexI = indexList[i][0]
                indexJ = indexList[j][0]
                if indexI <= indexJ: return [indexI, indexJ]
                else: return [indexJ, indexI]
        return None