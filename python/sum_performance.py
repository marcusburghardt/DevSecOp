# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
#
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# This is the most simple way. Good readability but not good
# for performance for large lists
def sum_of_two(nums, target):
  for first in range(0, len(nums)):
    for second in range(first+1, len(nums)):
      result = nums[first] + nums[second]
      if result == target:
        return [first,second]
  return

# According to the documentation e benchmarkets I read, 
# List Comprehensions is the fasted way to read lists. I used the same
# approach of sum_of_two, but with List Comprehensions. At least for this case
# this was the less performatic function. I didn't go deep in the libraries to
# figure out if this could be improved. Instead, I changed the approach.
# https://levelup.gitconnected.com/faster-lists-in-python-4c4287502f0a
# https://wiki.python.org/moin/PythonSpeed/PerformanceTips
def sum_of_two2(nums, target):
    # Maybe I can remove the test from here and send to a function...
    # elements = [test_sum() for first in nums for second in nums[1:]]
    elements = [[first,second] for first in nums for second in nums[1:] if first + second == target]
    if elements:
        return [nums.index(elements[0][0]),nums.index(elements[0][1])]

# Here I tried to use recursion, even knowing Python is not so optimized as C/C++
# https://www.geeksforgeeks.org/python-handling-recursion-limit/
# However, looks a good approach for this problem keeping the readability easy.
def sum_of_two3(nums, target):
    # O controls the loop by the index, since the elements are not ordered.
    index = len(nums)-1
    for n in range(0, index):
        # To avoid another look, I always compare the last element with the previous.
        if (nums[index] + nums[n]) == target:
            return [n,index]
    # Then I remove the last element of a temporary list to continue the recursion
    # until all possible elements were tested or the result was found.
    if index > 1:
        nums_temp = nums[:index]
        result = sum_of_two3(nums_temp,target)
        if result != None:
            return result
    return

# The previous function improved the performance, but I was not happy.
# I could be even better if the list was sorted. However, I can't change the
# original list. Otherwise, I would mess up the indexes. So, let's see if
# the gain of working with sorted list compensate the weight of the sort process.
def sum_of_two_sorted(sorted_list, target):
    index = len(sorted_list)-1
    # If last element is bigger than the target, obviously it will not match if
    # summed with any other element. Skip the calculations for it and go to the next.
    if sorted_list[-1] > target:
        nums_temp = sorted_list[:index]
        return sum_of_two_sorted(nums_temp,target)
    # Simple math first. Target too small.
    elif sorted_list[0] >= target:
        return
    # If the sum of the two highest elements are lower than target, we can also
    # stop and avoid unnecessary calculations.
    elif sorted_list[-1] + sorted_list[-2] < target:
        return
    # Otherwise, let's calculate. :)
    else:
        for n in range(0, index):
            sum_result = sorted_list[index] + sorted_list[n]
            if sum_result == target:
                # return the elemens. The positions are collected in the
                # caller function.
                return [sorted_list[n],sorted_list[index]]
            # The sum is happening always with the highest number and the lowest number.
            # If any result is higher than target, we can stop here and avoid more
            # unnecessary calculations.
            elif sum_result > target:
                return
    # It is necessary to reduce the list for another round?
    if index > 1:
        nums_temp = sorted_list[:index]
        return sum_of_two_sorted(nums_temp,target)
    # Match not found
    return

# Here I created a new sorted list and send to the recursive function.
# If a match is found, get the index from the original list.
def sum_of_two4(nums, target):
    sorted_list = sorted(nums)
    result = sum_of_two_sorted(sorted_list,target)
    if result:
        return [nums.index(result[0]),nums.index(result[1])]
    return

# Usually I test performance with "time" command since is the easiest way in
# Linux. However, since I was in good inspiration to learn new things, researching
# a little I found this very nice module (timeit). It is very useful.
if __name__ == '__main__':
    from timeit import timeit

    print("2 elements")
    print(timeit('sum_of_two([1,2],         3)',number=1000,setup='from __main__ import sum_of_two'))
    print(timeit('sum_of_two2([1,2],         3)',number=1000,setup='from __main__ import sum_of_two2'))
    print(timeit('sum_of_two3([1,2],         3)',number=1000,setup='from __main__ import sum_of_two3'))
    print(timeit('sum_of_two4([1,2],         3)',number=1000,setup='from __main__ import sum_of_two4'))

    print("\n3 elements")
    print(timeit('sum_of_two([3,2,4],       6)',number=1000,setup='from __main__ import sum_of_two'))
    print(timeit('sum_of_two2([3,2,4],       6)',number=1000,setup='from __main__ import sum_of_two2'))
    print(timeit('sum_of_two3([3,2,4],       6)',number=1000,setup='from __main__ import sum_of_two3'))
    print(timeit('sum_of_two4([3,2,4],       6)',number=1000,setup='from __main__ import sum_of_two4'))

    print("\n4 elements")
    print(timeit('sum_of_two([2,7,11,15],  13)',number=1000,setup='from __main__ import sum_of_two'))
    print(timeit('sum_of_two2([2,7,11,15],  13)',number=1000,setup='from __main__ import sum_of_two2'))
    print(timeit('sum_of_two3([2,7,11,15],  13)',number=1000,setup='from __main__ import sum_of_two3'))
    print(timeit('sum_of_two4([2,7,11,15],  13)',number=1000,setup='from __main__ import sum_of_two4'))

    print("\n4 elements no match")
    print(timeit('sum_of_two([2,7,11,15], 123)',number=1000,setup='from __main__ import sum_of_two'))
    print(timeit('sum_of_two2([2,7,11,15], 123)',number=1000,setup='from __main__ import sum_of_two2'))
    print(timeit('sum_of_two3([2,7,11,15], 123)',number=1000,setup='from __main__ import sum_of_two3'))
    print(timeit('sum_of_two4([2,7,11,15], 123)',number=1000,setup='from __main__ import sum_of_two4'))

    import sys
    sys.setrecursionlimit(10**6)
    print("\nbigger lists match")
    print(timeit('sum_of_two(list(range(1,1000)),1997)',number=100,setup='from __main__ import sum_of_two'))
    print(timeit('sum_of_two2(list(range(1,1000)),1997)',number=100,setup='from __main__ import sum_of_two2'))
    print(timeit('sum_of_two3(list(range(1,1000)),1997)',number=100,setup='from __main__ import sum_of_two3'))
    print(timeit('sum_of_two4(list(range(1,1000)),1997)',number=100,setup='from __main__ import sum_of_two4'))

    print("\nbigger lists no match big target")
    print(timeit('sum_of_two(list(range(1,1000)),1998)',number=100,setup='from __main__ import sum_of_two'))
    print(timeit('sum_of_two2(list(range(1,1000)),1998)',number=100,setup='from __main__ import sum_of_two2'))
    print(timeit('sum_of_two3(list(range(1,1000)),1998)',number=100,setup='from __main__ import sum_of_two3'))
    print(timeit('sum_of_two4(list(range(1,1000)),1998)',number=100,setup='from __main__ import sum_of_two4'))

    print("\nbigger lists no match tiny target")
    print(timeit('sum_of_two(list(range(1,1000)),1)',number=100,setup='from __main__ import sum_of_two'))
    print(timeit('sum_of_two2(list(range(1,1000)),1)',number=100,setup='from __main__ import sum_of_two2'))
    print(timeit('sum_of_two3(list(range(1,1000)),1)',number=100,setup='from __main__ import sum_of_two3'))
    print(timeit('sum_of_two4(list(range(1,1000)),1)',number=100,setup='from __main__ import sum_of_two4'))

    print("\nExpected results")
    print(sum_of_two4([1,2],         3))   #-> [0, 1] or [1, 0]
    print(sum_of_two4([3,2,4],       6))   #-> [1, 2] or [2, 1]
    print(sum_of_two4([2,7,11,15],  13))   #-> [0, 2] or [2, 0]
    print(sum_of_two4([2,7,11,15], 123))   #-> None
    print(sum_of_two4(list(range(1,1000)),1997))