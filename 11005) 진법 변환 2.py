import sys

N, B = map(int, sys.stdin.readline().split())

# ord(A) = 65, chr(65) = A

baseB = ""
while N:
    N, mod = divmod(N,B)

    if mod < 10: baseB += str(mod)
    else: baseB += chr(mod+55)

print(baseB[::-1])
