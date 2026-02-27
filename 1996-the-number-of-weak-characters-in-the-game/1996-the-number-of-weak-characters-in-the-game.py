class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        total = 0

        properties.sort(key = lambda x: (-x[0], x[1]))
        last_defc = properties[0][1]

        max_defc = last_defc

        for i in range(1, len(properties)):
            defc = properties[i][1]

            if defc < max_defc:
                total += 1

            max_defc = max(max_defc, defc)

            
        return total