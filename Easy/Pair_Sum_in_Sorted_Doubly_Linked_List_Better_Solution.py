# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        my_set = set()
        temp = head
        result = []
        while temp is not None:
            remaining = target - temp.data
            if remaining in my_set:
                result.append([remaining,temp.data])    
            my_set.add(temp.data)
            temp=temp.next
        return result
