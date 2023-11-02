def rata_rata(nilai_a, nilai_b):
    rata_rata = (nilai_a + nilai_b) / 2
    return rata_rata

nilai_a = float(input("Masukkan nilai a: "))
nilai_b = float(input("Masukkan nilai b: "))

hasil_rata_rata = rata_rata(nilai_a, nilai_b)

print(f"Rata-ratanya adalah {hasil_rata_rata}")
