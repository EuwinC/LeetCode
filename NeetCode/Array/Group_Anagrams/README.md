Solution 1:
Solution 1 groups anagrams by sorting each string’s characters to create a unique key in a hashmap. For example, 'eat' and 'tea' both sort to 'aet', so they’re grouped together. It processes all N strings, sorting each one of length up to K in O(K log K) time, leading to a total time complexity of O(N * K log K). The space complexity is O(N * K) to store all strings in the hashmap.

|Complexity|Big O|
|--|--|
|Time|O(N*KlogK)|
|Space|O(N)|

Solution 2:
Solution 2 groups anagrams by creating a frequency array for each string’s characters, converting it to a tuple, and using that as the hashmap key. Since anagrams have identical character counts, this works efficiently without sorting. For N strings of maximum length K, it takes O(K) per string to build the frequency array, resulting in O(N * K) time complexity. Space complexity is O(N * K) for storing the strings, with a small constant overhead for the frequency tuples.

|Complexity|Big O|
|--|--|
|Time|O(N*K)|
|Space|O(N*K)|
