class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        exp_total=n*(n+1)//2
        result=exp_total-total
        return result
        