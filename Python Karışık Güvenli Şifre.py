while True:
    import string
    from random import *

    characters = string.ascii_letters + string.punctuation  + string.digits

    len_characters = int(input("\nŞifrenizin uzunluğu kaç karakter olsun? Yazınız: "))

    for x in range(len_characters):
        password =  "".join(choice(characters))
        print (password, end="")
