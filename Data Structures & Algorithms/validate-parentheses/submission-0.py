class Solution:
    def isValid(self, s: str) -> bool:
        # a stack would be helpful here becasue it is LIFO
        # along with a hashmap that maps each opening and closing bracket 
        # once we have this we push any opening bracket to the stack
        # pop whenever we see a closing and compare becasue the order matters 


        stack = [] #stacks are implemented as lists under the hood 
        parantheses = {'{':'}', '(':')', '[':']'}

        for i in s:
            if i in parantheses:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if parantheses[top] != i:
                        return False
                    else:
                        continue

        return len(stack) == 0




        



        