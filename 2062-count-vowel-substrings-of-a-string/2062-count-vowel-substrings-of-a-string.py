class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        total = 0
        vowels = set("aeiou")
        found = defaultdict(int)

        left = 0
        right = 0

        while left < len(word) - 3:
            
            
            print(f"left = {left} - {word[left]}")
            print(f"right = {right} - {word[right]}")
            print(f"left to right = {word[left:right + 1]}")
            print(f"found = {found}")
            

            if word[left] in vowels:
                while right < len(word) and word[right] in vowels:
                    found[word[right]] += 1

                    if len(found) == 5:
                        print(f"found in forward check: {word[left:right + 1]}")
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

                print(f"left = {left} - {word[left]}")
                print(f"right = {right} - {word[right]}")
                print(f"left to right = {word[left:right + 1]}")
                print(f"found = {found}")
              
                while right > left and len(found) == 5:
                    found[word[right]] -= 1
                    
                    total += 1
                    print(f"found in back check : {word[left:right + 1]}")

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


            print("\n")
            
        return total