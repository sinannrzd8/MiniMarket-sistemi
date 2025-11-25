import time
import json
import os
import logging

enter_key = False
t=0

logging.basicConfig(level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s", datefmt = "%Y-%d-%m %H:%M:%S",filename = "history.log")

def list_products(products, cathegory):
    items = products[cathegory]["products"]
    print('\n[Məhsul ID]   Ad                       Qiymət (AZN)')
    for p in items:
        print(f"[{p['id']}] {p['name']:<22} {p['price']:.2f}")
    return items

def header(slptm,text):
    print("\t\t\t\t Mini-Market\n\t\t\t  ...........................\n\t\t{}".format(text))
    time.sleep(slptm)

def writer(id,name,password,balance,basket,favs):
    with open("users.json","r",encoding="utf-8") as file:
        user_Db = json.load(file)    
    user_Db[id]["username"] = name
    user_Db[id]["password"] = password
    user_Db[id]["balance"] = balance
    with open("users.json","w",encoding="utf-8") as file:
        user_Db = json.dump(user_Db,file,ensure_ascii = False,indent=4)
    with open("user_baskets.json","r",encoding="utf-8") as file:
        all_baskets = json.load(file)
    all_baskets[id] = basket
    with open("user_baskets.json","w",encoding="utf-8") as file:
        all_baskets = json.dump(all_baskets,file,ensure_ascii = False,indent=4)
    with open("user_favorites.json","r",encoding="utf-8") as file:
        all_favs = json.load(file)
    all_favs[id] = favs
    with open("user_favorites.json","w",encoding="utf-8") as file:
        all_favs = json.dump(all_favs,file,ensure_ascii = False,indent=4)
    logging.info("User_ID ({}) : Successful database saving.".format(id))
    
    
def cooldown_check(slptm,fails):
    logging.info("User_ID (NONE) : Wrong log in informations. Failed log in.")
    if fails != 0 and fails%3==0:
        logging.info("User_ID (NONE) : Cooldown - 10 second")
        while slptm:
            countdown_text = "Çox sayda uğursuz cəhddən sonra hesabınız müvəqqəti bloklanıb. {:02d} saniyə sonra yenidən cəhd edin.".format(slptm)
            if slptm != 1:
                print(countdown_text, end='\r')
            else:
                print(countdown_text)
            time.sleep(1)
            slptm -= 1

while True:
    if t == 0:
        header(0.2,"\t\tXoş Gəlmisiniz!")
    username_list = []
    with open("users.json","r+",encoding="utf-8") as file:
        user_Db = json.load(file)
        for i in range(len(user_Db)):
            username_list.append(user_Db[str(i)]["username"])

    input_username = input("İstifadəçi adını daxil edin : ")

    if input_username in username_list:
        user_id = username_list.index(input_username)
        with open("users.json","r+",encoding="utf-8") as file:
            user_Db = json.load(file)
            correct_password = user_Db[str(user_id)]["password"]
            user_balance = user_Db[str(user_id)]["balance"]
            
        input_password = input("İstifadəçi parolunu daxil edin : ")
        
        if input_password==correct_password:
            print("Giriş Uğurludur...")
            enter_key = True
            logging.info("User_ID ({}) : Successfull log in.".format(user_id))
            with open("user_baskets.json","r+",encoding="utf-8") as file:
                all_baskets = json.load(file)
                user_basket = all_baskets[str(user_id)]
            with open("user_favorites.json","r+",encoding="utf-8") as file:
                all_favs = json.load(file)
                user_favs = all_favs[str(user_id)]        
        else:
            print("İstifadəçi adı və ya şifrə yanlışdır.")
            t += 1
            cooldown_check(10,t)
    
    else:
        input_password = input("İstifadəçi parolunu daxil edin : ")
        print("İstifadəçi adı və ya şifrə yanlışdır.")
        t += 1
        cooldown_check(10,t)

    mainselection = None

    while enter_key:
        while mainselection == None:
            header(1.2,"\t\t Əsas Səhifə")
            print("1) Kateqoriyalar\n2) Səbətim (gözləyənlər)\n3) Favoritlərim\n4) Tarixçə\n5) Parametrlər\n6) Balans\n0) Çıxış")
            writer(str(user_id),input_username,correct_password,user_balance,user_basket,user_favs)
            try:
                mainselection = int(input("Seçim edin:"))
                if mainselection not in range(0,7):
                    print("Yanlış seçim.")
                    mainselection = None
            except ValueError:
                print("Yanlış seçim.")

            if mainselection == 0:
                print("Çüsdüm çıx get😭...")
                enter_key = False
        while mainselection == 1:
            header(1.2,"\t\tKateqoriyalar")
            with open("products.json","r+",encoding="utf-8") as file:
                DEFAULT_PRODUCTS = json.load(file)
            for cath in DEFAULT_PRODUCTS:
                print(cath,")", DEFAULT_PRODUCTS[cath]["name"],sep="")
            print("\n Çıxmaq üçün: X")
            cathegory_id = input("Kateqoriyanı daxil et : ")
            if cathegory_id.upper() == "X":
                mainselection = None
                break
            if cathegory_id not in DEFAULT_PRODUCTS.keys():
                print("Yanlış seçim.")
                break
            items = list_products(DEFAULT_PRODUCTS, cathegory_id)
            try:
                product_id = int(input("Məhsul ID daxil edin: "))
            except:
                print("Yanlış seçim.")
                break
            prod_select = None
            for p in items:
                if p["id"] == product_id:
                    prod_select = p
                    break
            if prod_select is None:
                print("Belə məhsul yoxdur!")
                continue
            print(f"Seçildi: {prod_select['name']} - {prod_select['price']} AZN")
            print("B → Səbətə əlavə et")
            print("F → Favoritlərə əlavə et")
            print("X → Ləğv et")
            operation_select = input("Seçim: ")
            time.sleep(0.5)
            if operation_select.upper() == "B":
                qty = input("Miqdar daxil et: ")
                if qty.isdigit() == False or int(qty) < 1:
                    print("Miqdar mütləq natural ədəd olmalıdır.")
                    continue
                else:
                    qty = int(qty)
                user_basket.append({
                        "name": prod_select["name"],
                        "price": prod_select["price"],
                        "qty": qty,
                        "total": prod_select["price"] * qty
                    })
                print("Səbətə əlavə edildi!")
                logging.info("User_ID ({}) : Product added to basket.".format(user_id))
            elif operation_select.upper() == "F":
                print(prod_select)
                prod_select[0] = len(user_favs)
                user_favs.append(prod_select)
                print("Favoritlərə əlavə edildi!")
                logging.info("User_ID ({}) : Product added to Favourites".format(user_id))
            elif operation_select.upper() == "X":
                print("Ləğv edildi.")
            else:
                print("Yanlış əməliyyat!")
        while mainselection == 2:
            header(1.2,"\t\t---SƏBƏT---")
            if len(user_basket) == 0:
                print("Səbət boşdur!")
            total = 0
            i = 0
            for item in user_basket:
                i += 1
                print(f"{i}){item['name']} | {item['price']} AZN x {item['qty']}  = {item['total']}")
                total += item['total']
            print(f"ÜMUMİ MƏBLƏĞ: {total} AZN\n")
            print("1) Checkout")
            print("2) Səbəti təmizlə")
            print("3) Hər-hansı məhsulu səbətdən çıxart.")
            print("0) Geri")
            basket_select = input("Seçim daxil et: ")
            time.sleep(0.5)
            try:
                basket_select = int(basket_select)
            except:
                print("Yanlış seçim.")
                break
            if basket_select == 1:
                if total <= user_balance:
                    user_balance -= total
                    print("Checkout uğurludur! Balansdan çıxıldı!")
                    print("Yeni balans:", user_balance, "AZN")
                    logging.info("User_ID ({}) : Successful checkout.\nTotal:{}".format(user_id, total))
                    user_basket.clear()
                else:
                    print("Balansınızda kifayət qədər vəsait yoxdur, emeliyyat ləğv edildi!")
                    logging.info("Failed checkout.")
            elif basket_select == 2:
                user_basket.clear()
                print("Səbət təmizləndi!")
                logging.info("Basket cleared.")
            elif basket_select == 3:
                try:
                    basket_del_id = int(input("Silinecek ID: "))
                except:
                    print("Yanlış seçim.")
                    break
                if basket_del_id < 1 or basket_del_id > len(user_basket):                        
                    print("Yanlış ID!")
                    break
                deleted = user_basket.pop(basket_del_id - 1)
                print(f"{deleted['name']} silindi.")
                logging.info("Product deleted from basket.")
            elif basket_select == 0:
                mainselection = None
                break
            else:
                print("Yanlış seçim!")
        while mainselection == 3:
                header(1.2,"\t---Favoritlər")
                if len(user_favs) == 0:
                    print("Favorit yoxdur!")
                i = 1
                for item in user_favs:
                    print(f"{i}) {item['name']} - {item['price']} AZN")
                    i += 1
                print("\n1) Favoriti sebete elave et.")
                print("2) Favoritləri təmizlə.")
                print("3) Məhsulu sil.")
                print("0) Geri.")

                fav_select = input("Seçim: ")
                time.sleep(0.5)
                try:
                    fav_select = int(fav_select)
                except:
                    print("Yanlış seçim.")
                    break
                if fav_select == 1:
                    try:
                        fav_add_id = int(input("Favorit ID daxil edin: "))
                    except:
                        print("Yanlış seçim.")
                        break
                    if fav_add_id < 1 or fav_add_id > len(user_favs):
                        print("Yanlış ID!")
                        break

                    selected_item = user_favs[fav_add_id - 1]

                    qty = int(input("Miqdar daxil edin: "))
                    if qty <= 0:
                        print("Miqdar düzgün deyil!")
                        break

                    user_basket.append({
                        "name": selected_item["name"],
                        "price": selected_item["price"],
                        "qty": qty,
                        "total": selected_item["price"] * qty
                    })
                    print("Sebete elave edildi!")

                elif fav_select == 2:
                    user_favs.clear()
                    print("Favoritlər təmizləndi.")

                elif fav_select == 3:
                    try:
                        fav_del_id = int(input("Silinecek ID: "))
                    except:
                        print("Yanlış seçim.")
                        break
                    if fav_del_id < 1 or fav_del_id > len(user_favs):
                        print("Yanlış ID!")
                        break
                        
                    print(f"{user_favs[fav_del_id - 1]['name']} silindi.")
                    deleted = user_favs.pop(fav_del_id - 1)
                
                elif fav_select == 0:
                    mainselection = None
                    break
                else:
                    print("Yanlış seçim!")
        while mainselection == 4:
            header(2,"\t\tTarixçə")
            with open("history.log","r+",encoding="utf-8") as file:
                print(file.read())
            mainselection = None
        while mainselection == 5:
            header(1.2,"\t\t{}".format(input_username))
            print("Istifadəçi adını dəyişmək üçün: 1\nŞifrəni dəyişmək üçün: 2\nGeri dönmək üçün: 0")
            setting_select = input("Əməliyyatı daxil edin:")
            time.sleep(0.5)
            if setting_select not in ["1","2","0"]:
                print("Yanlış seçim.")
            elif setting_select == "0":
                mainselection = None

            elif setting_select == "1":
                change_key = False
                inputed_password = input("Şifrənizi qeyd edin: ")
                if inputed_password == correct_password:
                    change_key = True
                else:
                    inputed_password = input("Şifrə yanlışdır, yenidən cəhd edin: ")
                    if inputed_password == correct_password:
                        change_key = True
                if change_key == True:
                    new = input("Yeni istifadəçi adını daxil edin: ")
                    input_username = new
                    print("İstifadəçi adı uğurla dəyişdirildi. Yeni istifadəçi adınız: ",input_username)
                else:
                    print("Əməliyyat baş tutmadı.")   
            elif setting_select == "2":
                change_key = False
                inputed_password = input("Şifrənizi qeyd edin: ")
                if inputed_password == correct_password:
                    change_key = True
                else:
                    inputed_password = input("Şifrə yanlışdır, yenidən cəhd edin: ")
                    if inputed_password == correct_password:
                        change_key = True
                    else:
                        print("Əməliyyat ləğv edildi...")
                if change_key == True:
                    new = input("Yeni şifrəni daxil edin: ")
                    if len(new) < 12 or new.isdigit() == True:
                        print("Tətbiqimizin yeni siyasətinə əsasən sadəcə rəqəmlərdən ibarət və ya 12 simvoldan qısa şifrələr keçərsizdir.")
                    else:
                        new2 = input("Yeni şifrəni təkrar daxil edin: ")
                        if new == new2:
                            print("Şifrəniz uğurla dəyişdirildi.")
                            correct_password = new
                            logging.info("User_ID ({}) : Password changed.".format(user_id))
                else:
                    print("Əməliyyat baş tutmadı.")
        while mainselection == 6:
            header(1.2,"\t Sizin balansınız:{} AZN".format(user_balance))
            print("Balansı artırmaq üçün: +\nGeri dönmək üçün:0")
            slct = input("Əməliyyatı daxil edin: ")
            time.sleep(0.5)
            if slct not in ["+","0"]:
                print("Yanlış seçim.")
            if slct == "0":
                mainselection = None
            else:
                try:
                    amount = int(input("Artırılacaq məbləği qeyd edin: "))
                    if amount < 0:
                        print("Yanlış seçim.")
                    else:
                        user_balance += amount
                        print("Əməliyyat uğurla icra edildi. Sizin balansınız: ",user_balance)
                        logging.info("User_ID ({}) : Balance increased.".format(user_id))
                except:
                    print("Yanlış seçim.")