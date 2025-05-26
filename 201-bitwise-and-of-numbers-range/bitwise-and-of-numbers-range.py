class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        # We could do it by iteration but come on we are going to iterate billion times in the worest case so ...

        shif = 0

        # why not handle the common prefix of all the numbers in that range that does not change meaning the common prefix of all the numbers in which there value does not flip over the course

        # below the common prefix of the list of binary numbers is  the first 2 most significan bit the others will flip in the process

# 11010  ... 26
# 11011
# 11100
# 11101
# 11110  ... 30


        # what we are doing here is we are dividing by 2 (left and right) until left and right are equal and counting the number of division it takes to make left and right equal

        # example left = 26 and right = 30 so 
        
            # Step 1:
            # left  = 11010 → 1101
            # right = 11110 → 1111
            # still not equal

            # Step 2:
            # left  = 1101 → 110
            # right = 1111 → 111
            # still not equal

            # Step 3:
            # left  = 110 → 11
            # right = 111 → 11
            # now they are equal!

        # then finally we will left shift left by the steps it take us to make left and right equal

        while left != right:

            shif += 1
            left >>= 1
            right >>= 1
        
        return left << shif

