class Solution:
    def frequencyCount(self, arr):
        n = len(arr)+1
        hl = [0] * n 
        for i in arr:
            
            hl[i] += 1
            
        return hl[1:]
