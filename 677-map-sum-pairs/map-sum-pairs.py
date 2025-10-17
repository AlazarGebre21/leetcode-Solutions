class MapSum:

    def __init__(self):
        self.root = {}
        self.my_dict = {}

    def insert(self, key: str, val: int) -> None:
        if not self.my_dict.get(key,0):
            self.my_dict[key] = val
            cur = self.root
            for c in key:
                if c not in cur.keys():
                    cur[c] = {}
                cur = cur[c]
                cur['//'] = cur.get('//', 0) + val
            cur['/'] = True
        else:
            cur = self.root
            for c in key:
                cur = cur[c]
                cur['//'] = cur.get('//', 0) - self.my_dict[key] + val
            
            self.my_dict[key] = val


        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c in cur.keys():
                cur = cur[c]
            else:
                return 0
        return cur['//']
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)