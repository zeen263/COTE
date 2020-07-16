import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    zero = [1, 0, 1]
    one = [0, 1, 1]

    for j in range(3, n+1):
        zero.append(zero[j-1] + zero[j-2])
        one.append(one[j-1] + one[j-2])

    print(zero[n], one[n])
