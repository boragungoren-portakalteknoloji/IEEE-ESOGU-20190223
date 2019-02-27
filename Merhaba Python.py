# Python'a girerken önce metin değişkenleri ile çalışalım 
print("Merhaba Eskişehir")
merhabaString = "Merhaba Eskişehir"
print(merhabaString)
print("Adım:", " ", "Bora")
adString = "Adım: Bora"
ayrismisString = adString.split()
# print(ayrismisString)
print(ayrismisString[0], " ", ayrismisString[1])
# 0, 1, 2, ... Programlama dillerinde genelde 0'dan başlayarak sayıyoruz.

# Sayısal değerler söz konusu olunca,
# değişkenlerin türünü onlara atanan değer belirler

x = 0
y = 1
z = x + 2 * y
print("x: ", x, "y: ", y, "z: ", z)
z = 5 / 2
print ("z:", z)
# Eğer bir sayının gerçek sayı olmasını istiyorsak
z = float (2)
print ("z:", z)
# Eğer bir sayının tam sayı olmasını istiyorsak
z = int (5/2)
print ("z:", z)
# parantezler, işlem üstünlükleri, vs geçerli
z = (2 * (x-1)) * (3*y-2) / z
#      -2 * 1 / 2
print ("İşlem sonucu, z: ",z)

# Mantıksal işlemler için Boolean türü değişkenler kullanılabilir
acikmi = True
kapalimi = not acikmi
print("Kapalı mı? ", kapalimi)
yaAciktirYaKapali = acikmi or kapalimi
hemAcikHemKapali = acikmi and kapalimi
print("Ya açıktır ya kapalı.", yaAciktirYaKapali)
print("Hem açık hem kapalı", hemAcikHemKapali)
# Bu tür işlemleri daha sonra dallanmalarda kullanacağız

# Kullanıcıdan komut satırı girdisi almak gerekirse
kullaniciAdi = input("Adınız ne? ")
print("Teşekkürler ",kullaniciAdi, ". Tanıştığımıza memnun oldum.")

# Laboratuvar uygulaması: Kullanıcıdan üç sayı alıp
# onların toplamını ve ortalamasını yazan bir program geliştirelim
