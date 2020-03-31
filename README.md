# simple-interleaving
Recursion practice demonstrating simple interleaving of user input in Python

***PROMPT***

Picking one letter from string 1 (str1) in each recursive call until there is no letter remaining in string 1; then keep picking one letter from string 2 (str2) in each recursive call until there is no letter remaining in string 2.

Example:

(str1 = AB, str2 = MN, interleave ="“)
 
1. Pick one character from str1 and put it in interleave string
(str1 = B, str2 = MN, interleave ="A")

2. Check if there is any character remaining in String 1: Yes, repeat Step 1.
(str1 = , str2 = MN, interleave ="AB")

No more characters remaining in String 1, now repeat Step 1 for String 2 until is empty.
(str1 =  , str2 = N, interleave ="ABM")
(str1 =  , str2 = , interleave ="ABMN")

The interleave string length became 4 that is str1.length + str2.length;  This is the first interleave string, display it on the screen.

Recursive call will be returned and reach at step where call for character B will be completed.
(str1 = B, str2 = MN, interleave ="A")
Since call for B is completed, now it will pick a letter from string 2 and next call will be.

(str1 = B, str2 = N, interleave ="AM") and it continues.
