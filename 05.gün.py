# liste oluşturma
my_list = ["elma", "armut", "çilek", "muz"]

# liste elemanlarına erişim
print(my_list[0])  # elma
print(my_list[2])  # çilek
print(my_list[-1])  # muz

# liste uzunluğunu bulma
my_list = ["elma", "armut", "çilek", "muz"]
print(len(my_list))  # 4

# liste elemanlarına ekleme
my_list = ["elma", "armut", "çilek", "muz"]
my_list.append("portakal")
print(my_list)  # ['elma', 'armut', 'çilek', 'muz', 'portakal']

# liste elemanlarından çıkarma
my_list = ["elma", "armut", "çilek", "muz"]
my_list.remove("armut")
print(my_list)  # ['elma', 'çilek', 'muz']

# liste elemanlarını sıralama
my_list = [3, 7, 2, 1, 8, 4]
my_list.sort()
print(my_list)  # [1, 2, 3, 4, 7, 8]

# liste elemanlarını tersine çevirme
my_list = ["elma", "armut", "çilek", "muz"]
my_list.reverse()
print(my_list)  # ['muz', 'çilek', 'armut', 'elma']

# liste dilimleme
my_list = ["elma", "armut", "çilek", "muz"]
print(my_list[1:3])  # ['armut', 'çilek']

