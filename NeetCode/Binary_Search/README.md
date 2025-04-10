Binary Search is an algorithm that is used to search the element in the array.
The benefit of using binary search is that it could reduce the time complexity to log(N) while still having space complexity in O(1).



When can we use binary search?".
->  If we can discover some kind of monotonicity, for example, if condition(k) is True and condition(k + 1) is True, then we can consider binary search.

Decide return value. Is it return left or return left - 1?
-> after exiting the while loop, left is the minimal k​ satisfying the condition function

How to initialize the boundary variable left and right?
-> Correctly initialize the boundary variables left and right. Only one rule: set up the boundary to include all possible elements

How to update the boundary? How do you choose the appropriate combination from left = mid, left = mid + 1, and right = mid, right = mid - 1?

