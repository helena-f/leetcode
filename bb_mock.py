# hello

Changes to Make Anagram

Find out how close two words are to being anagrams of each other. A string s1 is an anagram of another string s2 if the same characters exist in both s1 and s2 in any order.

Write a function which accepts two strings, and returns the minimum number of letters that must be changed to make a word an anagram of another?

For example, to make 'bond' an anagram of 'down' you need to change 1 letter: 'b' to 'w'.

If either string contains a number or, the strings are different lengths return -1. Assume letters are all lowercase.


| input1 | input2 | answer |
| ------ | ------ | ------ |
| abba   | bbaa   | 0      |
| bond   | down   | 1      |
| axayy  | azzzz  | 4      |
| xxyy   | xxxx   | 2      |
| xxx1   | xxxx   | -1     |
| xxyyz  | xxxx   | -1     |
| xxyyyyyi |  xxxxyyyy | 2   |


axayy  | azzzz

counter2 = Counter(input2)
  {a:1, z: 4} 
counter2 = { a: -1, x: -1, y:-2, z: 4} 
# counter1 ={a:2, x: 1, y:2} 
for ch in input1:
    axayy
    a 
    1
    a
    y
    y

# how can we compare the two maps
# whats in it, the counts, 
# what funtionality can we use with counter
# sort, len
# abs diff


# what does it mean it's a negative vlaue?
1 + -1 
-1 + 4 = 5
1 + 1 + 2 = 4


from collections import Counter
def make_anagram(input1, input2):
    # valid input
    if len(input1) != len(input2):
        return -1
    for i in range(len(input1)):
        if not input1[i].isalpha() or not input2[i].isalpha():
            return -1

# axayy  | azzzz
    # anagram differences
    counter1 = Counter(input1) # a:1 x:1:y2 z: -4
    for ch in input2: #a z z
        if ch in counter1:
            counter1[ch] -= 1
        else:
            counter1[ch] = -1
    
    sum = 0
    for ch, count in counter1.items():
        if count > 0:
           sum += count # 1, 1, 2
    
    return sum # 4

#counters don't go negative
# dfs next, tree searches, pointers

# listen to hints
# typing proficiency good
        
