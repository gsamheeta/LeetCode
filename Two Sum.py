"""
        Intuition (TWO SUM):
        - We are given an **unsorted** array and need to find **two indices** such that their values sum up to a target.
        - Brute force checks all pairs — but that's O(n²) time.
        - The optimal solution uses a **hashmap** to store previously seen values and their indices.
        - For each element, we check if its **complement** (target - current) exists in the hashmap.
        - This reduces the time complexity to O(n) with O(n) space.

        Approaches:
        1. ✅ Hashmap → O(n) time, O(n) space (Best for unsorted input)
        2. ❌ Two Pointer → O(n log n) time, O(n) space (Needs sorting, loses original indices)
        3. ❌ Binary Search → O(n log n) time, O(n) space (Less intuitive and still needs sorting)
        4. ❌ Brute Force → O(n²) time, O(1) space
        """


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # ✅ Optimal Approach — Hashmap
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i

        # ------------------------------------------------
        # ❌ Two Pointer (requires sorting — modifies original indices)
        # ------------------------------------------------
        # indexed = [(val, idx) for idx, val in enumerate(nums)]
        # indexed.sort(key=lambda x: x[0])
        #
        # left, right = 0, len(indexed) - 1
        # while left < right:
        #     s = indexed[left][0] + indexed[right][0]
        #     if s == target:
        #         return [indexed[left][1], indexed[right][1]]
        #     elif s < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return []

        # ------------------------------------------------
        # ❌ Binary Search (requires sorting + slower than 2-pointer)
        # ------------------------------------------------
        # import bisect
        # indexed = [(val, idx) for idx, val in enumerate(nums)]
        # indexed.sort(key=lambda x: x[0])
        # values = [v for v, _ in indexed]
        #
        # for i, (v, orig_idx) in enumerate(indexed):
        #     complement = target - v
        #     j = bisect.bisect_left(values, complement, lo=i+1)
        #     if j < len(values) and values[j] == complement:
        #         return [orig_idx, indexed[j][1]]
        # return []

        # ------------------------------------------------
        # ❌ Brute Force
        # ------------------------------------------------
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))  # Expected: [0, 1]

    # Test Case 2
    nums = [3, 2, 4]
    target = 6
    print("Test Case 2:", sol.twoSum(nums, target))  # Expected: [1, 2]

    # Test Case 3
    nums = [3, 3]
    target = 6
    print("Test Case 3:", sol.twoSum(nums, target))  # Expected: [0, 1]

    # Test Case 4 (no valid pair)
    nums = [1, 2, 3]
    target = 7
    print("Test Case 4:", sol.twoSum(nums, target))  # Expected: None or handled error

