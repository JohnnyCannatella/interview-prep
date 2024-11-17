# Two Pointers Pattern

## Pattern Description
- two pointer algorithm has these characteristics:
  - Two moving pointers, regardless of directions, moving dependently or independently; 
  - A function that utilizes the entries referenced by the two pointers, which relates to the answer in a way;
  - An easy way of deciding which pointer to move; 
  - A way to process the array when the pointers are moved.
- **Common Uses**: 
  - It’s commonly applied to problems involving pairs, such as pair sums, palindrome checking, or scenarios where you need to compare elements from opposite ends of a sequence.
- classification:
  - **Same direction:** 
    - the function used in this question is comparing the value of the fast pointer to its previous entry and see if they match
  - **Opposite direction:**
    - the function is comparing the sum of the entries to the desired amount. If the sum is greater, we move the larger pointer, 
    - and if the sum is lesser, we move the smaller pointer. If the sum is equal, we find our answer and we stop the program.
  - **Sliding window:**
    - we keep track of the number of characters that appear in the window. We move the later pointer, inserting the item into the set, 
    - until there is a duplicate. Then, we move the earlier pointer, removing items out of the set, until we can insert the item. We also keep track of the largest size each time for the answer.
- Note:
  - The two-pointer technique is not limited to arrays. Two pointer can be done on other structures, like linked list, as long as they are iterable.
  - Two pointers are helpful because it often offers a more efficient solution than the naive solution. (less complexity)

