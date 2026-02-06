# Question 1:
# change a string from snake case to camel case
# case___c__C
# notes:
# use delim, note str functions
# using example in code is good for following
# for loop range syntax is wrong
# good to see catch bugs
# know .join, .split, .pop

# naming confusion: firstWord is not clear- sawFirstWord is better
# preference, but put outputs next to code- otherwise easy to assume code is 
# doing what you THINK is doing, not what it actually is

# Now, given an array. change from snake case to camel in O(1) space


# Question 2:
# You're given movie relations for similar movies, where Movie A -> Movie B 
# if A and B are similar. You're also given the ratings for each movie. 
# Design data structures of the inputs and outputs to return the 
# top K similar movies to a movie.

# notes:
# listing out cases first is good, makes it easier to comprehend what you're 
# asking for the interviewer

# should ask to clarify as well: negative/positive/min/max of integers, 
# null/0 len/0 case- in this problem: ratings, K

# hash relations = build adjacency list - describe approach as graph

# use defaultdict since it's easier

# I like the steps outlined in the code associated with the plan
# try not to waste time on examples that are too complicated for their purpose

# note: for key value in hashmap, the syntax is for m, r in ratings.items()

# when walking through, check condition inputs 
# ie. while not stack -> check while not [1,2]
# shows how your condition is wrong

# not sure if set([movie]) does what you want it to

# if the interviewer asks for pseudocode, write the algorithm and don't code

# Question 3:
# You're given a vector of coins ie. [1, 5, 10, 25]
# Return the minimum number of coins needed to represent
# values from 1... N