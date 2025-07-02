class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        

        city_a = []
        city_b = []
        city_cost_diff = []
        n = len(costs) // 2
        idx = 0

        for cost_a, cost_b in costs:
            city_cost_diff.append((abs(cost_a - cost_b), idx))
            idx += 1
            

        city_cost_diff.sort(reverse=True)

        for diff, idx in city_cost_diff:
            
            if costs[idx][0] < costs[idx][1] and len(city_a) != n:
                city_a.append(costs[idx][0])

            elif costs[idx][0] > costs[idx][1] and len(city_b) != n:
                city_b.append(costs[idx][1])

            elif len(city_a) == n and len(city_b) != n:
                city_b.append(costs[idx][1])

            else:
                city_a.append(costs[idx][0])
        

        
        return sum(city_a) + sum(city_b)
            


