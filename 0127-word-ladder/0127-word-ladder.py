class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        
        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        letters = "abcdefghijklmnopqrstuvwxyz"

        begin_list = {beginWord}
        end_list = {endWord}
        visited = set([beginWord, endWord])
        moves = 1

        while begin_list and end_list:

            if len(begin_list) > len(end_list):
                begin_list, end_list = end_list, begin_list
            
            next_list = set()
            for word in begin_list:

                for i in range(len(word)):
                    for c in letters:
                        if word[i] != c:
                            find = word[:i] + c + word[i + 1:]
                            
                            if find in end_list:
                                return moves + 1

                            if find in wordList and find not in visited:
                                next_list.add(find)
                                visited.add(find)
                
            begin_list = next_list
            moves += 1

        return 0