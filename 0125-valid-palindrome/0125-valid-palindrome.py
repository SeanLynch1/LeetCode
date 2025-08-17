class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = {
                    'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g',
                    'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n',
                    'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u',
                    'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z'
                    }

        left = 0
        right = len(s) -1
        output = False

        if len(s) == 1:
            return True
            
        while right > left:
            print("left = ", left)
            print("right = ", right)
            left_letter = s[left]
            right_letter = s[right]

            if left_letter.lower() not in alphabet:
                print("left_letter = ", left_letter)
                left += 1
            elif right_letter.lower() not in alphabet:
                print("right_letter = ", right_letter)
                right -= 1
            elif left_letter.lower() == right_letter.lower():
                print(left_letter.lower(), " == ", right_letter.lower())
                left += 1
                right -= 1
                output = True
            else:
                print("false")
                print("FALSE")
                return False

            print("\n")
        print("returning output")
        return output