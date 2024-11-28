import itertools

def is_minimal(point, A):
    for other in A:
        if all(x <= y for x, y in zip(other, point)) and other != point:
            return False
    return True

A1 = [(n, k) for n in range(1, 100) for k in range(1, 100) if n * k > 11]
minimal_points_1 = [point for point in A1 if is_minimal(point, A1)]
print("Minimal points in the set {(n, k) in N^2 : n * k > 11}:")
for point in minimal_points_1:
    print(point)

A2 = [(n, k) for n in range(1, 20) for k in range(1, 20) if (n - 10)**2 + (k - 10)**2 <= 25]
minimal_points_2 = [point for point in A2 if is_minimal(point, A2)]
print("\nMinimal points in the set {(n, k) in N^2 : (n - 10)^2 + (k - 10)^2 <= 25}:")
for point in minimal_points_2:
    print(point)

