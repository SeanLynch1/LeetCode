class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        words_dict = Counter(words)
        output = []

        for offset in range(word_len):
            left = offset
            seen = defaultdict(int)
            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right+word_len]
                if word in words_dict:
                    seen[word] += 1
                    while seen[word] > words_dict[word]:
                        left_word = s[left:left+word_len]
                        seen[left_word] -= 1
                        left += word_len
                    if right - left + word_len == total_len:
                        output.append(left)
                else:
                    seen.clear()
                    left = right + word_len

        return output
