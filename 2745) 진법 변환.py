import sys

N, B = sys.stdin.readline().split()
N = N[::-1]
B = int(B)

# ord(A) = 65, chr(65) = A
size = len(N)
base10 = 0
for i in range(size):
    if N[i].isdigit():
        base10 += int(N[i]) * B**i
    else:
        base10 += (ord(N[i])-55) * B**i

print(base10)