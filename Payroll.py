# ============================================================
# Sistem Penggajian Karyawan (Payroll System)
# Materi: Class, Encapsulation, Inheritance, Polymorphism
# ============================================================


class Karyawan:
    """Superclass untuk semua jenis karyawan."""

    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama                    # public
        self.id_karyawan = id_karyawan      # public
        self.__gaji_pokok = 0               # private
        self.gaji_pokok = gaji_pokok        # lewat setter agar divalidasi

    # Getter
    @property
    def gaji_pokok(self):
        return self.__gaji_pokok

    # Setter
    @gaji_pokok.setter
    def gaji_pokok(self, nilai):
        if nilai <= 0:
            print(f"[PERINGATAN] Gaji pokok tidak valid ({nilai}). "
                  f"Nilai harus lebih besar dari 0.")
        else:
            self.__gaji_pokok = nilai

    def hitung_gaji_total(self):
        return self.__gaji_pokok

    def tampilkan_info(self):
        print(f"Nama          : {self.nama}")
        print(f"ID Karyawan   : {self.id_karyawan}")
        print(f"Gaji Pokok    : Rp {self.gaji_pokok:,.0f}")


class KaryawanTetap(Karyawan):
    """Child class: karyawan dengan tunjangan jabatan."""

    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan          # public

    # Overriding
    def hitung_gaji_total(self):
        return self.gaji_pokok + self.tunjangan

    # Overriding
    def tampilkan_info(self):
        print("=== Karyawan Tetap ===")
        super().tampilkan_info()
        print(f"Tunjangan     : Rp {self.tunjangan:,.0f}")
        print(f"Total Gaji    : Rp {self.hitung_gaji_total():,.0f}")


class KaryawanKontrak(Karyawan):
    """Child class: karyawan dengan upah lembur."""

    def __init__(self, nama, id_karyawan, gaji_pokok, jam_lembur, tarif_lembur):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.jam_lembur = jam_lembur        # public (int)
        self.tarif_lembur = tarif_lembur    # public

    # Overriding
    def hitung_gaji_total(self):
        return self.gaji_pokok + (self.jam_lembur * self.tarif_lembur)

    # Overriding
    def tampilkan_info(self):
        print("=== Karyawan Kontrak ===")
        super().tampilkan_info()
        print(f"Jam Lembur    : {self.jam_lembur} jam")
        print(f"Tarif Lembur  : Rp {self.tarif_lembur:,.0f} / jam")
        print(f"Total Lembur  : Rp {self.jam_lembur * self.tarif_lembur:,.0f}")
        print(f"Total Gaji    : Rp {self.hitung_gaji_total():,.0f}")


# ============================================================
# MAIN PROGRAM
# ============================================================
if __name__ == "__main__":
    # 1. Buat objek
    karyawan_tetap = KaryawanTetap("Angga Ahmad Fahreza", "KT-001", 9000000, 2000000)
    karyawan_kontrak = KaryawanKontrak("Wein Ayyubilukman", "KK-001", 5000000, 20, 50000)

    # 2. Simpan ke dalam list
    daftar_karyawan = [karyawan_tetap, karyawan_kontrak]

    # 3. Demonstrasi Polymorphism
    print("##### DEMONSTRASI POLYMORPHISM #####\n")
    for karyawan in daftar_karyawan:
        karyawan.tampilkan_info()
        print("-" * 40)

    # 4. Demonstrasi Encapsulation
    print("\n##### DEMONSTRASI ENCAPSULATION #####\n")

    print(">> Gaji pokok awal Angga:", karyawan_tetap.gaji_pokok)

    print("\n>> Mengubah gaji pokok dengan nilai TIDAK valid (-1000000):")
    karyawan_tetap.gaji_pokok = -1000000

    print("\n>> Mengubah gaji pokok dengan nilai VALID (9000000):")
    karyawan_tetap.gaji_pokok = 9000000

    print("\n>> Info setelah perubahan:\n")
    karyawan_tetap.tampilkan_info()