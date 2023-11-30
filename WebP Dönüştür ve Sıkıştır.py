# .jpg, .png ve .jpeg uzantılı dosyaları .webp'ye dönüştüp sıkıştırma işlemi yaparak alandan tasarruf sağlar. Web siteleri için birebirdir.

from PIL import Image
import os

# Giriş klasörünü tanımlayın
giris_klasoru = 'x:\WebP Dönüştürme ve Sıkıştırma/'

# Giriş klasöründeki tüm dosyaları alın
dosya_listesi = os.listdir(giris_klasoru)

for dosya_adı in dosya_listesi:
    if dosya_adı.endswith(('.jpg', '.jpeg', '.png')):
        # Giriş dosyasının yolunu oluşturun
        giris_yolu = os.path.join(giris_klasoru, dosya_adı)
        
        # Resmi yükle ve webp'ye dönüştür
        im = Image.open(giris_yolu)
        webp_yolu = os.path.splitext(giris_yolu)[0] + '.webp'
        im.save(webp_yolu, 'WEBP', quality=50)  # Kalite ayarı

print("Tüm fotoğraflar webp formatına dönüştürüldü ve aynı yere kaydedildi.")
