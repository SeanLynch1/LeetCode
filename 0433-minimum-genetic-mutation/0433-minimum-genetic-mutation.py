class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bank = set(bank)

        if endGene not in bank:
            return -1

        letters = "ACGT"

        queue = deque([startGene])
        moves = 0

        while queue:

            for i in range(len(queue)):
                curr_word = queue.popleft()

                for j in range(len(curr_word)):
                    for l in letters:

                        search_word = curr_word[:j] + l + curr_word[j+1:]

                        if search_word == endGene:
                            return moves + 1

                        if search_word in bank:
                            queue.append(search_word)
                            bank.remove(search_word)
            
            moves += 1

        return -1



