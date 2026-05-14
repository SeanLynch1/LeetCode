class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        alphabet = defaultdict(str)

        for i in range(len(order)):
            alphabet[order[i]] = i

        print(alphabet)


        for i in range(1, len(words)):
            
            left = words[i - 1]
            curr = words[i]

            idx = 0
            print(f"left = {left}, curr = {curr}")
            while idx < len(left) and idx < len(curr):
                print(f"idx = {idx}")
                left_letter = left[idx]
                curr_letter = curr[idx]

                if alphabet[left_letter] > alphabet[curr_letter]:
                    return False
                elif alphabet[left_letter] < alphabet[curr_letter]:
                    break
                idx += 1
            
            if curr == left[:len(curr)] and len(left) > len(curr):
                return False


        return True