class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count, i = 0, 0

        while (i < len(nums)):
            if (nums[i] != val):
                count += 1
                i += 1
            else:
                nums.pop(i)
        
        for j in range(len(nums) - count):
            nums.append(0)
        
        return count