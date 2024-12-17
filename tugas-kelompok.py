

def add_student(dict):
    student_id = int(input("Masukkan NIM siswa: "))
    if student_id in dict:
        print("\n===========================")
        print("NIM sudah terdaftar.")
        print("===========================")

        return

    name = input("Masukkan nama siswa: ")
    score = int(input("Masukkan nilai siswa: "))

    dict[student_id] = {"name": name, "score": score}
    
    print("\n===========================")
    print("Siswa berhasil ditambahkan.")
    print("----------------------------")
    print("Data Mahasiswa")
    display_students(dict)
    print("===========================")

def remove_student(dict):
    student_id = int(input("Masukkan NIM siswa yang akan dihapus: "))

    if student_id in dict:
        del dict[student_id]
        print("\n===========================")
        print("Siswa berhasil dihapus.")
        print("----------------------------")
        print("Data Mahasiswa")
        display_students(dict)
        print("===========================")
    else:
        print("\n===========================")
        print(f"NIM {student_id} tidak ditemukan.")
        print("===========================")

def display_students(dict):
    if not dict:
        print("Tidak ada data siswa yang tersedia.")
        return

    for index, (student_id, details) in enumerate(dict.items(), start=1):
        print(f"{index}. NIM: {student_id}, Nama: {details['name']}, Nilai: {details['score']}")

def search_student(dict):
    student_id = int(input("Masukkan NIM siswa yang dicari: "))

    if student_id in dict:
        details = dict[student_id]
        print("\n===========================")
        print(f"NIM: {student_id}, Nama: {details['name']}, Nilai: {details['score']}")
        print("===========================")
    else:
        print("\n===========================")
        print(f"NIM {student_id} tidak ditemukan.")
        print("===========================")

def average_score(dict):
    if not dict:
        print("\n===========================")
        print("Tidak ada data untuk menghitung rata-rata nilai.")
        print("===========================")
        return
    
    scores = []
    for details in dict.values():
        scores.append(details['score'])

    avg = sum(scores) / len(scores)
    print("\n===========================")
    print(f"Rata-rata nilai: {avg:.2f}")
    print("===========================")

student_data = {}  

while True:
    print("""
Menu Utama:
1. Tambah Siswa
2. Hapus Siswa
3. Tampilkan Data Siswa
4. Cari Siswa
5. Hitung Rata-rata Nilai
6. Keluar
    """)

    menu_choice = int(input("Pilih opsi (1-6): "))

    if menu_choice > 6 or menu_choice < 1:
        print("\n===========================")
        print("Input tidak valid! Silakan masukkan angka antara 1 hingga 6.")
        print("===========================")
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
        print("Program selesai.")
        break
