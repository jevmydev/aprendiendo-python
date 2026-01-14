"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
import os
os.system("clear")

def find_first_sum(nums, goal):
    range_nums = range(len(nums) - 1)

    for index in range_nums:
        num = nums[index]
        next_index = index + 1

        for compare_num in nums[next_index:]:
            total = num + compare_num

            if total == goal:
                return [index, nums.index(compare_num, next_index)]
    
    return None

nums = [4, 5, 6, 2]
goal = 8

print(find_first_sum(nums, goal))  # [2, 3]