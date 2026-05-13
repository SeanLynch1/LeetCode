class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        trie = defaultdict(set)
        
        for num in nums:
            sqr_root = int(num ** 0.5)

            for i in range(2, sqr_root + 1):
                if num % i == 0:
                    val = int(num/i)

                    trie[num].add(i)
                    trie[num].add(val)
                    
                    trie[val].add(num)
                    trie[i].add(num)

        for key, val in trie.items():
            print(key, val)

        visited = set()
        self.temp_size = 0
        size = 0

        def dfs(val: int) -> None:

            if val in visited:
                return
            
            visited.add(val)
            if val in num_set:
                self.temp_size += 1

            for item in trie[val]:
                dfs(item)

        for n in nums:
            self.temp_size = 0

            if n not in visited:
                dfs(n)
                size = max(size, self.temp_size)

        return size