class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        output = []
        mapping = defaultdict(list)
        visited = defaultdict(int)
        supplies = set(supplies)

        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                mapping[recipes[i]].append(ingredient)

        def traverse_recipes(item: str) -> bool:
            
            if item in supplies:
                return True

            if item not in mapping:
                return False

            if visited[item] == 1:
                return False

            if not mapping[item] or visited[item] == 2:
                visited[item] = 2
                return True

            visited[item] = 1

            for ingredient in mapping[item]:

                if traverse_recipes(ingredient):
                    visited[ingredient] = 2
                else:
                    return False

            visited[item] = 2

            return True
            
        for recipe in recipes:
            if visited[recipe] == 2 or traverse_recipes(recipe):
                output.append(recipe)

        return output