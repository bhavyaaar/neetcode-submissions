class Solution:
    def isValid(self, s: str) -> bool:
        #queue can be used 
        #dictionary to map the opening and closing brackets
        # what gets added to stack: opening 
        # we always see an opening first and the most recent one eeds to get closed so stack works because it keeps the last(most recent) opening on top of the stack
        # we can pop it and work accordingly 

        matching = {"(":")", "{":"}", "[":"]"}
        stack = []

        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack:
                    return False
                top_element = stack.pop()
                if c != matching[top_element]:
                    return False

        return len(stack) == 0
                    






        