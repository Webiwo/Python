my_file = open("test.txt")

print(my_file.read())
my_file.seek(0)

print(my_file.readline())
print(my_file.readlines())

my_file.close()

# opcja with nie wymaga zamykania pliku

with open("test.txt", mode="r+") as my_new_file:  # mode="a" - append
    print(my_new_file.readlines())
    result = my_new_file.write("hellloooo")

# pathlib - umożliwia obsługę plików na wielu systemach operacyjnych


try:
    with open("nie_ma_pliku.txt") as txt_file:
        print(txt_file.read())
except FileNotFoundError as err:
    print(f"File does not exist {err}")
