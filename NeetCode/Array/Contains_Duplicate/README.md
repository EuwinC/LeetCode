3 approaches have been given:

Approach 1: brute Force 
At first, we thought we could use a loop to check the numbers individually. If same is occurs, return True 
Time Complexity: O(N^2)
Space COmplexity: O(N)


Approach 2: set
we change the data structure from array to set, which has the benefit that searching in the set is O(1)
Time Complexity: O(N)
Space Complexity: O(N)

Approach 3: dictionary/collections.Counter
we change the data structure from array to dictionary(hashmap), which we store 
Time Complexity: O(N)
Space Complexity: O(N)
