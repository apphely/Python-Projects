from PIL import Image
import os

# Klasördeki tüm dosyaları listele
klasor_yolu = "x:\.Çalışmalarım ve Projelerim\Kodlama\Python Projeler\WebP Dönüştürme ve Sıkıştırma/"  # Webp dosyalarının bulunduğu klasörün yolu
hedef_kalite = 20  # %20 sıkıştırma kalitesi

# Klasördeki tüm dosyaları al
dosyalar = os.listdir(klasor_yolu)

# Webp dosyalarını işle
for dosya_adı in dosyalar:
    if dosya_adı.endswith(".webp"):
        dosya_yolu = os.path.join(klasor_yolu, dosya_adı)

        # Webp dosyasını aç
        im = Image.open(dosya_yolu)

        # Kaliteyi ayarla ve kaydet
        im.save(dosya_yolu, "webp", quality=hedef_kalite)

print("Webp dosyaları %20 kalitesinde sıkıştırıldı.")
