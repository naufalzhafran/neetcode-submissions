class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0 , len(numbers) - 1

        while i < j:
            currsum = numbers[i] + numbers[j]
            if currsum < target:
                i += 1
                continue
            elif currsum > target:
                j -= 1
                continue
            else:
                return [i + 1, j + 1]


        return [i + 1, j + 1]