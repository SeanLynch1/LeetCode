class Solution:
    def countAnagrams(self, s: str) -> int:
        
        total = 1
        words = list(s.split(" "))
        mod = (10**9) + 7
        for word in words:
            
            mapping = defaultdict(int)
            duplicates = 1
            permutations = 1

            # find duplicates
            for i in range(len(word)):
                ch = word[i]
                mapping[ch] += 1

                duplicates *= mapping[ch]
                permutations *= len(word) - i

            inv = pow(duplicates, mod-2, mod)
            total_permutations = (permutations * inv) % mod
            total *= total_permutations
            total %= mod

            print(f"{word}'s factorial of its duplicates = {duplicates}")
            print(f"total = {int(total)}")
            
        return int(total)