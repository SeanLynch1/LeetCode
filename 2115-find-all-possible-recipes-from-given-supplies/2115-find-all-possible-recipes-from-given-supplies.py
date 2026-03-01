class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        output = []
        self.mapping = defaultdict(list)
        self.visited = defaultdict(int)
        supplies = set(supplies)

        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                self.mapping[recipes[i]].append(ingredient)

            
        def traverse_recipes(item: str) -> bool:
            
            if item in supplies:
                return True

            if item not in self.mapping:
                return False

            if self.visited[item] == 1:
                return False

            if not self.mapping[item] or self.visited[item] == 2:
                self.visited[item] = 2
                return True

            self.visited[item] = 1

            for ingredient in self.mapping[item]:

                if traverse_recipes(ingredient):
                    self.visited[ingredient] = 2
                else:
                    return False

            self.visited[item] = 2

            return True
            
        for recipe in recipes:
            if self.visited[recipe] == 2 or traverse_recipes(recipe):
                output.append(recipe)

        return output