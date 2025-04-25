'''
    Let's go to casino
    Author: Saksham Rathi
'''
import sys
MOD = 1000000007  # 1e9+7
def countways(n):
    if n == 0:
        return 1
    ways = [0] * (n + 1)
    ways[0] = 1  
    for i in range(1, n + 1):
        for j in range(1, 7): 
            if i - j >= 0:
                ways[i] = (ways[i] + ways[i - j])%MOD  
    return ways[n]
num = int(sys.argv[1])
print(countways(num))