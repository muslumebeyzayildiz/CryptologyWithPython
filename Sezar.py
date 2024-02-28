def sezar_sifrele(metin):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    sifrelenmis_metin = ''
    for harf in metin:
        if harf.lower() in alfabe:
            harf_index = alfabe.index(harf.lower()) #harflerin alfabe içindeki indeksini döndğrüyor
            sifrelenmis_index = (harf_index + 3) % 29
            sifrelenmis_metin += alfabe[sifrelenmis_index]
        else:
            sifrelenmis_metin += harf
    return sifrelenmis_metin
def sezar_sifreCoz(metin):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    sifrelenmis_metin = ''
    for harf in metin:
        if harf.lower() in alfabe:
            harf_index = alfabe.index(harf.lower()) #harflerin alfabe içindeki indeksini döndğrüyor
            sifrelenmis_index = (harf_index - 3) % 29
            sifrelenmis_metin += alfabe[sifrelenmis_index]
        else:
            sifrelenmis_metin += harf
    return sifrelenmis_metin
