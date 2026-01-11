class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bank = set(bank)

        if endGene not in bank:
            return -1

        letters = "ACGT"

        begin_list = {startGene}
        end_list = {endGene}
        visited = set()

        moves = 0

        while begin_list:
            
            if len(begin_list) > len(end_list):
                begin_list, end_list = end_list, begin_list

            next_list = set()

            for word in begin_list:
                for i in range(len(word)):
                    for l in letters:

                        search_word = word[:i] + l + word[i + 1:]

                        if search_word in end_list:
                            return moves + 1

                        if search_word in bank and search_word not in visited:
                            next_list.add(search_word)
                            visited.add(search_word)
            
            moves += 1
            begin_list = next_list

        return -1



