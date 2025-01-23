import os

# Dizini belirtin
dizin_yolu = "/home/hzdmr/nodeapp"

# Göz ardı edilmesi gereken dosya ve klasörler
ignore_listesi = ["node_modules"]

# Dosya ve klasör adlarını alt klasörler dahil listeleme
with open("dosya_listesi.txt", "w", encoding="utf-8") as dosya:
    for kok_dizin, alt_dizinler, dosyalar in os.walk(dizin_yolu):
        # Ignore listedeki klasörleri alt_dizinler listesinden çıkar
        alt_dizinler[:] = [d for d in alt_dizinler if d not in ignore_listesi]
        
        # Bulunduğunuz dizini yazdır
        dosya.write(f"Klasör: {kok_dizin}\n")
        
        # Alt klasörleri yazdır (ignore kontrolü sonrası)
        for alt_dizin in alt_dizinler:
            dosya.write(f"  Alt Klasör: {alt_dizin}\n")
        
        # Dosyaları yazdır (ignore kontrolü ile)
        for dosya_adi in dosyalar:
            if dosya_adi not in ignore_listesi:
                dosya.write(f"  Dosya: {dosya_adi}\n")
        
        dosya.write("\n")

print("Tüm dizin ve dosya adları (ignore listesi uygulanarak) 'dosya_listesi.txt' dosyasına aktarıldı.")