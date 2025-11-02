# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=rr2ss0g5
# Approach 1: Brute Force
# Time: O(n^2) | Space: O(1)

def two_sum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Approach 2: Optimized (Hash Map)
# Time: O(n) | Space: O(n)

def two_sum_optimized(nums, target):
    num_map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in num_map:
            return [num_map[diff], i]
        num_map[n] = i
