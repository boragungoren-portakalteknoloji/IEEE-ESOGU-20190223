import os

# Here is an absolute path
winabspath = "C:\\Users\\Bora\\OneDrive\\Desktop"
linabspath = "/home/bora/"

winprojectdir = "IEEE ESOGU"
linprojectdir = "IEEE ESOGU"

infile = "girdi.txt"
outfile = "cikti.txt"

inpath = os.path.join(winabspath, winprojectdir, infile)
outpath = os.path.join(winabspath, winprojectdir, outfile)

satirlar = []
noktalar = []
with open(inpath, 'r') as girdinesnesi:
        satirlar = girdinesnesi.readlines()

for satir in satirlar:
    kolonlar = satir.split()
    x = float ( kolonlar[0] )
    y = float ( kolonlar[1] )
    nokta = (x,y)
    noktalar.append(nokta)

ciktinesnesi = open(outpath, 'w')

for x,y in noktalar:
    print("x:",x," y:", y)
    z = x + y
    metin = str(z)
    ciktinesnesi.write(metin)
    ciktinesnesi.write("\n")

ciktinesnesi.close()

# Laboratuvar Çalışması: verilen x ve y değerlerini iki ait değişkene ait gözlemler olarak ele alarak
# bunların dağılım özelliklerini (ortalama ve ortanca) hesaplayalım. 
