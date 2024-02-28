def kaydirmali_sifrele(metin, key):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    sifrelenmis_metin = ''
    for harf in metin:
        if harf.lower() in alfabe:
            harf_index = alfabe.index(harf.lower())
            sifrelenmis_index = (harf_index + key) % len(alfabe)
            sifrelenmis_metin += alfabe[sifrelenmis_index]
        else:
            sifrelenmis_metin += harf
    return sifrelenmis_metin

def kaydirmali_sifreCoz(metin, key):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    sifrelenmis_metin = ''
    for harf in metin:
        if harf.lower() in alfabe:
            harf_index = alfabe.index(harf.lower())
            sifrelenmis_index = (harf_index - key) % len(alfabe)
            sifrelenmis_metin += alfabe[sifrelenmis_index]
        else:
            sifrelenmis_metin += harf
    return sifrelenmis_metin
