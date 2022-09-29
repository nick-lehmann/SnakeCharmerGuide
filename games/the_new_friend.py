"""
We have a list of friends
"Charlie" is a new friend, but in the beginning she is at the end.
We all like Charlie so we put her in the middle of our friends.

1. Create a list with 4 names (Alice, Bob, Diana, Elisa)
2. Put Charlie inside the friend list
3. Move Charlie to the middle
"""

# Original friends
friends = ['Alice', 'Bob', 'Diana', 'Elisa']
print(friends)

# Charlie joins
friends.append('Charlie')
print(friends)

# Charlie is liked by everyone
friends.insert(2, friends.pop(-1))
print(friends)
