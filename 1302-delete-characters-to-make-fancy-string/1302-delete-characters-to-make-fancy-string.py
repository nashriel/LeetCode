class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        prev = s[0]
        stack = []
        stack.append(s[0])
        flag = False
        for c in s[1:]:
            if prev != c:
                prev = c
                stack.append(c)
                flag = False
                continue
            if flag is False:
                stack.append(c)
                flag = True
        return "".join(stack)