import os

while True:
    klasor = input("Aranacak KLasör: ")  # aranacak kök dizin yolu
    keyword = input("Aranacak Kelime: ")  # kullanıcıdan bir anahtar kelime isteniyor
    dosya_sayaci = 0  # bulunan dosyaların sayısını tutmak için bir sayaç başlatılıyor

    for root, dirs, files in os.walk(klasor, onerror=None):  # kök dizini tara
        for filename in files:  # mevcut dizindeki dosyaları işle
            file_path = os.path.join(root, filename)  # dosya yolunu oluştur
            try:
                with open(file_path, "rb") as f:  # dosyayı okumak için aç
                    # dosyayı satır satır oku
                    for line in f:  # satır numaralarını gerekiyorsa for i, line in enumerate(f) kullanın
                        try:
                            line = line.decode("utf-8")  # içeriği utf-8'e çözmeye çalış
                        except ValueError:  # çözme başarısız olduysa satırı atla
                            continue
                        if keyword in line:  # anahtar kelime mevcut satırda bulunuyorsa...
                            print(file_path)  # dosya yolunu yazdır
                            dosya_sayaci += 1  # bulunan dosyaların sayısını artır
                            break  # dosyanın geri kalanını işlemeye gerek yok
            except (IOError, OSError):  # okuma ve izin hatalarını yoksay
                pass
    # Toplam bulunan dosya sayısını yazdır
    print(f"Toplam {dosya_sayaci} dosya bulundu.\n\n")