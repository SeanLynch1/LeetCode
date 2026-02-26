class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        

        properties.sort(key=lambda x: (-x[0], x[1]))
        total = 0

        print(properties)
        max_def = properties[0][1]
        
        for i in range(1, len(properties)):

            defence = properties[i][1]
            
            if defence < max_def:
                total += 1

            max_def = max(max_def, defence)

        return total