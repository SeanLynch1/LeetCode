from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):

        graph = defaultdict(list)

        # Create the graph
        for r, ing_list in zip(recipes, ingredients):
            graph[r] = ing_list

        # Supplies are base solvable nodes
        supply_set = set(supplies)

        visited = {}  # 0 = unvisited, 1 = visiting, 2 = solved

        def dfs(item):
            # If supply, already solvable
            if item in supply_set:
                return True

            # If it's not a recipe and not a supply → cannot be made
            if item not in graph:
                return False

            # Cycle detected
            if visited.get(item, 0) == 1:
                return False

            # Already solved
            if visited.get(item, 0) == 2:
                return True

            visited[item] = 1

            for ing in graph[item]:
                if not dfs(ing):
                    return False

            visited[item] = 2
            return True

        result = []
        for r in recipes:
            if dfs(r):
                result.append(r)

        return result