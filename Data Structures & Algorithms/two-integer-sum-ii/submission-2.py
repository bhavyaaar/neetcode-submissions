class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      #two pointers
      # the array is nondecreasing, meaning the the greater elements are going to be to the right, so if we want the value to be lower maybe move the element down?

      l = 0
      r = len(numbers) -1
      while l < r:   
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[r] + numbers[l] < target:
            l += 1
        else:
            return [l+1, r+1]
      return []
    

         

