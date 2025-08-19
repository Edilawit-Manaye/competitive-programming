# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

n = int(input())
children = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    parent = int(input())
    children[parent].append(i)

is_spruce = True
for i in range(1, n + 1):
    if children[i]:
        leaf_children_count = 0
        for child in children[i]:
            if not children[child]:
                leaf_children_count += 1
        if leaf_children_count < 3:
            is_spruce = False
            break

if is_spruce:
    print("Yes")
else:
    print("No")