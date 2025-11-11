class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        security_count = []
        total_beams = 0

        for b in bank:
            temp = b.count('1')
            if temp != 0:
                security_count.append(temp)
        
        for i in range(len(security_count) - 1):
            total_beams += security_count[i]*security_count[i+1]
        
        return total_beams

        
    