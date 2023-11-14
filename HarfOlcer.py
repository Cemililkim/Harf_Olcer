kelime = input("Metin giriniz: ")

sesliharf_sayac = 0
sessizharf_sayac = 0

sesliharf = "aıoueiöü"
sessizharf = "bcçdfgğhjklmnprsştvyz"

for harf in kelime.lower():
    if harf in sesliharf:
        sesliharf_sayac += 1
    elif harf in sessizharf:
        sessizharf_sayac += 1


print(f"Sesli harf sayısı: {sesliharf_sayac}")
print(f"Sessiz harf sayısı: {sessizharf_sayac}")
print(f"Toplam harf sayısı: {sesliharf_sayac + sessizharf_sayac} ")

input("Çıkış yapmak için bir tuşa basın")
