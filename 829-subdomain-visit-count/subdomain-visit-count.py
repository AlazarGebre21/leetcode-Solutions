class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dict = {}
        result = []
        for i in range(len(cpdomains)):
            array = cpdomains[i].split(' ')
            domain_int = int(array[0])
            domain_array = array[1].split('.')
            domain_str = ''
            j = len(domain_array) - 1
            while j >= 0:
                if j != len(domain_array) - 1:
                    domain_str = domain_array[j] + '.' + domain_str
                else:
                    domain_str = domain_array[j]
                
                if domain_str in domain_dict:
                    domain_dict[domain_str] += domain_int
                else:
                    domain_dict[domain_str] = domain_dict.get(domain_str,domain_int)
                j -= 1
        
        for key, value in domain_dict.items():
            result.append(str(value) + " " + key)
        
        return result







                