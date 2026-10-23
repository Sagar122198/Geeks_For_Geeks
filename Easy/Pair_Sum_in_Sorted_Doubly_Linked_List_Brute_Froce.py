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
        temp = head
        pairs = []
        while temp is not None:
            front = temp.next
            while front is not None:
                if temp.data + front.data == target:
                    pairs.append([temp.data,front.data])
                front = front.next
            temp=temp.next
        return pairs
