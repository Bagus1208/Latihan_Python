n = int(input('Ingin menampilkan berapa bilangan? = ')) 
count = 0
b1 = 1
b2 = 1

while count < n:
   print(b1)
   bilangan_terakhir = b1 + b2
   b1 = b2
   b2 = bilangan_terakhir
   count += 1