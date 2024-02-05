from itertools import combinations

def D(lengths):

    # Sort the list of lengths in ascending order
    lengths.sort()
    unique_polygons = set()

    n = len(lengths)

    # Iterate through the lengths, considering each as the longest side
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if lengths[i] + lengths[j] > lengths[k]:
                    unique_polygons.add(tuple(sorted([lengths[i], lengths[j], lengths[k]])))

    # Count polygons with more sides (up to n sides)
    for num_sides in range(4, n + 1):
        for combo in combinations(lengths, num_sides):
            if isPolygon(list(combo)):
                unique_polygons.add(combo)

    return len(unique_polygons)

def isPolygon(lengths):
    # Check if a set of lengths can form a polygon
    n = len(lengths)
    if sum(lengths) - max(lengths) > max(lengths):
        return True
    return False


ns = [2, 2, 2, 2]
print(D(ns))

