gol = input('Input Golongan karyawan    : ')
pend = input('Input pendidikan karyawan     : ' )

if gol == 'A' or gol == 'a':
    if pend == 'SMA' or pend == 'sma':
        gaji = 5000000
        print('Gaji yang didapat adalah         : ' + str(gaji))
    elif pend == 'S1' or pend == 's1':
        gaji = 7000000
        print('Gaji yang didapat adalah         : ' + str(gaji))
    else:
        print('Anda salah memasukan input')

elif gol == 'B' or gol == 'b':
    if pend == 'SMA' or pend == 'sma':
        gaji = 7000000
        print('Gaji yang didapat adalah         : ' + str(gaji))
    elif pend == 'S1' or pend == 's1':
        gaji = 11000000
        print('Gaji yang didapat adalah         : ' + str(gaji))
    else:
        print('Anda salah memasukan input')

else:
    print('Anda salah memasukan input')
