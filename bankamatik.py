
isim=input("Lütfen İsminizi Giriniz: ")
hesapNo=input("Lütfen Hesap Numaranızı Giriniz: ")
kisiselHesap = {
    'ad':isim,
    'hesapNo':hesapNo,
    'bakiye':3000,
    'ekHesap':2000
}


def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print('paranızı alabilirsiniz.')
    else:
        toplam=hesap['bakiye']+hesap['ekHesap']   

        if (toplam>=miktar):
            ekHesapkullanimi=input('Ek hesap kullanılsın mı (e/h)?')
            hesap['ekHesap']=hesap['ekHesap']-(miktar-hesap['bakiye'])
            hesap['bakiye']=0

            if ekHesapkullanimi=='e':
                print('Paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızında {hesap['bakiye']} bulunmaktadır.")    
        else:
            print('Üzgünüz Bakiyeniz Yetersiz')     
            
    print(f"{hesap['bakiye']} kadar hesapta paranız ve {hesap['ekHesap']} kadar ek hesapta paranız bulunmaktadır")


cekilecekMiktar=int(input("Hesaptan Çekilecek Miktar: "))

paraCek(kisiselHesap,cekilecekMiktar)

