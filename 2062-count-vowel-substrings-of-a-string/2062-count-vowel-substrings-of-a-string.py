class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        total = 0
        vowels = set("aeiou")
        found = defaultdict(int)

        left = 0
        right = 0

        while left < len(word) - 3:
            
            if word[left] in vowels:
                while right < len(word) and word[right] in vowels:
                    found[word[right]] += 1

                    if len(found) == 5:
                        total += 1
                    
                    right += 1

                right -= 1

                found[word[left]] -= 1
                if found[word[left]] <= 0:
                    del found[word[left]]

                left += 1
                if left > right:
                    right = left
                    continue

                while right > left and len(found) == 5:
                    found[word[right]] -= 1
                    
                    total += 1

                    if found[word[right]] <= 0:
                        del found[word[right]]
                    else:
                        right -= 1
                
                found[word[left]] -= 1
                if found[word[left]] <= 0:
                    del found[word[left]]

                left += 1

                
            else:
                found = defaultdict(int)
                left += 1
                right = left

        return total