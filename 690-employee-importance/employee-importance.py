"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        importance = {}
        graph = {}
        total_imp = 0
        
        for i in range(len(employees)):
            graph[employees[i].id] = employees[i].subordinates
            importance[employees[i].id] = employees[i].importance
        

        def dfs(vertex):
            nonlocal total_imp

            for n in graph[vertex]:

                dfs(n)
            
            total_imp += importance[vertex]
        
        dfs(id)
        return total_imp
            
        


    