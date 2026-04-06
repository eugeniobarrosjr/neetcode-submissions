# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs

        middle = (start + end) // 2

        self.mergeSortHelper(pairs, start, middle)
        self.mergeSortHelper(pairs, middle + 1, end)
        self.merge(pairs, start, middle, end)

        return pairs
    
    def merge(self, array, start, middle, end):
        left = array[start : middle + 1]
        right = array[middle + 1: end + 1]

        i = 0 # index for left
        j = 0 # index for right
        k = start # index for array

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

            

