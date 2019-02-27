# Program akışı temel olarak bir deyimin çalıştırılıp çalıştırılmayacağına
# karar vermektir.
# Program akışı bir ağacın dalları gibi ikiye ayrıldığı (sonra birleştiği)
# için buna dallanma (branching) adı verilir
x = int ( input("Bir tam sayı girin.") )
if x > 0:
    # Dallanmalarda çalıştırılacak kod blokları bir sekme (tab) kadar girintili yazılır. 
    print("Pozitif")
    if x>5:
        print("bir de 5 den büyük")
elif x > -3:
    print ("-3 den büyük")
else:
    # Dallanmalarda çalıştırılacak kod blokları bir sekme (tab) kadar girintili yazılır. 
    print ("Pozitif değil")

# Aynı düşünce yapısı ile bu kararı defalarca verip deyimi belirli
# bir koşula uyduğu müddetçe çalıştırmak mümkündür
# Bunlara döngü (loop) adı verilir
sayac = 0
while sayac < 3:
    # Döngülerde de çalıştırılacak kod blokları bir sekme (tab) kadar girintili yazılır. 
    print("Sayac:", sayac)
    sayac = sayac + 1
# Döngüden çıkıp, önceki akış hattına dönünce girintili yazmayı bırakırız
print("Döngüden çıktık.")
print("Sayac:", sayac)

# Laboratuvar uygulaması: Kullanıcının girdiği (1000'den küçük) bir tam sayının
# asal olup olmadığını söyleyen bir program geliştirelim

# Döngülerle çalışmak bize daha çok veriyle çalışmak anlamına gelir.
# Tuple sabit boyutlu bir kaptır. İndekslenmiştir. Bu nedenle sıralı (sequenced)
# bir kap (container) olduğunu söylememiz gerekir. 
gunler = ("Pazartesi","Salı","Çarşama","Perşembe","Cuma","Cumartesi","Pazar")
for bugun in gunler:
    print ("Bugün: ", bugun)

# Not: tuple içerikleri birleştirilebilir tuple1 + tuple2 şeklinde

# Kesit alma önemli bir tekniktir. Liste ve tuple larda kullanılır
kimlik = ["Bora", "Güngören", "Yönetici Ortak", "Portakal Teknoloji", 1]
kesit = kimlik[0:2] # 0'dan başla 2'den küçük olduğunca ilerle
print (kesit)
kesit2 = kimlik[2:] #2'den başla sona kadar al
print(kesit2)

# Listeler değişken boyutlu ve indeksli kaplardır.
# İçindeki elemanları aramak, kaldırmak, yeni eleman eklemek mümkündür.

def cuzdanToplam(cuzdan):
    toplam = 0
    for para in cuzdan:
        toplam = toplam + para
    return toplam

cuzdan = [1, 5, 10, 10, 20, 50, 100]
print("Cüzdan:", cuzdan)
toplam = cuzdanToplam(cuzdan)
print ("Toplamda ", toplam, " TL var")

# Para ekleyelim
cuzdan.insert(4,200) # Eklediğimiz elemanın indeksi 4 olacak, diğerleri kayacak
print("Cüzdan:", cuzdan)
toplam = 0
for para in cuzdan:
    toplam = toplam + para
print ("Toplamda ", toplam, " TL var")

ceptenCikan = [10, 10, 5, 1]
cuzdan.extend(ceptenCikan)
print("Cüzdan:", cuzdan)
toplam = 0
for para in cuzdan:
    toplam = toplam + para
print ("Toplamda ", toplam, " TL var")

del cuzdan[0:1]
print (cuzdan)
#uzunluk = len(cuzdan)
#del cuzdan[uzunluk-3:uzunluk-1]
del cuzdan[-3:-1]
print (cuzdan)
# Listeler ve tuple lar da birer değişkendir dolayısı ile
# karıştırılarak kullanılabilir
koordinatlar = [ (0,0), (1,2), (4,5)] # Liste içindeki her eleman bir tuple
alan = 0
for x,y in koordinatlar:
        alan = alan + x*y
print("Alan: ", alan)

# Aynı örneği öbür türlü düşünsek, tuple içinde her eleman bir liste olsa?
koordinatlar = ( [0,0], [1,2], [4,5]) 
alan = 0
for x,y in koordinatlar:
        alan = alan + x*y
print("Alan: ", alan)
# Kod çalıştı, ama bunu bunlardan hangisi yapılan işin doğasına (alan hesabına)
# daha uygun olurdu? Ne zaman tuple ne zaman list seçmeli? 

# İki tuple (liste de olurdu) varsa
xler = (0, 1, 4)
yler = (0, 2, 5)
# then we you can use the zip function
zipli = zip(xler,yler)
zipliliste = list(zipli)
print (zipliliste)
alan = 0
for x,y in koordinatlar:
        alan = alan + x*y
print("Alan: ", alan)

# Sözlük veri yapısı anahtar-değer (key-value) ikilisi saklamak için kullanılır
adresler = {}
adresler["ODTÜ"] = "gbora@metu.edu.tr"
adresler["Bilkent"] = "bora.gungoren@bilkent.edu.tr"
adresler["Gmail"] = "bora.gungoren@gmail.com"

for k in adresler:
    print("Anahtar:\t", k, "\t\t", "Değer:", adresler[k])

for k,v in adresler.items():
    print("Anahtar:\t", k, "\t\t", "Değer:", v)

# Laboratuvar uygulaması: Kullanıcının girdiği sayıda adres için o adresin çevre koordinatlarını kaydeden bir
# program oluşturalım. 

