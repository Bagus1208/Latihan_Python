angka = int(input('Input sebuah angka antara 1-12: '))

bulan = ''
loop = ''
 
if angka == 1:
    bulan = 'Januari'

elif angka == 2:
    bulan = 'Februari'

elif angka == 3:
    bulan = 'Maret'

elif angka == 4:
    bulan = 'April'

elif angka == 5:
    bulan = 'Mei'

elif angka == 6:
    bulan = 'Juni'

elif angka == 7:
    bulan = 'Juli'

elif angka == 8:
    bulan = 'Agustus'

elif angka == 9:
    bulan = 'September'

elif angka == 10:
    bulan = 'Oktober'

elif angka == 11:
    bulan = 'November'

elif angka == 12:
    bulan = 'Desember'

else:
    print('angka yang anda masukan tidak valid')


if 1 <= angka <= 12:
    print('Bulan ke ' + str(angka) + ' adalah : ' + str(bulan))

