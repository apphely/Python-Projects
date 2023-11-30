# Belirlediğiniz bir klasördeki istemediğiniz uzantıya ship bütün dosyaları silebileceğiniz bir python kodu.
import os

# Kullanıcıdan klasör adını ve silmek istediği dosya uzantısını al
dir_name = input("Lütfen klasör adını girin: ")
file_extension = input("Silmek istediğiniz dosya uzantısını girin (örn: zip/opf): ")

# Kullanıcının girdiği klasör adını kontrol et
if not os.path.exists(dir_name):
    print(f"{dir_name} adında bir klasör bulunamadı.")
else:
    # Klasördeki belirtilen uzantılı dosyaları sil
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(f".{file_extension}"):
            os.remove(os.path.join(dir_name, item))
    print(f".{file_extension} uzantılı dosyalar silindi.")
