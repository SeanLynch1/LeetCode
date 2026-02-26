class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        

        total = 0
        # sort on attack key
        properties.sort(key= lambda x: x[0])

        print(properties)
        # we know last attack key is the highest value

        max_att = properties[-1][0]
        max_def = 0

        for i in range(len(properties)-1,-1,-1):
            
            att = properties[i][0]
            defence = properties[i][1]

            max_def = max(max_def, defence)

            if att < max_att and defence < max_def:
                print(f"incrementing total, att = {att}, def = {defence}")
                total += 1

        return total