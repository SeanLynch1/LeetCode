class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        telephone = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        if len(digits) == 1:
            return list(telephone[digits[0]])
            
        max_digit_len = len(telephone[digits[0]])

        print("max digit lengt =  = ", max_digit_len)
        combinations = ["" for _ in range(max_digit_len **(len(digits)))]

        combination_len = len(combinations)

        print("combination length = ", combination_len)

        section_length = (combination_len / max_digit_len)


        # add letters
        
        for i in range(len(digits)):
            print("i = ", i)
            letter = -1
            for j in range(combination_len):
                
                if j % section_length == 0:
                    letter += 1

                if letter == len(telephone[digits[i]]):
                    letter = 0

                combinations[j] += telephone[digits[i]][letter]


            section_length = section_length / max_digit_len
            
            print("combinations = ", combinations, "\n")

        print(combinations)

        return combinations

