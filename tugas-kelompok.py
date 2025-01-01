# Fungsi untuk menambahkan mahasiswa baru ke dalam dictionary
def add_student(dict):
    # Meminta input NIM mahasiswa
    student_id = int(input("Masukkan NIM mahasiswa: "))
    # Memeriksa apakah NIM sudah terdaftar dalam dictionary
    if student_id in dict:
        print("\n===========================")
        print("NIM sudah terdaftar.")
        print("===========================")
        return

    # Meminta input nama dan nilai mahasiswa
    name = input("Masukkan nama mahasiswa: ")
    score = int(input("Masukkan nilai mahasiswa: "))
    
    # Menambahkan data mahasiswa ke dictionary
    dict[student_id] = {"name": name, "score": score}
    
    # Menampilkan pesan berhasil dan daftar mahasiswa
    print("\n===========================")
    print("Mahasiswa berhasil ditambahkan.")
    print("----------------------------")
    print("Data Mahasiswa")
    display_students(dict)
    print("===========================")

# Fungsi untuk menghapus mahasiswa dari dictionary
def remove_student(dict):
    # Meminta input NIM mahasiswa yang akan dihapus
    student_id = int(input("Masukkan NIM mahasiswa yang akan dihapus: "))
    
    # Memeriksa apakah NIM ada dalam dictionary
    if student_id in dict:
        # Menghapus data mahasiswa
        del dict[student_id]
        print("\n===========================")
        print("Mahasiswa berhasil dihapus.")
        print("----------------------------")
        print("Data Mahasiswa")
        display_students(dict)
        print("===========================")
    else:
        # Menampilkan pesan jika NIM tidak ditemukan
        print("\n===========================")
        print(f"NIM {student_id} tidak ditemukan.")
        print("===========================")

# Fungsi untuk menampilkan semua data mahasiswa
def display_students(dict):
    # Memeriksa apakah dictionary kosong
    if not dict:
        print("Tidak ada data mahasiswa yang tersedia.")
        return
    
    # Menampilkan data mahasiswa satu per satu
    for index, (student_id, details) in enumerate(dict.items(), start=1):
        print(f"{index}. NIM: {student_id}, Nama: {details['name']}, Nilai: {details['score']}")

# Fungsi untuk mencari data mahasiswa berdasarkan NIM
def search_student(dict):
    # Meminta input NIM mahasiswa yang dicari
    student_id = int(input("Masukkan NIM mahasiswa yang dicari: "))
    
    # Memeriksa apakah NIM ada dalam dictionary
    if student_id in dict:
        # Menampilkan data mahasiswa jika ditemukan
        details = dict[student_id]
        print("\n===========================")
        print(f"NIM: {student_id}, Nama: {details['name']}, Nilai: {details['score']}")
        print("===========================")
    else:
        # Menampilkan pesan jika NIM tidak ditemukan
        print("\n===========================")
        print(f"NIM {student_id} tidak ditemukan.")
        print("===========================")

# Fungsi untuk menghitung rata-rata nilai mahasiswa
def average_score(dict):
    # Memeriksa apakah dictionary kosong
    if not dict:
        print("\n===========================")
        print("Tidak ada data untuk menghitung rata-rata nilai.")
        print("===========================")
        return
    
    # Mengambil semua nilai mahasiswa dari dictionary
    scores = []
    for details in dict.values():
        scores.append(details['score'])
    
    # Menghitung rata-rata nilai
    avg = sum(scores) / len(scores)
    print("\n===========================")
    print(f"Rata-rata nilai: {avg:.2f}")
    print("===========================")

# Dictionary untuk menyimpan data mahasiswa
student_data = {}  

# Loop utama program
while True:
    # Menampilkan menu utama
    print("""
Menu Utama:
1. Tambah Mahasiswa
2. Hapus Mahasiswa
3. Tampilkan Data Mahasiswa
4. Cari Mahasiswa
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
