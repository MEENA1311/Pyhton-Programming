set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.add(6)
set1.remove(2)
set1.discard(10)  # No error if not present
popped = set1.pop()
set1.clear()
set_copy = set2.copy()
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))
print("Is Subset:", set1.issubset(set2))
print("Is Superset:", set1.issuperset(set2))
print("Are Disjoint:", set1.isdisjoint(set2))
