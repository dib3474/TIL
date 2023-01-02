import sys
input = sys.stdin.readline

def find(a, num):
    start = 0
    end = len(a)-1
    while start <= end:
        m = (start+end)//2
        if a[m] == num:
            return 1
        elif a[m] > num:
            end = m-1
        else:
            start = m+1
    return 0

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
L = list(map(int, input().split()))

for x in L:
    print(find(a, x))