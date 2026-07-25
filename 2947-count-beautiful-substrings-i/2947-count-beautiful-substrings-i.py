class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
        answer = 0

        # define min beautiful sub string length
        x = 1
        while (x * x) % k != 0:
            x += 1

        min_len = x * 2
        
        # k = 1, min len = 2
        # k = 2, min len = 4
        # k = 3, min len = 6
        # k = 4, min len = 4
        # k = 5, min len = 10
        # k = 6, min len = 12
        # k = 7, min len = 14
        # k = 8, min len = 8
        # k = 9, min len = 18
        # k = 10,min len = 20

        visited = defaultdict(int)
        visited[(0,0)] = 1

        vowels = {'a','e','i','o','u'}
        balance = 0

        for i in range(len(s)):
            ch = s[i]

            if ch in vowels:
                balance += 1
            else:
                balance -= 1

            remainder = (i + 1) % min_len

            answer += visited[(balance, remainder)]

            visited[(balance, remainder)] += 1


        return answer  