class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        ice_cream_cost = 0
        count = 0
        hash_map = [0] * (max(costs) + 1)
        for i in range(len(costs)):
            hash_map[costs[i]] += 1
        
        for j in range(len(hash_map)):
            if hash_map[j] == 0:
                continue
            elif hash_map[j] == 1:
                if ice_cream_cost < coins:
                    ice_cream_cost += j
                    hash_map[j] -= 1
                    if ice_cream_cost <= coins:
                        count += 1
                else:
                    break
            elif hash_map[j] > 1:
                while ice_cream_cost < coins and hash_map[j] > 0:
                    ice_cream_cost += j
                    hash_map[j] -= 1
                    if ice_cream_cost <= coins:
                        count += 1
        return count
            
            
                
        