'''
근데 6중 for문 버전이 더 빠르다 어째서
'''

import sys, itertools

while True:
    s = sys.stdin.readline()
    if s[0]=="0": break

    pool = list(map(int, s.split()))
    k = pool.pop(0)

    res = itertools.combinations(pool, 6)
    for combi in res:
        print(' '.join(map(str, combi)))
    print()