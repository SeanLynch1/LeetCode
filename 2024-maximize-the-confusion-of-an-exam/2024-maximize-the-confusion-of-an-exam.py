class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def findSubstringOfChar(char: str) -> int:
            
            longest = 1
            left = 0
            bank = k

            for right in range(len(answerKey)):

                if answerKey[right] != char:
                    bank -= 1

                    while bank < 0:
                        if answerKey[left] != char:
                            bank += 1

                        left += 1
                    
                longest = max(longest, (right + 1) - (left))
                right += 1

            return longest

        return max(findSubstringOfChar('T'), findSubstringOfChar('F'))