class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        directed_graph = {}
        judge = set()
        is_it_judge = None

        if not trust and n == 1:
            return 1
        elif not trust and n > 1:
            return -1

        for i in range(1,n+1):
            directed_graph[i] = set()
        
        for _from, _to in trust:
            directed_graph[_from].add(_to)

        for key,values in directed_graph.items():
            if not len(values):
                is_it_judge = key
        
        for key, value in directed_graph.items():
            if key != is_it_judge and is_it_judge not in value:
                return -1
        
        return is_it_judge

