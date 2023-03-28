# set oluşturma
my_set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}

# set elemanlarına ekleme
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}

# set elemanlarından çıkarma
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print(my_set)  # {1, 2, 4, 5}

# iki set'in birleşimi
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5, 6, 7, 8}

# iki set'in kesişimi
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection_set = set1.intersection(set2)
print(intersection_set)  # {4, 5}

# set elemanlarının farkı
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
diff_set = set1.difference(set2)
print(diff_set)  # {1, 2, 3}

# set elemanlarını sıralama
my_set = {3, 7, 2, 1, 8, 4}
sorted_set = sorted(my_set)
print(sorted_set)  # [1, 2, 3, 4, 7, 8]

# set'in alt kümeleri
my_set = {1, 2, 3}
subsets = [set(i) for i in list(itertools.chain.from_iterable(itertools.combinations(my_set, r) for r in range(len(my_set) + 1)))]
print(subsets)  # [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
