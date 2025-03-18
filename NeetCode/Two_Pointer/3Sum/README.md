In 3 sum, it will have 4 possible combinations from 3 sum equal zero.


|Combinations|Example|
|---|---|
|a combination of three zeros| [0,0,0]|
|a zero with two value which pos + neg = 0| [-1,0,1]|
|two pos number and one neg number which p1 + p2 = -neg|[-3,1,2]|
|two neg number and one pos number which n1 + n2 = -pos|[-2,-1,3]|

We first need separate pos, neg, and zero to make all these combinations.
If there are more than 3 zeros in the array, there must be [0,0,0]. We can add it to the result.
Then, to reduce the time to find value, we should make a HashSet to store neg and pos so if we need to find if the value is in neg/pos, it will be faster.

After that, we need to make a nested for loop, which is in {for I,p1 in enumerate(pos)} and for p2 in pos[i+1:], which will be a two-pointer and scan all cases remain.

Lastly since it require non duplicate we can use hash to store the result (remember to change the array to tuple) and change it back to list at last
|Complexity|value|
|---|---|
|Time|O(N^2)|
|Space|O(N)|
