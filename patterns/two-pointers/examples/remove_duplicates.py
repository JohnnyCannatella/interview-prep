#EXAMPLE - TWO POINTERS -> Same Direction
# Intuition
# If we could use extra memory, we could easily solve this by going through the list once and using a hash set to record elements we have seen. But we are not allowed extra memory so we have to look at the conditions and see if there's anything we could use. An important condition is that the numbers are sorted, which means the same numbers are next to each other. This means as we go through the list, once we see a number A, we will see all occurrences of A together, and will not see A again after we see B. Using this key observation, we can devise a fast/slow pointer solution.

# Time Complexity: O(n)

# We simply traverse the array once, moving from left to right.

# Space Complexity: O(1)

from typing import List

def remove_duplicates(arr: List[int]) -> int:
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = remove_duplicates(arr)
    print(" ".join(map(str, arr[:res])))