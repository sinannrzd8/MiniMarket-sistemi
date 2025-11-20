import time
import json
import os
from pathlib import Path

t=0
user_balance=100.0

DATA_DIR = Path('data')
DEFAULT_USERS = [
    {"balance": 100.0, "failed_attempts": 0, "lock_until": None}
]

DEFAULT_PRODUCTS = {
    "Geyimler": [
        {"id": 1, "name": "T-Shirt", "price": 12.50},
        {"id": 2, "name": "Hoodie", "price": 45.00},
        {"id": 3, "name": "Jeans",  "price": 60.00}
    ],
    
    "İdman": [
        {"id": 1, "name": "Ball", "price": 7.34},
        {"id": 2, "name": "Dumbbell", "price": 16.25},
        {"id": 3, "name": "Boxing Pole", "price": 29.99}
    ],

    "Elektronika": [
        {"id": 1, "name": "Mouse", "price": 6.47},
        {"id": 2, "name": "Mouse Pad", "price": 11.45},
        {"id": 3, "name": "Keyboard", "price": 44.59}
    ]
}

favourities = []
sebet = []
history = []

print("==========Xoş Gəlmisiniz==========")

while t==0:
    user_name='Siccin'
    user_password=1234
    for i in range(3):
        username = input('Istifadəçi adını daxil edin : ')
        password = int(input("İstifadəçi parolunu daxil edin : "))
        if user_name==username and user_password==password:
            print("Giriş Uğurludur....")
            history.append("Giriş Uğurludur....")
            break
        else:
            print("İstifadəçi Tapılmadı!!!\n")
            history.append("Giriş Uğursuzdur...")
    else:
        print("Sən getdin bloka😏 (10 saniyəlik)")

        time.sleep(10)
        continue

    def list_products(products, category):
        items = products.get(category, [])
        print('\n[Məhsul ID]   Ad                       Qiymət (AZN)')
        for p in items:
            print(f"[{p['id']}] {p['name']:<22} {p['price']:.2f}")
        return items

    while True:
        print("\n=== Əsas menyu ===")
        print("1) Kateqoriyalar\n"
            "2) Səbətim (gözləyənlər)\n"
            "3) Favoritlərim \n"
            "4) Tarixçə \n"
            "5) Settings (şifrəni dəyiş) \n"
            "6) Balansımı göstər \n"
            "0) Çıxış \n")
        
        secim = int(input())

        if secim==0:
            print("Çüsdüm çıx get😭...")
            exit()

        if secim==1:
            print(DEFAULT_PRODUCTS)
            for kat in DEFAULT_PRODUCTS:
                print("---", kat)
            category = input("Kateqoriyanı daxil et : ")
            if category == "İdman":
                items = list_products(DEFAULT_PRODUCTS, "İdman")
                
                product_id = int(input("Məhsul ID daxil edin: "))
                
                secilen = None
                for p in items:
                    if p["id"] == product_id:
                        secilen = p
                        break

                if secilen is None:
                    print("Belə məhsul yoxdur!")
                    continue

                print(f"Seçildi: {secilen['name']} - {secilen['price']} AZN")

                miqdar = int(input("Miqdar daxil et: "))
                if miqdar <= 0:
                    print("Miqdar 0 və ya mənfi ola bilməz!")
                    continue

                print("B → Səbətə əlavə et")
                print("F → Favoritlərə əlavə et")
                print("X → Ləğv et")
                sec = input("Seçim: ")

                if sec.upper() == "B":
                    history.append(f"Səbətə əlavə olundu: {secilen['name']} x{miqdar}")

                    sebet.append({
                        "ad": secilen["name"],
                        "price": secilen["price"],
                        "qty": miqdar,
                        "total": secilen["price"] * miqdar
                    })
                elif sec.upper() == "F":
                    history.append(f"Favoritlərimə əlavə olundu: {secilen['name']}")
                    favourities.append({
                        "ad": secilen["name"],
                        "price": secilen["price"],
                    })
                elif sec.upper() == "X":
                    print("Ləğv edildi.")
                else:
                    print("Yanlış əməliyyat!")

            if category == "Elektronika":
                items = list_products(DEFAULT_PRODUCTS, "Elektronika")
                
                product_id = int(input("Məhsul ID daxil edin: "))
                
                secilen = None
                for p in items:
                    if p["id"] == product_id:
                        secilen = p
                        break

                if secilen is None:
                    print("Belə məhsul yoxdur!")
                    continue

                print(f"Seçildi: {secilen['name']} - {secilen['price']} AZN")

                miqdar = int(input("Miqdar daxil et: "))
                if miqdar <= 0:
                    print("Miqdar 0 və ya mənfi ola bilməz!")
                    continue

                print("B → Səbətə əlavə et")
                print("F → Favoritlərə əlavə et")
                print("X → Ləğv et")
                sec = input("Seçim: ")

                if sec.upper() == "B":
                    history.append(f"Səbətə əlavə olundu: {secilen['name']} x{miqdar}")
                    sebet.append({
                        "ad": secilen["name"],
                        "price": secilen["price"],
                        "qty": miqdar,
                        "total": secilen["price"] * miqdar
                    })
                    print("Səbətə əlavə edildi!")

                elif sec.upper() == "F":
                    history.append(f"Favoritlərimə əlavə olundu: {secilen['name']}")
                    favourities.append(secilen)
                    print("Favoritlərə əlavə edildi!")

                elif sec.upper() == "X":
                    print("Ləğv edildi.")
                else:
                    print("Yanlış əməliyyat!")

            if category == "Geyimler":
                items = list_products(DEFAULT_PRODUCTS, "Geyimler")
                
                product_id = int(input("Məhsul ID daxil edin: "))
                
                secilen = None
                for p in items:
                    if p["id"] == product_id:
                        secilen = p
                        break

                if secilen is None:
                    print("Belə məhsul yoxdur!")
                    continue

                print(f"Seçildi: {secilen['name']} - {secilen['price']} AZN")

                miqdar = int(input("Miqdar daxil et: "))
                if miqdar <= 0:
                    print("Miqdar 0 və ya mənfi ola bilməz!")
                    continue

                print("B → Səbətə əlavə et")
                print("F → Favoritlərə əlavə et")
                print("X → Ləğv et")
                sec = input("Seçim: ")

                if sec.upper() == "B":
                    history.append(f"Səbətə əlavə olundu: {secilen['name']} x{miqdar}")
                    sebet.append({
                        "ad": secilen["name"],
                        "price": secilen["price"],
                        "qty": miqdar,
                        "total": secilen["price"] * miqdar
                    })
                    print("Səbətə əlavə edildi!")

                elif sec.upper() == "F":
                    history.append(f"Favoritlərimə əlavə olundu: {secilen['name']}")
                    favourities.append(secilen)
                    print("Favoritlərə əlavə edildi!")

                elif sec.upper() == "X":
                    print("Ləğv edildi.")
                else:
                    print("Yanlış əməliyyat!")

        if secim == 2:
            print("\n--- SƏBƏT ---")
            if len(sebet) == 0:
                print("Səbət boşdur!")
            else:
                for item in sebet:
                    print(item)
            umumi = 0
            for item in sebet:
                print(f"{item['ad']} | {item['price']} AZN x {item['qty']}  = {item['total']}")
                umumi += item['total']

            print(f"ÜMUMİ MƏBLƏĞ: {umumi} AZN\n")

            print("1) Checkout")
            print("2) Səbəti təmizlə")
            print("0) Geri")

            alt_secim = int(input("Seçim daxil et: "))

            if alt_secim == 1:
                if umumi <= user_balance:
                    user_balance -= umumi
                    history.append(f"Checkout uğurludur. {umumi} AZN")
                    print("Checkout uğurludur! Balansdan çıxıldı!")
                    print("Yeni balans:", user_balance, "AZN")
                    sebet.clear()
                else:
                    history.append(f"Checkout uğursuzdur. Balans: {umumi} AZN")
                    print("Balans çatmır, emeliyyat ləğv edildi!")

            elif alt_secim == 2:
                sebet.clear()
                print("Sebet temizlendi!")

            elif alt_secim == 0:
                continue
            else:
                print("Yanlış emeliyyat!")

        if secim == 3:
            print("\n--- FAVORİTLƏR ---")

            if len(favourities) == 0:
                print("Favorit yoxdur!")
                continue

            say = 1
            for item in favourities:
                print(f"{say}) {item['name']} - {item['price']} AZN")
                say += 1

            print("\n1) Favoriti sebete elave et.")
            print("2) Favoriti sil.")
            print("0) Geri.")

            sec = int(input("Seçim: "))

            if sec == 1:
                fav_id = int(input("Favorit ID daxil edin: "))

                if fav_id < 1 or fav_id > len(favourities):
                    print("Yanlış ID!")
                    continue

                secilen = favourities[fav_id - 1]

                miq = int(input("Miqdar daxil edin: "))
                if miq <= 0:
                    print("Miqdar düzgün deyil!")
                    continue

                sebet.append({
                    "ad": secilen["name"],
                    "price": secilen["price"],
                    "qty": miq,
                    "total": secilen["price"] * miq
                })

                print("Sebete elave edildi!")

            elif sec == 2:
                fav_id = int(input("Silinecek ID: "))

                if fav_id < 1 or fav_id > len(favourities):
                    print("Yanlış ID!")
                    continue

                silinen = favourities.pop(fav_id - 1)
                print(f"{silinen['name']} silindi.")

            elif sec == 0:
                continue
            else:
                print("Yanlış seçim!")

        if secim == 4:
            print("\n--- TARİXÇƏ ---")
            
            if len(history) == 0:
                print("Tarixçə boşdur!")
            else:
                for procces in history:
                    print(procces)

        if secim==5:
            newpassword = int(input("Yeni sifrenizi daxil edin"))
            trypassword = int(input("Yeni sifrenizi tekrar daxil edin"))
            if newpassword==trypassword:
                password = newpassword
                print("Sifre deyisdirildi...")
                break

        if secim==6:
            print("Balans:", DEFAULT_USERS[0]["balance"])