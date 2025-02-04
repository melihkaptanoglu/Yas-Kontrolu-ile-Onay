
while True:
        isim=input("İsminizi Giriniz: ")
        if all(char.isalpha() or char.isspace() for char in isim):
            break
        else :
            print("Lütfen geçerli bir isim giriniz.(Sadece Harf İçermeli!)")  

while True:
    soyisim= input("Soyisminizi Giriniz: ")      
    if all(char.isalpha() or char.isspace() for char in soyisim):
        break
    else :
        print("Lütfen geçerli bir soyisim giriniz.(Sadece Harf İçermeli!)")  


while True:
    try:
        yas=int(input("Yaşınızı Giriniz: "))
        if yas>0 :
            break
        else:
            print("Lütfen geçerli bir yaş giriniz.")
    except ValueError:  # Eğer yaş için geçerli bir sayı girilmezse
        print("Lütfen geçerli bir yaş giriniz.")


while True:
    sehir= input("Yaşadığınız Şehri Giriniz: ")      
    if all(char.isalpha() or char.isspace() for char in sehir):
        break
    else :
        print("Lütfen geçerli bir şehir adı giriniz.(Sadece Harf İçermeli!)")  



 # isim= isim.strip()
 # isim= isim.capitalize()
 # soyisim= soyisim.capitalize()
 # soyisim= soyisim.strip()
 # sehir= sehir.strip()
 # sehir= sehir.capitalize()

isim = isim.strip().title()
soyisim = soyisim.strip().capitalize()
sehir = sehir.strip().title()

print(f"Merhaba, {isim} {soyisim}, {yas} yaşındasın ve {sehir} `da yaşadığını belirttin programımız çevrimiçi erişime açık.")


if yas>=20 :
    print("Programımıza katılabilirsin.")
else:
    print("Ama maalesef,programımız sadece 20 yaş ve üstü için geçerlidir.")
        
