class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        l_value = nums[left]
        r_value = nums[right]
        mini = min(l_value, r_value)

        mid = (left + right) // 2
        while left < right:
            if nums[mid] > r_value:
                left = mid + 1
                mini = min(mini, nums[left])
                l_value = nums[left]
                mid = (left + right) // 2
            else:
                right = mid 
                mini = min(mini, nums[right])
                r_value = nums[right]
                mid = (left + right) // 2
        return mini



        