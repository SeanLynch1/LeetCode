class Solution:
    def strStr(self, haystack, needle):

        result = -1

        for i in range(len(haystack)):
            print(i)
            print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return result