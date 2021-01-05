# =============================================================================
# No.1711 Count Good Meals

# A good meal is a meal that contains exactly two different food items 
# with a sum of deliciousness equal to a power of two.

# =============================================================================

from collections import Counter

class Solution:
    def countPairs(self, deliciousness):
        
        target = [2**i for i in range(22)]
        
        deli = Counter(deliciousness)
        
        visited = set()
        
        num = 0
        
        for i in deli:
            if i * 2 in target:
                num += (deli[i] * (deli[i]-1) / 2)
                # print (num)
            for j in target:
                if (j - i) in deli and (j - i) not in visited and (j-i) != i:
                    num += (deli[i] * deli[j - i])
                    # print (num)
                    
            visited.add(i)
        return int(num) % 1_000_000_007
    
    # ans 