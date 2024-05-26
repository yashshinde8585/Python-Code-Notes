''' 
SET
1.Collection of unordered items 
2 Group of unique value as single entity
3 insertion order is not preserved
4 slicing not work 
5 Hetrogeneous elements are allowed
6 set must be unique and immutable
7 sets -> mutable | set -> elements -> immutable 
8 set data structure is Hasheble -> inmmutable 
9 can't use index of items of items to access them since the order is always changing 
10 Using set we can perform mathematical operations
'''
set1 = {'vishal','krushna','yash','chandu','vishal'}
# print(set1)

# for name in set1:
    # print(name)

# add(): new item to be added passed in as parameter
# set1.add("Mahesh")
# print(set1)

# update(): add an item from another set or other DS
# set2 = {"mess","aksh"}
# set1.update(set2)
# print(set1)

# discard(): remove a specified item. 
# set1.discard("Mahesh")
# print(set1)

# remove(): works the same way as the discard() mehtod 

# clear(): clear all the items in the set
# set1.clear()
# print(set1) #op: set()

# set(): we can converted the list,tuple to a set. for remove duplicates items
# numList = [1,2,3,4,1,2,3,4]
# numTuple = (1,2,3,4,1,2,3,4)
# numList = set(numList)
# numTuple = set(numTuple)
# print(numList)
# print(numTuple)

# union(): able to get the union of two sets. 
# first = {1,2,3,4}
# second = {5,1,6,2,7}
# print(first.union(second))

# intersection(): items that are common both sets 
# first = {1,2,3,4}
# second = {5,1,6,2,7}
# print(first.intersection(second)) #op: {1, 2}

# difference(): all elements that are in this set but not the others
# first = {1,2,3,4}
# second = {5,1,6,2,7}
# print(first.difference(second)) #op: {3, 4}

# symmetric_difference():  all elements that are in exactly one of the sets.(either of two sets but not in both)
# first = {1,2,3,4}
# second = {5,1,6,2,7}
# print(first.symmetric_difference(second))