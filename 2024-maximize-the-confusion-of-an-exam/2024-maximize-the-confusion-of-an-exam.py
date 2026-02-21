class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        

        longest = 0
        counts = defaultdict(int)
        max_frequency = 0
        left = 0

        for right in range(len(answerKey)):

            counts[answerKey[right]] += 1
            max_frequency = max(max_frequency, counts[answerKey[right]])

            while (right + 1 - left) - max_frequency > k:
                counts[answerKey[left]] -= 1
                left += 1


            longest = max(longest, right + 1 - left)


        return longest