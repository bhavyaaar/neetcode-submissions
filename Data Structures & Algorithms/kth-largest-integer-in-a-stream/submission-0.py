class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #constructor that needs to initalzie the object 
        # turns the given inputs nums into a min heap and removes until it is k length
        self.minHeap = nums
        self.k =  k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

        

    def add(self, val: int) -> int:
        # add method which can add elements as long as they are
        self.value = val
        heapq.heappush(self.minHeap, self.value)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        
