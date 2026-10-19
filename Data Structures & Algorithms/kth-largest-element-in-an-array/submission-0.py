class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        #initialzie an empty minheap 
        minHeap = []
        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap) #remove smallest to make sure the heap is at k elemetns
        return minHeap[0] #then the kth element will be at the top to return 
            

        