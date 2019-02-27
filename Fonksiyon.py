def topla(sayi1, sayi2=0,ad="Bora"):
    sayi3 = sayi1 + sayi2
    sayi1 = 9
    return sayi1,sayi3

sayi1= 3
yenisayi,sonuc = topla(sayi1=sayi1,sayi2=5)
print(yenisayi, " ", sonuc)
sonuc = topla(sayi1=sayi1,ad="Mahmut")
print(sonuc)
print("Sayi1 değişti mi? Değeri:", sayi1)