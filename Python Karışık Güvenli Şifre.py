# Her türlü harfi ve karakteri kullanarak istediğiniz uzunlukta güvenli şifreler oluşturur.
while True: # Sürekli döngüye sokar.
    import string
    from random import *

    characters = string.ascii_letters + string.punctuation  + string.digits # Harfler, sayılar ve işaretleri kullanarak şifreleme karakterlerini belirler.

    len_characters = int(input("\nŞifrenizin uzunluğu kaç karakter olsun? Yazınız: ")) #Şifre uzunluğu için kullanıcıdan yazmasını ister.

    for x in range(len_characters):
        password =  "".join(choice(characters))
        print (password, end="")
