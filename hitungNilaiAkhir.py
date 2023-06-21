nilaiAkhir = ''

def ringkasan (nilaiHuruf):
    if nilaiAkhir >= 70:
        print('Nilai Huruf       : ' + nilaiHuruf)
        print('Selamat anda dinyatakan lulus')
    
    elif nilaiAkhir <= 69:
        print('Nilai Huruf       : ' + nilaiHuruf)
        print('Anda dinyatakan tidak lulus')

print('Menghitung Nilai Akhir')
print('======================')
print('')

tugas = float(input('Input nilai Tugas : '))
uts = float(input('Input nilai UTS   : '))
uas = float(input('Input nilai UAS   : '))

nilaiAkhir = (0.2 * tugas) + (0.3 * uts) + (0.5 * uas)
print('Nilai Akhir       : ' + str(nilaiAkhir))


if 91.0 <= nilaiAkhir <= 100:
    ringkasan('A')
elif 76 <= nilaiAkhir <= 90.9:
    ringkasan('B')
elif 70 <= nilaiAkhir <= 75.9:
    ringkasan('C')
elif 61 <= nilaiAkhir <= 69.9:
    ringkasan('C')
elif 41 <= nilaiAkhir <= 60.9:
    ringkasan('D')
elif 0 <= nilaiAkhir <= 40.9:
    ringkasan('E')

