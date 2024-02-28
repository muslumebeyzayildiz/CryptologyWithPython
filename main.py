from KaydirmaliSifreleme import kaydirmali_sifrele, kaydirmali_sifreCoz # KaydirmaliSifreli.py dosyasını içe aktarma
from Sezar import sezar_sifrele, sezar_sifreCoz
from DogrusalSifrelemeAffine import affine_sifrele,affine_desifrele
def main():

    kelime = input("Lütfen SEZAR ŞİFRELEME İLE şifrelemek istediğiniz kelimeyi girin: ")
    sifrelenmis_kelime = sezar_sifrele(kelime)
    print("Şifrelenmiş hali:", sifrelenmis_kelime)
    print("Deşifrelenmiş hali:", sezar_sifreCoz(sifrelenmis_kelime))

#######################

    metin = input("Lütfen KAYDIRMALI ŞİFRELEME İLE şifrelemek istediğiniz metni girin: ")
    key = int(input("Lütfen bir kaydırma anahtarı girin: "))
    sifrelenmis_metin = kaydirmali_sifrele(metin, key)
    print("Şifrelenmiş hali:", sifrelenmis_metin)
    print("Deşifrelenmiş hali:", kaydirmali_sifreCoz(metin,key))

#######################

    anahtar_A = int(input("Lütfen bir anahtar A değeri girin: "))
    anahtar_B = int(input("Lütfen bir anahtar B değeri girin: "))
    metin = input("Lütfen şifrelemek istediğiniz metni girin: ")
    sifreli_metin = affine_sifrele(metin, anahtar_A, anahtar_B)
    print("Şifrelenmiş metin:", sifreli_metin)

    desifrelenmis_metin = affine_desifrele(sifreli_metin, anahtar_A, anahtar_B)
    print("Deşifrelenmiş metin:", desifrelenmis_metin)


if __name__ == "__main__":
    main()
