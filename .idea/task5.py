n = int(input())
my_set = {frozenset(input() for _ in range(int(input()))) for _ in range(n)}
res = frozenset.intersection(*my_set)
print(*sorted(res), sep='\n')