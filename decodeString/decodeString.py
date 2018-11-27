class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == "]":
                stack.pop()
                word = ""
                while stack[len(stack)-1] != "[":
                    word =  stack.pop() + word
                stack.pop()
                wordNum = ""
                while len(stack) > 0 and stack[len(stack)-1].isdigit():
                    wordNum = stack.pop() + wordNum    
                word = int(wordNum) * word
                stack.append(word)
        output = ""
        for element in stack:
            output = output + element
        return output


test = Solution()

print(test.decodeString("3[a]2[bc]"))
# should return aaabcbc
print(test.decodeString("3[a2[c]]"))
#should return accaccacc
print(test.decodeString("2[abc]3[cd]ef"))
#abcabccdcdcdef