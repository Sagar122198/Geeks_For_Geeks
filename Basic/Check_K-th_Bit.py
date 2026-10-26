class Solution:
    def checkKthBit(self, n, k):
        result = ""
        while n>0:
            if n%2 == 1:
                result += "1"
            else:
                result += "0"
            n = n//2
        result = result[::-1]
        if k < len(result) and result[len(result)- 1- k] == "1":
            return True
        else:
            return False
