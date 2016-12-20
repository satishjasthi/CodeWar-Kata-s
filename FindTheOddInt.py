#Details:Given an array, find the int that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

#my first attempt code :)
def find_it(l):
	return([number for number in l if (l.count(number)%2 != 0)][0])

#a = find_it([1,1,5,3,3,6,5,3,6,6,6]);print(a)

#other amazing solutions:

import operator

def find_it(xs):
    return reduce(operator.xor, xs)

from collections import Counter
def find_it(l):
    return [k for k, v in Counter(l).items() if v % 2 != 0][0]

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
