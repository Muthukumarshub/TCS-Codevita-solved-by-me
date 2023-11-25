def max_expertise(n, c, conflicts, expertise):
    dp = [0] * (1 << n)
    for i in range(n):
        dp[1 << i] = expertise[i]
    for mask in range(1 << n):
        for i in range(n):
            if (mask & (1 << i)) == 0:  
                for conflict in conflicts[i]:
                    if mask & (1 << conflict):  
                        break
                else:
                    dp[mask | (1 << i)] = max(dp[mask | (1 << i)], dp[mask] + expertise[i])
    max_expertise_value = max(dp)
    return max_expertise_value

# Input
n, c = map(int, input().split())
conflicts = [[] for _ in range(n)]
for _ in range(c):
    a, b = map(int, input().split())
    conflicts[a-1].append(b-1)
    conflicts[b-1].append(a-1)
expertise = list(map(int, input().split()))

# Output
result = max_expertise(n, c, conflicts, expertise)
print(result)