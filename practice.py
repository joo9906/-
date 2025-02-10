n, m = map(int, input().split())
arr = [0] * 1000001

for _ in range(n):
    x, y = map(int, input().split())
    arr[y-1] = x

def polar(arr, m):
    window = sum(arr[:m*2+1])
    max_ice = window

    for i in range(1, 100000-m*2) :
        window = window - arr[i-1] + arr[i+m*2]
        if max_ice < window:
            max_ice = window

    return max_ice

print(polar(arr, m))