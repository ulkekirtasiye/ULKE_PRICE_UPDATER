import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("ULKE PRICE UPDATER")
app.geometry("900x500")

tedarikci = ""
akinsoft = ""


def tedarikci_sec():
    global tedarikci
    tedarikci = filedialog.askopenfilename(
        title="Tedarikçi Excel Dosyası",
        filetypes=[("Excel", "*.xlsx *.xls")]
    )
    lbl1.configure(text=tedarikci)


def akinsoft_sec():
    global akinsoft
    akinsoft = filedialog.askopenfilename(
        title="Akınsoft Excel Dosyası",
        filetypes=[("Excel", "*.xlsx *.xls")]
    )
    lbl2.configure(text=akinsoft)


def fiyat_guncelle():

    if not tedarikci or not akinsoft:
        print("Lütfen iki Excel dosyasını seçin.")
        return

    print("Tedarikçi :", tedarikci)
    print("Akınsoft  :", akinsoft)


baslik = ctk.CTkLabel(
    app,
    text="ULKE PRICE UPDATER",
    font=("Arial", 28, "bold")
)
baslik.pack(pady=20)

btn1 = ctk.CTkButton(
    app,
    text="Tedarikçi Excel Seç",
    command=tedarikci_sec
)
btn1.pack(pady=10)

lbl1 = ctk.CTkLabel(app, text="Dosya seçilmedi")
lbl1.pack()

btn2 = ctk.CTkButton(
    app,
    text="Akınsoft Excel Seç",
    command=akinsoft_sec
)
btn2.pack(pady=20)

lbl2 = ctk.CTkLabel(app, text="Dosya seçilmedi")
lbl2.pack()

btn3 = ctk.CTkButton(
    app,
    text="Fiyatları Güncelle",
    fg_color="green",
    command=fiyat_guncelle
)
btn3.pack(pady=30)

app.mainloop()