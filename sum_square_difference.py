tot = 0
tots = 0
res = 0
for x in range(101):
    a = (x ** 2)
    tot = tot + a
    print(tot)
for x in range(1,101):
    tots = tots + x
    res = tots ** 2
    print(res)

print(res - tot)