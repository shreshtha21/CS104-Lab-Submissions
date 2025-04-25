'''
    Tower of Hanoi
    Author: Abhi Jain
'''

'''
Write your code to solve tower of hanoi problem here
Take input from user for number of disks

Output format:
line 1: number of moves(N)
line 2: move1
line 3: move2
...
line N+1: moveN
'''

'''
To solve this problem, you can use the recursive approach.
'''

import argparse
n = argparse.ArgumentParser()
n.add_argument("n", type=int)
args = n.parse_args()
n = args.n

def toh(n,s,d,a,moves):
    count=0
    if n==1:
        moves.append(f"{s} {d}")
        return 1
    else:
        count = 0
        count += toh(n - 1, s, a, d, moves)  # Move n-1 disks to auxiliary
        moves.append(f"{s} {d}")  # Move nth disk to destination
        count += 1
        count += toh(n - 1, a, d, s, moves)  # Move n-1 disks from auxiliary to destination
        return count

moves = []
count = toh(n,1,3,2,moves)
print(count)
for move in moves:
    print(move)
