class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        vowels = set("aieou")

        def sumOfCombinations(k : int) -> int:
            
            distinct = defaultdict(int)
            left = 0
            total = 0

            for i in range(len(word)):

                letter = word[i]

                if letter not in vowels:
                    distinct.clear()
                    left = i + 1
                    continue

                distinct[letter] += 1

                while len(distinct) > k:
                    distinct[word[left]] -= 1

                    if distinct[word[left]] == 0:
                        del distinct[word[left]]

                    left += 1

                print(word[left: i + 1])
                total += i - left + 1

            return total


        # finds the number of combinations from word that includes all 5 vowels or less
        # find the number of combinations from word that includes max of 4 vowels or less
        # the diffence is the number of 5 vowel substrings
        return sumOfCombinations(5) - sumOfCombinations(4)