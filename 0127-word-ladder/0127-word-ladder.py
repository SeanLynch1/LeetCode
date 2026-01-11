class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        word_list = set(wordList)

        if endWord not in wordList:
            return 0

        letters = 'abcdefghijklmnopqrstuvwxyz'
        begin_list = {beginWord}
        end_list = {endWord}

        visited = set([beginWord, endWord])
        moves = 1

        while begin_list:

            if len(begin_list) > len(end_list):
                begin_list, end_list = end_list, begin_list

            # simulates a queue
            next_list = set()

            for word in begin_list:

                for i in range(len(word)):
                    for l in letters:

                        search_word = word[:i] + l + word[i + 1:]

                        if search_word in end_list:
                            return moves + 1

                        if search_word in word_list and search_word not in visited:
                            next_list.add(search_word)
                            visited.add(search_word)

            moves += 1
            begin_list = next_list

        return 0