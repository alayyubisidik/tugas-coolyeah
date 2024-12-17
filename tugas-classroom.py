# numbers = []

# numberOfInput = int(input("Berapa jumlah angka yang anda ingin masukan?  "))

# print("\nSilakan masukkan angka-angka Anda:")
# for i in range(numberOfInput): 
#     numberInput = int(input(f"Masukan angka ke-{i + 1}: "))
#     numbers.append(numberInput)

# sumOfNumbers = sum(numbers)
# averageOfNumbers = sumOfNumbers / len(numbers)

# print(f"\nHasil Perhitungan:")
# print(f"1. Total dari semua angka yang Anda masukkan adalah: {sumOfNumbers}")
# print(f"2. Rata-rata dari angka-angka tersebut adalah: {averageOfNumbers:.2f}")



# ================================================


# names = ()

# numberOfInput = int(input("Berapa jumlah nama yang ingin Anda masukkan? "))

# print("\nSilakan masukkan nama-nama Anda:")
# for i in range(numberOfInput): 
#     nameInput = input(f"Masukkan nama ke-{i + 1}: ")
#     names += (nameInput,)  

# print("\nDaftar nama yang Anda masukkan:")
# for i, name in enumerate(names): 
#     print(f"{i}. {name}")




# ===================================================



# mahasiswa_data = {}
# number_of_students = int(input("Berapa banyak data mahasiswa yang ingin Anda masukkan? "))

# for i in range(number_of_students):
#     print(f"\nMasukkan data untuk mahasiswa ke-{i + 1}:")
    
#     npm = input("Masukkan NPM: ")
#     nama = input("Masukkan Nama: ")
#     prodi = input("Masukkan Program Studi: ")

#     mahasiswa_data[npm] = (nama, prodi)

# print("\nDaftar data mahasiswa yang telah dimasukkan:")
# for npm, data in mahasiswa_data.items():
#     print(data)
#     nama, prodi = data 
#     print(f"NPM: {npm}, Nama: {nama}, Prodi: {prodi}")


# =================================================


# kalimat = input("Masukkan sebuah kalimat: ")

# kata_list = kalimat.split()

# frekuensi_kata = {}

# for kata in kata_list:
#     if kata in frekuensi_kata:
#         frekuensi_kata[kata] += 1
#     else:
#         frekuensi_kata[kata] = 1

# print("\nFrekuensi setiap kata dalam kalimat:")
# for kata, frekuensi in frekuensi_kata.items():
#     print(f"Kata: '{kata}', Frekuensi: {frekuensi}")
