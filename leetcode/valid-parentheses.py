class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = deque()
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if stack:
                    o = stack.pop()
                    if o == '(' and char != ')':
                        return False
                    elif o == '{' and char != '}':
                        return False
                    elif o=='[' and char != ']':
                        return False
                else:
                    return False #if stack empty, closing bracket
        
        if not stack:
            return True
        else:
            return False # if more opens than closing
                        
        
        #add to stack = stack.append(char to add)
        #remove from stack = stack.pop()