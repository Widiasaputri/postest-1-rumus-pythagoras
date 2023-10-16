# Login sederhana
print('Nama:Widia Saputri')
print('NIM:2309116019 (Ganjil)')
print('Kelas:A SI 23\n')

print('1. Sisi Miring')
print('2. Sisi Tegak')
print('3. Sisi Alas\n')

pilihan = int(input('pilih sisi yang ingin diselesaikan:\n'))

if pilihan == 1:
    a = int(input('Sisi Tegak:'))
    b = int(input('Sisi Alas:'))
    c = a**2 + b**2
    print("hasil: ", c)
elif pilihan == 2:
    a = int(input('Sisi Miring:'))
    b = int(input('Sisi Alas:'))
    c = a**2 - b**2
    print('hasil: ', c)
elif pilihan == 3:
    a = int(input('Sisi Miring:' ))
    b = int(input('Sisi Tegal:'))
    c = a**2 - b**2
    print('hasil: ', c)
else:
    print('maaf, tidak ada dipilihan')




