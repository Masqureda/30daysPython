# tuple oluşturma
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # (1, 2, 3, 4, 5)

# tuple elemanlarına erişim
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # 1
print(my_tuple[3])  # 4

# tuple elemanlarını güncelleme
my_tuple = (1, 2, 3, 4, 5)
my_tuple[2] = 7  # TypeError: 'tuple' object does not support item assignment

# tuple içindeki elemanların sayısını alma
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # 5

# tuple içinde belirli bir elemanın sayısını alma
my_tuple = (1, 2, 3, 4, 5, 3, 2, 1)
print(my_tuple.count(3))  # 2

# tuple içinde belirli bir elemanın indeksini alma
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # 2

# tuple'ları daha büyük bir tuple'a ekleme
my_tuple1 = (1, 2, 3)
my_tuple2 = (4, 5, 6)
my_tuple3 = my_tuple1 + my_tuple2
print(my_tuple3)  # (1, 2, 3, 4, 5, 6)
