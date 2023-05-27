set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Enter your solution heres

union_set = set1.union(set2)
inter_set = set1.intersection(set2)
diff_set = set1.difference(set2)
sym_diff = set1.symmetric_difference(set2)

print("Union set:", union_set)
print("Intersection set:", inter_set)
print("Difference set:", diff_set)
print("Symmetric difference set:", sym_diff)