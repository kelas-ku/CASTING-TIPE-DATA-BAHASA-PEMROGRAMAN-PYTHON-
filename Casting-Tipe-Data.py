# Casting Tipe Data
# Merubah nilai tipe data menjadi nilai tipe data yang lainnya

"""
	1. Merubah nilai tipe data integer atau singkatannya (int),
	menjadi nilai tipe data yang lainnya.
	2. Merubah nilai tipe data float menjadi nilai tipe data yang lainnya
	3. Merubah nilai tipe data string (str) tanda kutip (''),
	menjadi nilai tipe data yang lainnya.
	4. Merubah nilai tipe data string (str) tanda kutip (""),
	menjadi nilai tipe data yang lainnya.
	5. Merubah nilai tipe data boolean (bool) True,
	menjadi nilai tipe data yang lainnya.
	6. Merubah nilai tipe data boolean (bool) False,
	menjadi nilai tipe data yang lainnya.
"""

# Color
reset = "\033[1;0m"
hijau = "\033[1;32m"
merah = "\033[1;31m"
kuning = "\033[1;33m"

# Merubah int (intger) ke tipe data yang lainnya
# Variabel umum
data_int = 9
data_float = 9.1
data_str1 = '11' # menggunakan tanda kutip('')
data_str2 = "10" # menggunakan tanda kutip ("")
data_bool_true = True
data_bool_false = False
# Variabel casting tipe data integer (int)
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
# Variabel casting float
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
# Variabel casting tipe data string (str) kutip ('')
data_int = int(data_str1)
data_float = float(data_str1)
data_bool = bool(data_str1)
# Variabel casting tipe data string (str) kutip ("")
data_int = int(data_str2)
data_float = float(data_str2)
data_bool = bool(data_str2)
# Variabel casting tipe data boolean (bool) True
data_int = int(data_bool_true)
data_float = float(data_bool_true)
data_str = str(data_bool_true)
# VAriabel casting tipe data boolean (bool) False
data_int = int(data_bool_false)
data_float = float(data_bool_false)
data_str = str(data_bool_false)

# Judul
print(f"{hijau}-"*47)
print(f"{reset}{'CASTING TIPE DATA':^43}")
print(f"{hijau}-"*47)

# Pemanggilan 1
print(f"{reset}Merubah Integer Menjadi Tipe Data Yang Lainnya")
print(f"{hijau}-"*47)
print(f"{reset}Data {merah}: {kuning}", data_int, f"{reset}-type {merah}: {kuning}", type(data_int))
print(f"{reset}Data {merah}: {kuning}", data_float, f"{reset}-type {merah}: {kuning}", type(data_float))
print(f"{reset}Data {merah}: {kuning}", data_str, f"{reset}-type {merah}: {kuning}", type(data_str))
print(f"{reset}Data {merah}: {kuning}", data_bool, f"{reset}-type {merah}: {kuning}", type(data_bool))
print(f"{hijau}-"*47)
print(f"{reset}Merubah Float Menjadi Tipe Data Yang Lainnya")
print(f"{hijau}-"*47)
print(f"{reset}Data {merah}: {kuning}", data_float, f"{reset}-type {merah}: {kuning}", type(data_float))
print(f"{reset}Data {merah}: {kuning}", data_int, f"{reset}-type {merah}: {kuning}", type(data_int))
print(f"{reset}Data {merah}: {kuning}", data_str, f"{reset}-type {merah}: {kuning}", type(data_str))
print(f"{reset}Data {merah}: {kuning}", data_bool, f"{reset}-type {merah}: {kuning}", type(data_bool))
print(f"{hijau}-"*47)
print(f"{reset}Merubah String Menjadi Tipe Data Yang Lainnya") # string (str) kutip ('')
print(f"{hijau}-"*47)
print(f"{reset}Data {merah}: {kuning}", data_str1, f"{reset}-type {merah}: {kuning}", type(data_str1))
print(f"{reset}Data {merah}: {kuning}", data_int, f"{reset}-type {merah}: {kuning}", type(data_int))
print(f"{reset}Data {merah}: {kuning}", data_float, f"{reset}-type {merah}: {kuning}", type(data_float))
print(f"{reset}Data {merah}: {kuning}", data_bool, f"{reset}-type {merah}: {kuning}", type(data_bool))
print(f"{hijau}-"*47)
print(f"{reset}Merubah String Menjadi Tipe Data Yang Lainnya") # string (str) kutip ("")
print(f"{hijau}-"*47)
print(f"{reset}Data {merah}: {kuning}", data_str2, f"{reset}-type {merah}: {kuning}", type(data_str2))
print(f"{reset}Data {merah}: {kuning}", data_int, f"{reset}-typr {merah}: {kuning}", type(data_int))
print(f"{reset}Data {merah}: {kuning}", data_float, f"{reset}-type {merah}: {kuning}", type(data_float))
print(f"{reset}Data {merah}: {kuning}", data_bool, f"{reset}-type {merah}: {kuning}", type(data_bool))
print(f"{hijau}-"*47)
print(f"{reset}Merubah Boolean Menjadi Tipe Data Yang Lainnya") # boolean (bool) True
print(f"{hijau}-"*47)
print(f"{reset}Data {merah}: {kuning}", data_bool_true, f"{reset}-type {merah}: {kuning}", type(data_bool_true))
print(f"{reset}Data {merah}: {kuning}", data_int, f"{reset}-type {merah}: {kuning}", type(data_int))
print(f"{reset}Data {merah}: {kuning}", data_float, f"{reset}-type {merah}: {kuning}", type(data_float))
print(f"{reset}Data {merah}: {kuning}", data_str, f"{reset}-type {merah}: {kuning}", type(data_str))
print(f"{hijau}-"*47)
print(f"{reset}Merubah Boolean Menjadi Tipe Data Yang Lainnya") # boolean (bool) False
print(f"{hijau}-"*47)
print(f"{reset}Data {merah}: {kuning}", data_bool_false, f"{reset}-type {merah}: {kuning}", type(data_bool_false))
print(f"{reset}Data {merah}: {kuning}", data_int, f"{reset}-type {merah}: {kuning}", type(data_int))
print(f"{reset}Data {merah}: {kuning}", data_float, f"{reset}-type {merah}: {kuning}", type(data_float))
print(f"{reset}Data {merah}: {kuning}", data_str, f"{reset}-type {merah}: {kuning}", type(data_str))