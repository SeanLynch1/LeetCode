class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bank = set(bank)

        if endGene not in bank:
            return -1

        letters = "ACGT"

        begin_list = {startGene}
        end_list = {endGene}
        moves = 0

        while begin_list:
            
            if len(begin_list) > len(end_list):
                begin_list, end_list = end_list, begin_list

            for curr_word in begin_list:

                next_list = set()

                for j in range(len(curr_word)):
                    for l in letters:

                        search_word = curr_word[:j] + l + curr_word[ j+1:]

                        if search_word in end_list:
                            return moves + 1

                        if search_word in bank:
                            next_list.add(search_word)
                            bank.remove(search_word)
            
            begin_list = next_list
            moves += 1

        return -1



