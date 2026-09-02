class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre, suff = 1, 1

        # Initialize answer as negative infinity
        ans = float('-inf')

        # Traverse from both front and back
        for i in range(n):
            # Reset prefix if zero
            if pre == 0:
                pre = 1

            # Reset suffix if zero
            if suff == 0:
                suff = 1

            # Multiply prefix with front element
            pre *= nums[i]

            # Multiply suffix with back element
            suff *= nums[n - i - 1]

            # Update maximum product so far
            ans = max(ans, pre, suff)

        # Return the result
        return ans
