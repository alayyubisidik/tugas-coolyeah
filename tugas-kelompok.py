
student_data = {}  

def add_student():
    student_id = int(input("Masukkan NIM siswa: "))
    if student_id in student_data:
        print("\n===========================")
        print("NIM sudah terdaftar.")
        print("===========================")

        return

    name = input("Masukkan nama siswa: ")
    score = int(input("Masukkan nilai siswa: "))

    student_data[student_id] = {"name": name, "score": score}
    
    print("\n===========================")
    print("Siswa berhasil ditambahkan.")
    print("----------------------------")
    print("Data Mahasiswa")
    display_students()
    print("===========================")

def remove_student():
    student_id = int(input("Masukkan NIM siswa yang akan dihapus: "))

    if student_id in student_data:
        del student_data[student_id]
        print("\n===========================")
        print("Siswa berhasil dihapus.")
        print("----------------------------")
        print("Data Mahasiswa")
        display_students()
        print("===========================")
    else:
        print("\n===========================")
        print(f"NIM {student_id} tidak ditemukan.")
        print("===========================")

def display_students():
    if not student_data:
        print("Tidak ada data siswa yang tersedia.")
        return

    for index, (student_id, details) in enumerate(student_data.items(), start=1):
        print(f"{index}. NIM: {student_id}, Nama: {details['name']}, Nilai: {details['score']}")

def search_student():
    student_id = int(input("Masukkan NIM siswa yang dicari: "))

    if student_id in student_data:
        details = student_data[student_id]
        print("\n===========================")
        print(f"NIM: {student_id}, Nama: {details['name']}, Nilai: {details['score']}")
        print("===========================")
    else:
        print("\n===========================")
        print(f"NIM {student_id} tidak ditemukan.")
        print("===========================")

def average_score():
    if not student_data:
        print("\n===========================")
        print("Tidak ada data untuk menghitung rata-rata nilai.")
        print("===========================")
        return
    
    scores = []
    for details in student_data.values():
        scores.append(details['score'])

    avg = sum(scores) / len(scores)
    print("\n===========================")
    print(f"Rata-rata nilai: {avg:.2f}")
    print("===========================")

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
        add_student()
    elif menu_choice == 2:
        remove_student()
    elif menu_choice == 3:
        display_students()
    elif menu_choice == 4:
        search_student()
    elif menu_choice == 5:
        average_score()
    elif menu_choice == 6:
        print("Program selesai.")
        break
