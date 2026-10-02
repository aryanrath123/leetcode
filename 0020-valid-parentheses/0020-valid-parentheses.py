class Solution(object):
    def isValid(self, s):

        stack = []

        for ch in s:
            # opening brackets
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            # closing brackets
            else:
                if not stack:
                    return False

                top = stack.pop()

                if (ch == ')' and top != '(') or (ch == '}' and top != '{') or (ch == ']' and top != '['):
                    return False

        return len(stack) == 0