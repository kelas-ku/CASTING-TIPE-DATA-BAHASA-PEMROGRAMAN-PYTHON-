# Casting Tipe Data Khusus 1
# Dengan menggunakan nilai variabel tipe data int (integer)

# Color
reset = "\033[1;0m"
hijau = "\033[1;32m"
merah = "\033[1;31m"
kuning = "\033[1;33m"

# Data awal
data_tuple = (1, 2, 3)
data_list = [1, 3, 2]
data_set = {4, 5, 6}
data_dict = {"nama": "Zeth", "umur": 21}

# Khusus casting ke dic (dictionary)
data_tuple_dict = ({"nama": "Ali", "umur": 20},)
data_list_dict = [{"nama": "Ali", "umur": 20}]
data_set_dict = ({"nama": "Ali", "umur": 20},)

# Judul
print(f"{hijau}-"*60)
print(f"{reset}{'CASTING TIPE DATA':^58}")
print(f"{hijau}-"*60)

# Tuple
print(f"{reset}Merubah Tuple Menjadi Tipe Data Yang Lainnya")
print(f"{hijau}-"*60)
print(f"{reset}Data {merah}: {kuning}", data_tuple, f"{reset}-type {merah}: {kuning}", type(data_tuple))
tuple_list = list(data_tuple)
print(f"{reset}Data {merah}: {kuning}", tuple_list, f"{reset}-type {merah}: {kuning}", type(tuple_list))
tuple_set = set(data_tuple)
print(f"{reset}Data {merah}: {kuning}", tuple_set, f"{reset}-type {merah}: {kuning}", type(tuple_set))
tuple_dict = dict(data_tuple_dict)
print(f"{reset}Data {merah}: {kuning}", tuple_dict, f"{reset}-type {merah}: {kuning}", type(tuple_dict))

# List
print(f"{hijau}-"*60)
print(f"{reset}Merubah List Menjadi Tipe Data Yang Lainnya")
print(f"{hijau}-"*60)
print(f"{reset}Data {merah}: {kuning}", data_list, f"{reset}-type {merah}: {kuning}", type(data_list))
list_tuple = tuple(data_list)
print(f"{reset}Data {merah}: {kuning}", list_tuple, f"{reset}-type {merah}: {kuning}", type(list_tuple))
list_set = set(data_list)
print(f"{reset}Data {merah}: {kuning}", list_set, f"{reset}-type {merah}: {kuning}", type(list_set))
list_dict = dict(data_list_dict)
print(f"{reset}Data {merah}: {kuning}", list_dict, f"{reset}-type {merah}: {kuning}", type(list_dict))

# Set
print(f"{hijau}-"*60)
print(f"{reset}Merubah Set Menjadi Tipe Data Yang Lainnya")
print(f"{reset}-"*60)
print(f"{reset}Data {merah}: {kuning}", data_set, f"{reset}-type {merah}: {kuning}", type(data_set))
set_tuple = tuple(data_set)
print(f"{reset}Data {merah}: {kuning}", set_tuple, f"{reset}-type {merah}: {kuning}", type(set_tuple))
set_list = list(data_set)
print(f"{reset}Data {merah}: {kuning}", set_list, f"{reset}-type {merah}: {kuning}", type(set_list))
set_dict = dict(data_set_dict)
print(f"{reset}Data {merah}: {kuning}", set_dict, f"{reset}-type {merah}: {kuning}", type(set_dict))

# Dic
print(f"{hijau}-"*60)
print(f"{reset}Merubah Dict Menjadi Tipe Data Yang Lainnya")
print(f"{hijau}-"*60)
print(f"{reset}Data {merah}: {kuning}", data_dict, f"{reset}-type {merah}: {kuning}", type(data_dict))
dict_tuple = tuple(data_dict)
print(f"{reset}Data {merah}: {kuning}", dict_tuple, f"{reset}-type {merah}: {kuning}", type(dict_tuple))
dict_list = list(data_dict)
print(f"{reset}Data {merah}: {kuning}", dict_list, f"{reset}-type {merah}: {kuning}", type(dict_list))
dict_set = set(data_dict)
print(f"{reset}Data {merah}: {kuning}", dict_set, f"{reset}-type {merah}: {kuning}", type(dict_set))