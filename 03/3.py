from heapq import nsmallest

""" First part """
with open('input', 'r') as data:
    possible = 0
    for line in data:
        sides = [int(item.strip()) for item in line.strip().split(' ') if item]
        if max(sides) < sum(nsmallest(2, sides)):
            possible += 1


""" Second part """
def is_it_possible(sides):
    return max(sides) < sum(nsmallest(2, sides))

with open('input', 'r') as data:
    possible = 0
    while True:
        try:
            triangles = []
            for _ in range(3):
                triangles.append([item.strip() for item in next(data).strip().split(' ') if item])
            for i in range(3):
                sides = [triangles[0][i], triangles[1][i], triangles[2][i]]
                sides = [int(i) for i in sides]
                if is_it_possible(sides) == True:
                    possible += 1
        except StopIteration:
            break
print(possible)
