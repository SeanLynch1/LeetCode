class Solution:
    def reorganizeString(self, s: str) -> str:
        
        mapping = Counter(s)
        heap = []
        word = []

        for key, val in mapping.items():

            heappush(heap, [-val, key])

        while heap:

            node_1 = heappop(heap)

            word.append(node_1[1])
            node_1[0] += 1

            if heap:
                node_2 = heappop(heap)

                word.append(node_2[1])
                node_2[0] += 1

                if node_2[0] < 0:
                    heappush(heap, node_2)

                if node_1[0] < 0:
                    heappush(heap, node_1)

        return "".join(word) if len(word) == len(s) else ""