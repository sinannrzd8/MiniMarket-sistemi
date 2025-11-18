import time
import json
import os
from pathlib import Path

t=0

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


print("==========Xoş Gəlmisiniz==========")

while t==0:
    user_name='Sinan və Nicat'
    user_password=1234
    for i in range(3):
        username = input('Istifadəçi adını daxil edin : ')
        password = int(input("İstifadəçi parolunu daxil edin : "))
        if user_name==username and user_password==password:
            print("Giriş Uğurludur....")
            break
        else:
            print("İstifadəçi Tapılmadı!!!\n")
    else:
        print("Sən getdin bloka😏 (10 saniyəlik)")

        time.sleep(10)


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
            category = input("Kateqoriyanı daxil et.")

