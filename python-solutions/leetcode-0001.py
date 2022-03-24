# LeetCode Problem 1. Two Sum (https://leetcode.com/problems/two-sum/)
# approach explanation:
# create a dictionary that will store key-value pairs of numbers that have already been seen in the list.
# where the key is the number itself and the value is the number's index in the list.
# loop through the list and calculate the number that must be added to the current number to get the target sum.
# then check if this required number in the dictionary of all the numbers that have already been seen in the list.
# since there is always exactly one answer the function will always eventually return the indexes of the numbers that add up to the target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for curr_i, curr_num in enumerate(nums):
            required_num = target - curr_num
            if required_num in seen_nums:
                return [curr_i, seen_nums[required_num]]
            seen_nums[curr_num] = curr_i
            
