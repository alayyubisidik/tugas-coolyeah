# Fungsi untuk menambahkan siswa baru ke dalam dictionary
def add_student(dict):
    # Meminta input NIM siswa
    student_id = int(input("Masukkan NIM siswa: "))
    # Memeriksa apakah NIM sudah terdaftar dalam dictionary
    if student_id in dict:
        print("\n===========================")
        print("NIM sudah terdaftar.")
        print("===========================")
        return

    # Meminta input nama dan nilai siswa
    name = input("Masukkan nama siswa: ")
    score = int(input("Masukkan nilai siswa: "))
    
    # Menambahkan data siswa ke dictionary
    dict[student_id] = {"name": name, "score": score}
    
    # Menampilkan pesan berhasil dan daftar siswa
    print("\n===========================")
    print("Siswa berhasil ditambahkan.")
    print("----------------------------")
    print("Data Mahasiswa")
    display_students(dict)
    print("===========================")

# Fungsi untuk menghapus siswa dari dictionary
def remove_student(dict):
    # Meminta input NIM siswa yang akan dihapus
    student_id = int(input("Masukkan NIM siswa yang akan dihapus: "))
    
    # Memeriksa apakah NIM ada dalam dictionary
    if student_id in dict:
        # Menghapus data siswa
        del dict[student_id]
        print("\n===========================")
        print("Siswa berhasil dihapus.")
        print("----------------------------")
        print("Data Mahasiswa")
        display_students(dict)
        print("===========================")
    else:
        # Menampilkan pesan jika NIM tidak ditemukan
        print("\n===========================")
        print(f"NIM {student_id} tidak ditemukan.")
        print("===========================")

# Fungsi untuk menampilkan semua data siswa
def display_students(dict):
    # Memeriksa apakah dictionary kosong
    if not dict:
        print("Tidak ada data siswa yang tersedia.")
        return
    
    # Menampilkan data siswa satu per satu
    for index, (student_id, details) in enumerate(dict.items(), start=1):
        print(f"{index}. NIM: {student_id}, Nama: {details['name']}, Nilai: {details['score']}")

# Fungsi untuk mencari data siswa berdasarkan NIM
def search_student(dict):
    # Meminta input NIM siswa yang dicari
    student_id = int(input("Masukkan NIM siswa yang dicari: "))
    
    # Memeriksa apakah NIM ada dalam dictionary
    if student_id in dict:
        # Menampilkan data siswa jika ditemukan
        details = dict[student_id]
        print("\n===========================")
        print(f"NIM: {student_id}, Nama: {details['name']}, Nilai: {details['score']}")
        print("===========================")
    else:
        # Menampilkan pesan jika NIM tidak ditemukan
        print("\n===========================")
        print(f"NIM {student_id} tidak ditemukan.")
        print("===========================")

# Fungsi untuk menghitung rata-rata nilai siswa
def average_score(dict):
    # Memeriksa apakah dictionary kosong
    if not dict:
        print("\n===========================")
        print("Tidak ada data untuk menghitung rata-rata nilai.")
        print("===========================")
        return
    
    # Mengambil semua nilai siswa dari dictionary
    scores = []
    for details in dict.values():
        scores.append(details['score'])
    
    # Menghitung rata-rata nilai
    avg = sum(scores) / len(scores)
    print("\n===========================")
    print(f"Rata-rata nilai: {avg:.2f}")
    print("===========================")

# Dictionary untuk menyimpan data siswa
student_data = {}  

# Loop utama program
while True:
    # Menampilkan menu utama
    print("""
Menu Utama:
1. Tambah Siswa
2. Hapus Siswa
3. Tampilkan Data Siswa
4. Cari Siswa
5. Hitung Rata-rata Nilai
6. Keluar
    """)

    # Meminta input pilihan menu
    menu_choice = int(input("Pilih opsi (1-6): "))

    # Validasi input menu
    if menu_choice > 6 or menu_choice < 1:
        print("\n===========================")
        print("Input tidak valid! Silakan masukkan angka antara 1 hingga 6.")
        print("===========================")
    # Menjalankan fungsi berdasarkan pilihan menu
    elif menu_choice == 1:
        add_student(student_data)
    elif menu_choice == 2:
        remove_student(student_data)
    elif menu_choice == 3:
        display_students(student_data)
    elif menu_choice == 4:
        search_student(student_data)
    elif menu_choice == 5:
        average_score(student_data)
    elif menu_choice == 6:
        # Keluar dari program
        print("Program selesai.")
        break
