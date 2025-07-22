"""
    Intuition:
    - We are given an array of strings and asked to group anagrams together.
    - Anagrams are words that have the same characters with the same frequency.
    - Brute force compares each string to all others — expensive with O(n² × k log k) time.
    - A better approach is to use a **hash table** and group words by a key representing their content:
        > Sorted string is one option → fast and simple
        > Character frequency count is even better → avoids sorting and offers O(k) access
    - Both hash-based methods reduce time from quadratic to linear wrt number of strings.

    Approaches:
    1. ✅ Hash Table (Char Count as Key) → O(n * k) time, O(n) space
    2. ❌ Sorting Hash Key → O(n * k log k) time, O(n) space
    3. ❌ Brute Force → O(n² * k log k) time, O(n) space
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # ✅ Optimal Approach — Character Count as Hash Key
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26  # a-z
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

        # ------------------------------------------------
        # ❌ Sort-Based Hash Key
        # ------------------------------------------------
        # res = defaultdict(list)
        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     res[sorted_s].append(s)
        # return list(res.values())

        # ------------------------------------------------
        # ❌ Brute Force
        # ------------------------------------------------
        # n = len(strs)
        # visited = [False] * n
        # result = []
        # for i in range(n):
        #     if not visited[i]:
        #         group = [strs[i]]
        #         visited[i] = True
        #         sorted_i = ''.join(sorted(strs[i]))
        #         for j in range(i + 1, n):
        #             if not visited[j]:
        #                 sorted_j = ''.join(sorted(strs[j]))
        #                 if sorted_i == sorted_j:
        #                     group.append(strs[j])
        #                     visited[j] = True
        #         result.append(group)
        # return result


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Test Case 1:", sol.groupAnagrams(strs))  
    # Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    # Test Case 2
    strs = [""]
    print("Test Case 2:", sol.groupAnagrams(strs))  
    # Expected: [[""]]

    # Test Case 3
    strs = ["a"]
    print("Test Case 3:", sol.groupAnagrams(strs))  
    # Expected: [["a"]]

    # Test Case 4
    strs = ["abc", "def", "cba", "fed"]
    print("Test Case 4:", sol.groupAnagrams(strs))  
    # Expected: [["abc", "cba"], ["def", "fed"]]
