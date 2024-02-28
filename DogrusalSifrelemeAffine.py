def affine_sifrele(metin: str, anahtar_A: int, anahtar_B: int):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    sifreli_metin = ""
    alfabe_uzunluk = len(alfabe)
    for harf in metin:
         if harf.isalpha():
             i = (anahtar_A * alfabe.index(harf) + anahtar_B) % alfabe_uzunluk
             sifreli_metin += alfabe[i]
         else:
            sifreli_metin += harf
    return sifreli_metin


def affine_desifrele(metin: str, anahtar_A: int, anahtar_B: int):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    alfabe_uzunluk = len(alfabe)
    carpimsal_ters = kontrolet_affine(alfabe_uzunluk, anahtar_A)

    if carpimsal_ters == -1:
        return "Çarpımsal Ters Bulunamadı"

    desifrelenmis_metin = ""
    for harf in metin:
        if harf.isalpha():
            i = (carpimsal_ters * (alfabe.index(harf) - anahtar_B)) % alfabe_uzunluk
            desifrelenmis_metin += alfabe[i]
        else:
            desifrelenmis_metin += harf
    return desifrelenmis_metin


def kontrolet_affine(alfabe_uzunluk: int, anahtar_A: int):
    carpimsal_ters = -1
    i = 0

    while i < alfabe_uzunluk:
        if (anahtar_A * i) % alfabe_uzunluk == 1:
            carpimsal_ters = i
            break
        i += 1

    return carpimsal_ters

