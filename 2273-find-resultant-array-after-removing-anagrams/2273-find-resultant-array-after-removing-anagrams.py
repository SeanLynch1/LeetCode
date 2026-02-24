class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        output = [words[0]]
        prev_arr = [0] * 26

        for ch in words[0]:
            prev_arr[ord(ch) - ord('a')] += 1

        for i in range(1, len(words)):
            
            word = words[i]
            arr = [0] * 26

            for ch in word:
                arr[ord(ch) - ord('a')] += 1

            if arr != prev_arr:
                output.append(word)
            
            prev_arr = arr

        return output