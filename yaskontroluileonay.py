import tkinter as tk
from tkinter import messagebox

def on_submit():
    isim = entry_isim.get().strip().title()
    soyisim = entry_soyisim.get().strip().capitalize()
    sehir = entry_sehir.get().strip().title()
    yas_str = entry_yas.get().strip()
    
    #Boş alan kontrolü
    if not isim or not soyisim or not sehir or not yas_str:
        messagebox.showerror("Eksik Bilgi", "Lütfen tüm bilgileri eksiksiz giriniz.")
        return
    
    #Yaş kontrolü
    try:
        yas = int(yas_str)
        if yas <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Geçersiz Yaş", "Lütfen geçerli bir yaş giriniz.")
        return
    
    #İsim, soyisim ve şehir kontrolü
    if not (isim.isalpha() and soyisim.isalpha() and sehir.isalpha()):
        messagebox.showerror("Geçersiz Giriş", "Lütfen sadece harf içeren geçerli bir isim, soyisim ve şehir giriniz.")
        return
    
    #Ekranda çıktıyı gösterme
    result_text.set(f"Merhaba, {isim} {soyisim}, {yas} yaşındasın ve {sehir} 'da yaşıyorsun.\n")
    if yas >= 20:
        result_text.set(result_text.get() + "Programımıza katılabilirsin.")
    else:
        result_text.set(result_text.get() + "Ama maalesef, programımız sadece 20 yaş ve üstü için geçerlidir.")

#Ana pencereyi oluştur
root = tk.Tk()
root.title("Kullanıcı Bilgisi Girişi")

# İsim, Soyisim, Yaş ve Şehir etiketleri ve giriş alanları
tk.Label(root, text="İsminizi Giriniz: ").grid(row=0, column=0, padx=10, pady=5)
entry_isim = tk.Entry(root)
entry_isim.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Soyisminizi Giriniz: ").grid(row=1, column=0, padx=10, pady=5)
entry_soyisim = tk.Entry(root)
entry_soyisim.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Yaşınızı Giriniz: ").grid(row=2, column=0, padx=10, pady=5)
entry_yas = tk.Entry(root)
entry_yas.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Yaşadığınız Şehri Giriniz: ").grid(row=3, column=0, padx=10, pady=5)
entry_sehir = tk.Entry(root)
entry_sehir.grid(row=3, column=1, padx=10, pady=5)

#Sonuç gösterme metni
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

#Gönder butonu
submit_button = tk.Button(root, text="Gönder", command=on_submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Tkinter pencerenin sürekli açık kalmasını sağla
root.mainloop()
