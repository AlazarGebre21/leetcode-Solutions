class ProductOfNumbers:

    def __init__(self):
      self.product_prefix = []

    def add(self, num: int) -> None:
    
        if num == 0:
            self.product_prefix = []
        else:
            if len(self.product_prefix)  == 0:
                return self.product_prefix.append(num)
            elif len(self.product_prefix) >= 1:
                return self.product_prefix.append(num*self.product_prefix[-1])
                
        
    def getProduct(self, k: int) -> int:
        if k > len(self.product_prefix):
            return 0
        elif k == len(self.product_prefix):
            return self.product_prefix[-1]
        else:
            return self.product_prefix[-1] // self.product_prefix[len(self.product_prefix) - k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)