from datetime import datetime
from tabulate import tabulate

# Data Karyawan berisi daftar karyawan dalam bentuk list of dictionaries
data_karyawan = [
    {'ID Karyawan': 2023120001, 'Nama': 'Hafidz diya purwadhika', 'NIK': 202310225024, 'Jenis Kelamin': 'L', 'No Telepon': '081234567890', 'Tanggal Mulai Bekerja': '2023-01-01', 'Jabatan': 'CEO', 'Gaji Pokok': 16000000, 'Tunjangan Jabatan': 10000000},
    {'ID Karyawan': 2023120002, 'Nama': 'Erik Federick', 'NIK': 202310225023, 'Jenis Kelamin': 'L', 'No Telepon': '081234567891', 'Tanggal Mulai Bekerja': '2023-01-02', 'Jabatan': 'Data Analyst', 'Gaji Pokok': 8500000, 'Tunjangan Jabatan': 1500000}
]
# Fungsi untuk menampilkan data karyawan
def tampil_data() :
    print("\nData Karyawan :")
    headersK = data_karyawan[0].keys()
    dataK = [k.values() for k in data_karyawan]
    print(tabulate(dataK,headersK, tablefmt="grid"))
 
while True:
    try: 
        # Menampilkan menu utama
        print("Selamat Datang di Data Karyawan\n")
        print('''List Menu :
        1. Menampilkan Data Karyawan
        2. Menambah Data Karyawan
        3. Menghapus Data Karyawan
        4. Update Karyawan
        5. Exit Program''')
        menu = int(input("Masukkan angka Menu yang ingin dipilih : "))
        if menu > 5:
            print("Harap Masukan Angka Antara 1-5")
        # menu 1: Menampilkan data karyawan
        if menu == 1:
            while True:
                try:
                    print("1. Data seluruh Karyawan")
                    print("2. Data Karyawan Berdasarkan ID Karyawan")
                    menu_1 = int(input("Masukan angka menu yang ingin dipilih :"))

                    if menu_1 in [1, 2, 3]:
                        break  # Keluar dari perulangan jika input valid
                    else:
                        print("Masukkan angka 1, 2 atau 3 saja.")
                except:
                    print("Harap Masukkan angka")

            if menu_1 == 1:
                # Memanggil fungsi data karyawan untuk menampilkan data
                tampil_data()
            elif menu_1 == 2:
                while True:
                    try:
                        id_karyawan = int(input("Masukan ID Karyawan (10 angka):"))
                        found = False
                        if len(str(id_karyawan)) == 10:
                            for i in range (len(data_karyawan)):  # Mencari karyawan berdasarkan ID
                                if id_karyawan == data_karyawan[i]['ID Karyawan']:
                                    karyawan = data_karyawan[i]
                                    #Menampilkan detail karyawan jika ID ditemukan
                                    print(f"Nama                  : {karyawan['Nama']}")
                                    print(f"NIK                   : {karyawan['NIK']}")
                                    print(f"Jenis Kelamin         : {karyawan['Jenis Kelamin']}")
                                    print(f"Nomor Telepon         : {karyawan['No Telepon']}")
                                    print(f"Tanggal Mulai Bekerja : {karyawan['Tanggal Mulai Bekerja']}")
                                    print(f"Jabatan               : {karyawan['Jabatan']}")
                                    print(f"Gaji Pokok            : {karyawan['Gaji Pokok']}")
                                    print(f"Tunjangan Jabatan     : {karyawan['Tunjangan Jabatan']}")
                                    found = True
                            
                            if found ==  True :
                                while True:
                                    lanjut = input("Apakah Ingin Melanjutkan (ya/tidak): ").lower()
                                    if lanjut in ['ya']:
                                        tidak = True
                                        break
                                    elif lanjut in ['tidak']:
                                        tidak = False
                                        break
                                    else:
                                        print("Input salah ,Masukkan ya/tidak.")
                            
                            if tidak ==  False:
                                break
                    
                        else:
                            print(f"NIK {id_karyawan} tidak ditemukan. Silahkan coba lagi.")
      
                    except:
                        print("Input Yang Dimasukan Salah")
                
        # menu 2: Menambah data karyawan
        elif menu == 2:
            # Input Data Baru Karyawan
            while True:
                id_baru = input("Masukkan ID Karyawan (10 angka): ")
                if len(id_baru) == 10 :
                    id_tersedia = False
                    for i in range(len(data_karyawan)):
                        if id_baru == str(data_karyawan[i]['ID Karyawan']):
                            id_tersedia = True
                            print(f"ID {id_baru} sudah terdaftar. Harap masukkan ID baru.")
                            break

                    if not id_tersedia:
                        break
                else:
                    print("ID harus memiliki 10 Angka dan bukan Huruf.")

            while True:
                nama = input("Masukkan Nama Karyawan (minimal 3 karakter): ")
                if len(nama) >= 3:
                    break
                else:
                    print("Nama harus memiliki minimal 3 karakter.")

            while True:
                try:
                    nik = int(input("Masukkan NIK Karyawan (12 digit): "))
                    if len(str(nik)) == 12:
                        break
                    else:
                        print("NIK harus memiliki 12 digit.")
                except:
                    print("Masukan Angka")

            while True:
                jenis_kelamin = input("Masukkan Jenis Kelamin Karyawan (L/P):  ")
                if jenis_kelamin in ['l', 'p']:
                    jenis_kelamin = jenis_kelamin.upper()
                    break
                    
                else:
                    print("Input salah, harap masukan L/P ")

            while True:    
                no_telepon = input("Masukkan Nomor Telepon Karyawan: ")
                if len(str(no_telepon)) >= 10:
                        break
                else:
                    print("No Telepon harus memiliki minimal 10 digit.")

            tanggal_mulai_bekerja = datetime.now().strftime('%Y-%m-%d')

            while True:
                jabatan = input("Masukan Jabatan Karyawan :")
                if len(jabatan) >= 2:
                    break
                else:
                    print("Harap masukkan minimal 2 huruf")

            while True:
                gaji_input = input("Masukkan Gaji Karyawan :")
                try:
                    # Hilangkan koma dan spasi
                    gaji_input = gaji_input.replace(',', '')
                    gaji_input = gaji_input.replace('.', '')
                    
                    # Coba konversi ke integer
                    gaji = int(gaji_input)
                    break  # Hentikan loop jika berhasil dikonversi
                except :
                    print("Masukkan harus berupa angka. Silakan coba lagi.")

            while True:
                tunjangan_jabatan = (input("Masukan Tunjangan Jabatan :"))
                try:
                    # Hilangkan koma
                    tunjangan_jabatan = tunjangan_jabatan.replace(',', '')
                    tunjangan_jabatan = tunjangan_jabatan.replace('.', '')
                    
                    # Coba konversi ke integer
                    tunjangan_jabatan = int(tunjangan_jabatan)
                    break  # Hentikan loop jika berhasil dikonversi
                except :
                    print("Masukkan harus berupa angka. Silakan coba lagi.")

            # Menambah data karyawan baru ke dalam list
            data_baru = {'ID Karyawan': int(id_baru), 'Nama': nama, 'NIK': nik, 'Jenis Kelamin': jenis_kelamin, 'No Telepon': no_telepon, 'Tanggal Mulai Bekerja': tanggal_mulai_bekerja, 'Jabatan': jabatan, 'Gaji Pokok': gaji, 'Tunjangan Jabatan': tunjangan_jabatan}
            data_karyawan.append(data_baru)
             
            # Menampilkan data karyawan setelah penambahan
            tampil_data()

        elif menu == 3:
            while True:
                try:
                    # Menampilkan data karyawan
                    tampil_data()
                    # Input ID Karyawan yang mau dihapus
                    id_hapus = int(input("Masukkan ID Karyawan yang ingin dihapus : "))
                    if len(str(id_hapus)) == 10:
                        for i in range(len(data_karyawan)):
                            if data_karyawan[i]['ID Karyawan'] == id_hapus :
                                # Menghapus karyawan sesuai dengan dengan ID yang di masukan
                                data_karyawan.pop(i)
                                break
                        break
                    else:
                        print("ID harus memiliki minimal 10 digit")

                except:
                    print("Masukan Angka")

            # Menampilkan data karyawan setelah dihapus
            tampil_data()

        elif menu == 4:
            tampil_data()
            while True:
                try:
                    id_update = int(input("Masukkan ID Karyawan yang ingin diupdate : "))
                    if len(str(id_update)) == 10 :
                        break
                    else:
                        print(f"ID {id_update} tidak ditemukan, silahkan coba lagi.")
                except:
                    print("Input Yang Dimasukan Tidak Sesuai")
                    
                    
            ketemu = False
            for i in range(len(data_karyawan)):
                if id_update == data_karyawan[i]['ID Karyawan']:
                    while True:
                        try:
                            print("\nSilahkan Pilih Data Yang ingin di update :\n")
                            print('List Menu Update:\n1. Nomor Telepon\n2. Jabatan\n3. Gaji Pokok\n4. Tunjangan Jabatan')
                            data_update = int(input("Masukkan angka yang ingin diupdate : "))
                            if data_update in [1, 2, 3, 4]:
                                break  # Keluar dari perulangan jika input valid
                            else:
                                print("Masukkan angka 1, 2, 3, atau 4 saja.")
                        except :
                            print("Input yang dimasukkan harus berupa angka.")

                    while True:
                        try:
                            if data_update == 1:
                                no_telepon_baru = input("Masukkan Nomor Telepon baru: ")
                                if len(no_telepon_baru) >= 10 and no_telepon_baru.isdigit():
                                    data_karyawan[i]['No Telepon'] = no_telepon_baru
                                    print("Data Karyawan berhasil diupdate!")
                                    break
                                else:
                                    print("Nomor Telepon harus memiliki minimal 10 angka dan bukan huruf.")
                            elif data_update == 2:
                                jabatan_baru = input("Masukkan Jabatan baru: ")
                                if len(jabatan_baru) >= 2:
                                    data_karyawan[i]['Jabatan'] = jabatan_baru
                                    print("Data Karyawan berhasil diupdate!")
                                    break
                                else:
                                    print("Harap masukkan minimal 2 huruf.")
                            elif data_update == 3:
                                gaji_baru = int(input("Masukkan Gaji Pokok baru: "))
                                data_karyawan[i]['Gaji Pokok'] = gaji_baru
                                print("Data Karyawan berhasil diupdate!")
                                break
                            elif data_update == 4:
                                tunjangan_baru = int(input("Masukkan Tunjangan Jabatan baru: "))
                                data_karyawan[i]['Tunjangan Jabatan'] = tunjangan_baru
                                print("Data Karyawan berhasil diupdate!")
                                break
                        except :
                            print("Input yang dimasukkan salah. Silakan coba lagi.")
                
                tampil_data()
                ketemu = True
                if ketemu == True :
                    break
 
        elif menu == 5:
            break

    except:
        print("masukan angka") 