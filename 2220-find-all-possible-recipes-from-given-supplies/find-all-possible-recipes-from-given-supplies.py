class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph = defaultdict(list)
        pre_req = defaultdict(int)
        ans = []

        for recipe, ingrident in zip(recipes,ingredients):
            
            for i in ingrident:
                graph[i].append(recipe)
                pre_req[recipe] += 1
        
        for element in supplies:
            pre_req[element] = 0
        
        que = deque([key for key, value in pre_req.items() if value == 0])

        while que:

            req = que.popleft()

            for child in graph[req]:

                pre_req[child] -= 1

                if pre_req[child] == 0:
                    que.append(child)
                # if pre_req[child] == 0 and child in recipes:
                    ans.append(child)
        
        return ans

        

        
        