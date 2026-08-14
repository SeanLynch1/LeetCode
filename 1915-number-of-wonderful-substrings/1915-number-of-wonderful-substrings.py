class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        
        # a = 0001
        # b = 0010

        # aabb

        # 0001
        # 0001
        # 0000
        
        # 0010
        # 0000

        # [0000, 0001, 0000, 0010, 0000]

        # aaabb

        # [0000, 0001, 0000, 0001, 0011, 0001]

        # [1, 0, 1, 0]

        # 0001, 0000, 0010, 0000

        # [0000,0001,0000,0010,0000]

        mapping = defaultdict(int)
        mapping[0] = 1
        
        vocab = defaultdict(int)
        output = 0

        curr = 1
        for letter in "abcdefghij":
            vocab[letter] = curr
            curr = curr << 1

        prefix = 0
        for letter in word:
            prefix ^= vocab[letter]

            # if we have same value
            output += mapping[prefix]

            for i in range(10):
                output += mapping[prefix ^ (1 << i)]

            mapping[prefix] += 1

        return output