#!/usr/bin/env python3

class Solution(object):

    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[j] + nums[i] == target:
                    return [i, j]
                else:
                    j += 1
            i += 1


def main():
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([-1, -2, -3, -4, -5], -8))
    print(solution.twoSum([-1, -2, -3, -5, 15], 10))
    evens = [x for x in range(25198) if x % 2 == 0]
    print(evens)
    print(solution.twoSum(evens, 16021))

# Lesson: Be less confident of your solutions
# Lesson: Think of more test cases

if __name__ == "__main__":
    main()
