""" Data structure that finds the median of a data stream in constant time, and adds new items to the stream in logarithmic time """"

import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            heapq.heappush(self.right, num)
            return
            
        median = self.findMedian()
        
        if num < median:
            heapq.heappush(self.left, -num)
            if len(self.left) == len(self.right) + 2:
                move_to_right = -heapq.heappop(self.left)
                heapq.heappush(self.right, move_to_right)
        
        else:    
            heapq.heappush(self.right, num)
            if len(self.right) == len(self.left) + 2:
                move_to_left = -heapq.heappop(self.right)
                heapq.heappush(self.left, move_to_left)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0])/2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
