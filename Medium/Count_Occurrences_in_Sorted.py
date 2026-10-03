class Solution:
    def countFreq(self, arr, target):
        n = len(arr)
        low = 0
        high = n - 1
        lower_bound = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= target:
                lower_bound = mid
                high = mid - 1
            else:
                low = mid + 1

        if lower_bound == -1 or arr[lower_bound] != target:
            return 0

        low = 0
        high = n - 1
        upper_bound = n

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > target:
                upper_bound = mid
                high = mid - 1
            else:
                low = mid + 1

        return upper_bound - lower_bound
