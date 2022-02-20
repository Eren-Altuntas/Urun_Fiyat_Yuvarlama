import time

print("""

HOŞGELDİNİZ

*********************
Ürün Fiyat Yuvarlama
*********************

Created by Eren Altuntaş

""")


kg1 = float(input("1. ürün kg :  "))
kg2 = float(input("2. ürün kg :  "))
price1 = float(input("1. ürün fiyat: "))
price2 = float(input("2. ürün fiyat: "))
totalkg = (kg1 + kg2)
amb1 = (kg1 * price1)
amb2 = (kg2 * price2)
amb3 = (amb1 + amb2)
averageprice = (amb3 / totalkg)
averagepricestr = str(averageprice).split(".")[1]


'''price1strdotdigit = str(price1).split(".")[1] # Virgülden sonraki dijit
price1strdigit = int(price1strdotdigit[0]) # Virgülden sonraki ilk dijit
price1strnumber = int(str(price1).split(".")[0]) # Virgülden önceki sayı
price1strdigit = (price1strdigit * 1/10)
newprice = price1strnumber + price1strdigit

price2strdotdigit = str(price2).split(".")[1] # Virgülden sonraki dijit
price2strdigit = int(price2strdotdigit[0]) # Virgülden sonraki ilk dijit
price2strnumber = int(str(price2).split(".")[0]) # Virgülden önceki sayı
price2strdigit = (price2strdigit * 1/10)
newprice2 = price2strnumber + price2strdigit'''

liste = []
sayac = 0
a = 0.001

for i in range(999):
    newa = str(a).split(".")[0] + "." + str(a).split(".")[1][0]+ str(a).split(".")[1][1]+ str(a).split(".")[1][2] # Değer üretme
    liste.append(newa)
    a += 0.001

for i in range(999):
    newa = float(liste[i])
    ambcontrol = str(((price1 + newa) * kg1)).split(".")[1] # Birinci Kontrol Kodu
    if len(ambcontrol) == 3 or len(ambcontrol) == 2 or len(ambcontrol) == 1:# Ambalaj Virgülden sonraki hane sayısı kontro
        tryint = (((price1 + newa) * kg1) + (price2 * kg2)) / totalkg
        #print(tryint)
        #print(newprice + newa)
        tryintstr = str(tryint).split(".")[1]
        if (len(tryintstr) == 3 or len(tryintstr) == 2 or len(tryintstr) == 1) and (len(str((price1 + newa)).split(".")[1]) <= 3):# Ortalama Fiyat Virgülden sonraki hane sayısı kontrolü
            print("Yeni Fiyat => {}".format((price1 + newa)))

            print("""

            Fiyat Tablosu
            - - - - - - - - - - - - - - - - - - - - - - - - -
            |  1. Fiyat => {}                                |
            |                                                |
            |  2. Fiyat => {}                                |
            |                                                |
            |  Toplam kg => {}                               |
            |                                                |
            |  Ortalama Fiyat => {}                          |
            - - - - - - - - - - - - - - - - - - - - - - - - -

            İyi Günler ...

            ****Not: Eğer Yeni Fiyat adında bir değişken yoksa tablodaki verileri görmezden geliniz****

            """.format((price1 + newa),price2,totalkg,tryint))
            time.sleep(20)
            exit()
        else:
            pass
    else:
        pass

secim = input("2.yi denemek ister misiniz:(y/n) ")

if secim == "y":
    for i in range(999):
        newa = float(liste[i])
        ambcontrol = str(((price2 + newa) * kg2)).split(".")[1] # İkinci Kontrol Kodu
        if len(ambcontrol) == 3 or len(ambcontrol) == 2 or len(ambcontrol) == 1: # Ambalaj Virgülden sonraki hane sayısı kontrolü
            tryint = ((price1 * kg1) + ((price2 + newa) * kg2)) / totalkg
            #print(tryint)
            #print(newprice2 + newa)
            tryintstr = str(tryint).split(".")[1]
            if (len(tryintstr) == 3 or len(tryintstr) == 2 or len(tryintstr) == 1) and (len(str((price2 + newa)).split(".")[1]) <= 3): # Ortalama Fiyat Virgülden sonraki hane sayısı kontrolü
                print("Yeni Fiyat => {}".format((price2 + newa)))

                print("""

                Fiyat Tablosu
                - - - - - - - - - - - - - - - - - - - - - - - - -
                |  1. Fiyat => {}                                |
                |                                                |
                |  2. Fiyat => {}                                |
                |                                                |
                |  Toplam kg => {}                               |
                |                                                |
                |  Ortalama Fiyat => {}                          |
                - - - - - - - - - - - - - - - - - - - - - - - - -

                İyi Günler ...

                ****Not: Eğer Yeni Fiyat adında bir değişken yoksa tablodaki verileri görmezden geliniz****

                """.format(price1,(price2 + newa),totalkg,tryint))
                time.sleep(20)
                exit()
            else:
                pass

elif secim == "n":
    exit()
