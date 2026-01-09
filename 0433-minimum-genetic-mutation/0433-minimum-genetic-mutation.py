class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        if not bank:
            return -1

        
        
        bank_map = set(bank)

        if endGene not in bank_map:
            return -1

        bank_map.add(endGene)

        letters = "ACGT"

        begin_list = {startGene}
        end_list = {endGene}
        visited = set([startGene, endGene])
        moves = 0

        while begin_list:
            
            nxt_begin_list = set()
            print(f"begin_list = {begin_list}")
            print(f"end_list = {end_list}")
            print("\n")

            if len(begin_list) > len(end_list):
                begin_list, end_list = end_list, begin_list

            for word in range(len(begin_list)):
                curr_word = begin_list.pop()
                
                for i in range(len(curr_word)):
                    for c in letters:
                        if curr_word[i] != c:

                            search_word = curr_word[:i] + c + curr_word[i + 1:]
                            
                            if search_word in end_list:
                                return moves + 1

                            if search_word in bank_map and search_word not in visited:
                                nxt_begin_list.add(search_word)
                                visited.add(search_word)
                    
                begin_list = nxt_begin_list
                moves += 1

        return -1