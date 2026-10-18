class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        curr_num = 0
        for char in s:
            if char.isdigit():
                curr_num = curr_num* 10 + int(char)
            elif char == "[":
                stack.append((string,curr_num))
                curr_num = 0
                string = ""
            elif char == "]":
                prev_str, repeat_count = stack.pop()
                string = prev_str + repeat_count*string
            else:
                string += char
        return string
