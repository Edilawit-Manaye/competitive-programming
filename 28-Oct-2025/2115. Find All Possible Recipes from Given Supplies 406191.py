# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        in_degree = defaultdict(int)
        
        recipe_names_set = set(recipes)
        
        available_items = set(supplies)
        
        for i, recipe_name in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient not in available_items:
                    in_degree[recipe_name] += 1
                adj[ingredient].append(recipe_name)

        q = deque()
        
        for recipe_name in recipes:
            if in_degree[recipe_name] == 0:
                q.append(recipe_name)
                available_items.add(recipe_name)

        result = []
        while q:
            current_recipe = q.popleft()
            result.append(current_recipe)

            for next_recipe in adj[current_recipe]:
                in_degree[next_recipe] -= 1
                
                if in_degree[next_recipe] == 0 and next_recipe in recipe_names_set:
                    q.append(next_recipe)
                    available_items.add(next_recipe)
        
        return result