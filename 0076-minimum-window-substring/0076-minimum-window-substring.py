class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        chars_dict = defaultdict(int)

        for c in t:
            chars_dict[c] += 1

        char_count = len(t)

        left = 0
        seen = defaultdict(int)
        found = 0
        output = ""
        print(f"chars_dict = {chars_dict}")
        for right in range(len(s)):

            curr = s[right]
            print(f"curr = {curr}")

            if curr in chars_dict:
                
                seen[curr] += 1

                print(f"seen = {seen}, left = {s[left]}")

                if found == 0:
                    left = right
                    print(f"initializing left, left = {s[left]}")


                if seen[curr] <= chars_dict[curr]:
                    
                    found += 1

                    if found == char_count:
                        print("substring found!")
                        

                        left_char = s[left]

                        # handle duplicates
                        while left < right and s[left] == left_char and seen[left_char] > chars_dict[left_char]:
                            print(f"left = {s[left]}")
                            seen[left_char] -= 1
                            left += 1

                        while left < right and s[left] not in chars_dict:
                            left += 1
                        
                        print("removed duplicates, seen looks like -> ")
                        print(f"seen = {seen}, left = {s[left]}")


                        temp = s[left: right + 1]
                        print(f"word = {temp}")

                        output = temp if len(temp) < len(output) or output == "" else output
                        seen[s[left]] -= 1
                        print(f"After adding new word, seen looks like -> :{seen}")
                        left += 1
                        found -= 1

                        while left < right and s[left] not in chars_dict:
                            left += 1
                        
                        if left < right:
                            print(f"left = {s[left]}")

                        print(f"string = {s}")
                        print("\n")

        return output