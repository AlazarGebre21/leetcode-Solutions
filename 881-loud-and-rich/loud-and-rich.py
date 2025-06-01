class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        grap_h = defaultdict(list)
        n = len(quiet)
        ans = [0] * n

        for _from, _to in richer:
            grap_h[_to].append(_from)

        my_dict = {}

        for i in range(n):
            my_dict[quiet[i]] = i


        

        # print(grap_h)

        def bfs(node):
            _min = float('inf')
            visited = set()


            que = deque([node])

            while que:


                for _ in range(len(que)):

                    m = que.popleft()
                    visited.add(m)
                    # print(m)

                    _min = min(_min, quiet[m])

                    for child in grap_h[m]:
                        if child not in visited:
                            que.append(child)

                
            return _min
                

        for i in range(n):
            ans[i] = my_dict[bfs(i)]
            # print()
        
        return ans
            

