class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while s[j].isdigit():
                    j += 1
                stack.append(s[i:j])
                i = j
            if s[i] == "]":
                curr = deque()
                while not stack[-1].isdigit():
                    curr.appendleft(stack.pop())
                count = int(stack.pop())
                stack.append("".join(curr) * count)
            if s[i] not in "[]":
                stack.append(s[i])
            i += 1
        
        return "".join(stack)