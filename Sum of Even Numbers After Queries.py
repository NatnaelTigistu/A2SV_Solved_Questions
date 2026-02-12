class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        evenSum = sum(num for num in nums if num % 2 == 0)

        for querie in queries:
            if nums[querie[1]] % 2 == 0:
                evenSum -= nums[querie[1]]
                nums[querie[1]] = nums[querie[1]] + querie[0]
                if nums[querie[1]] % 2 == 0:
                    evenSum += nums[querie[1]]
            else:
                nums[querie[1]] = nums[querie[1]] + querie[0]
                if nums[querie[1]] % 2 == 0:
                    evenSum += nums[querie[1]]
            res.append(evenSum)

        return res