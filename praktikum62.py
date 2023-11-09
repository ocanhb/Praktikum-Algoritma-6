def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

def bulan_tahun(bulan, tahun):
    if bulan == 2:  
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in [4, 6, 9, 11]: 
        return 30
    else:
        return 31

while True:
    bulan = int(input("Masukkan angka bulan (1-12) atau 0 untuk menghentikan program: "))
    if bulan == 0:
       break
    if 1 <= bulan <= 12:
        if bulan == 2:
            tahun = int(input("Masukkan tahun e.g, 2021 : "))
            if tahun > 2021:
                print("Masukkan tahun hingga 2021.")
                continue
            jumlah_hari = bulan_tahun(bulan, tahun)
        else:
            jumlah_hari = bulan_tahun(bulan, None)
        
        print(f"Jumlah hari dalam bulan {bulan} adalah {jumlah_hari} hari.")
    else:
        print("Masukkan bulan yang valid (1-12).")
