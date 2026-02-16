class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        vowels = set("aeiou")

        def atMost(k : int) -> int:
            
            found = defaultdict(int)
            total = 0
            left = 0

            for right in range(len(word)):

                letter = word[right]
                if letter not in vowels:
                    
                    found.clear()
                    left = right + 1
                    continue

                found[letter] += 1

                while len(found) > k:
                    l = word[left]
                    found[l] -= 1

                    if found[l] <= 0:
                        del found[l]

                    left += 1


                total += right - left + 1

            return total

        return atMost(5) - atMost(4)