#Gerekli Kütüphaneleri import ediyoruz.

import requests
from bs4 import BeautifulSoup
import pandas as pd



all_value=[]
#Gerekli listeleri tanıtıyoruz.
paket,model,motor,marka2,fiyat,ilanNo,ilanTarihi,modelYili,km,yakitTuru,vitesTipi,motorHacmi,motorGucu,renk,kasaTipi,kimden,durumu=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

#Marka listesini tanıtıyoruz
marka=['Acura', 'Alfa Romeo', 'Audi', 'BMW', 'Cadillac', 'Chery', 'Chevrolet', 'Chrysler', 'Citroen', 'DS Automobiles', 'Dacia', 'Daewoo', 'Daihatsu', 'Diger', 'Dodge', 'Fiat', 'Ford', 'Gaz', 'Geely', 'Honda', 'Hyundai', 'Ikco', 'Isuzu', 'Jaguar', 'Jeep', 'Kia', 'Lada', 'Lancia', 'Land Rover', 'Lexus', 'Mahindra', 'Maserati', 'Mazda', 'Mercedes', 'Mini', 'Mitsubishi', 'Nissan', 'Opel', 'Peugeot', 'Porsche', 'Proton', 'Renault', 'Rover', 'Saab', 'Seat', 'Skoda', 'Smart', 'Ssangyong', 'Subaru', 'Suzuki', 'Tata', 'Tofas', 'Toyota', 'Volkswagen', 'Volvo']
deneme=[]
x=''


#Sitenin sayfaları arasında ilerleyebilmek için for döngüsü kuruyoruz.

#SAYFA
for f in range(2,81):
    
    #Veriyi çekeceğimiz linki xxx/sayfa='f' olarak ayarlıyoruz. Bu sayede bütün sayfalar içerisine erişebiliyoruz. 
    link1='xxx'+str(f)

    
    #Requests kütüphanesi ile sayfanın kaynağını çekiyoruz.
    r = requests.get(link1)

    #BeatifulSoup kütüphanesi ile çektiğimiz kaynak dosyasını düzenliyoruz. Ben 'lxml' olarak çektim (Diğerlerinden çok daha hızlı).
    source = BeautifulSoup(r.content,"lxml")

    #Site içerisinde karmaşık bir yapı olduğu için sayaçla kontrol etmek zorunda kaldım.
    sayacx=1


    #Bütün a etiketli offer-link classlarını çekiyoruz.
    #Sayfa içerisindeki her bir başlık içerisinde dönüyor.
    for i in source.find_all('a',attrs={'class':'offer-link'}):
        
        if sayacx%3==0:

            #Çektiğimiz classların 'href' karşılığını alıp yeni link olarak atıyoruz. 
            link=str('xxx'+i.get('href'))


            #Yeni linklerin kaynağını çekiyoruz.
            r2=requests.get(link)

            #BeatifulSoup kütüphanesi ile çektiğimiz kaynak dosyasını düzenliyoruz. 
            source2=BeautifulSoup(r2.content,'lxml')

            #Her bir ürün içerisinde istediğimiz verilerin bulunduğu 'table' etiketli car-details classını çekiyoruz.
            for y in source2.find_all('table',attrs={'class':'car-details'}):

                #Tablo içerisindeki satırlara ulaşıyoruz.
                for x in y.find_all('tr'):
                    
                    var=0
                    var2=0
                    #Satırlar arasındaki hücrelere ulaşıyoruz.
                    for c in x.find_all('td'):
                        
                        #Çok fazla boşluk vardı.Bir nevi strip işlemi uygulayarak onlardan kurtuldum.
                        c=(c.text.split())
                        c=' '.join(c)
                        
                        #c değişkenin son karakteri ₺,$ veya € ile bitiyorsa if bloğuna girer ve c değişkenini fiyat listesine ekler.
                        #FİYAT
                        if c.endswith('₺')==True or c.endswith('$')==True or c.endswith('€')==True:

                            
                            fiyat.append(c)
                            
                            continue
                        #c değişkeni içerisinde '»' varsa eğer if bloğuna girer ve marka, model, paket olarak ayırır, listelere ekler.
                        #MARKA,MODEL,MOTOR,PAKET
                        if '»' in c:
                            #Tablo içerisinde birden fazla marka verisi bulunduğu ve hepsinin alınıp sorun oluşturmaması için birini lsitelere ekliyorum.
                            var2+=1
                            if var2==2:
                            
                                splitted_marka2=c.split('»')
                                
                                marka2.append(splitted_marka2[1])
                                
                                del splitted_marka2[0]
                                del splitted_marka2[0]                                
                                                                      
                                                                    
                                model.append(splitted_marka2[0])
                                del splitted_marka2[0]
                                motor.append(splitted_marka2[0][:4])
                                paket.append(splitted_marka2[0][5:])
                                


                            
                            continue

                        #İlk önce açıklamayı daha sonra veriyi verdiği için değişken atayarak bu sorunu çözmeye çalıştım. elif bloğuna giriyor , var değeri tanıtılıyor.
                        #Bir sonraki iterasyonda istediğimiz veriyi alıyor ve var değeri sayesinde doğru listeye ekleniyor.
                        #İLAN NO:
                        elif c=='İlan No:':
                            var=1
                            continue
                        
                        #İLAN TARİHİ:
                        elif c=='İlan Tarihi:':
                            var=2
                            continue
                        
                        #MODEL YILI:
                        elif c=='Model Yılı:':
                            var=3
                            continue
                        
                        #KM:
                        elif c=='Kilometre:':
                            var=4
                            continue
                        
                        #YAKIT TÜRÜ:
                        elif c=='Yakıt Türü:':
                            var=5
                            continue
                        
                        #VİTES TİPİ:
                        elif c=='Vites Tipi:':
                            var=6
                            continue
                        
                        #MOTOR HACMİ:
                        elif c=='Motor Hacmi:':
                            var=7
                            continue
                        
                        #MOTOR GÜCÜ:
                        elif c=='Motor Gücü:':
                            var=8
                            continue
                        
                        #RENK:
                        elif c=='Renk:':
                            var=9
                            continue
                        
                        #KASA TİPİ:
                        elif c=='Kasa Tipi:':
                            var=10
                            continue
                        
                        #KİMDEN:
                        elif c=='Kimden:':
                            var=11
                            continue
                        
                        #DURUMU:
                        elif c=='Durumu:':
                            var=12
                            continue
                        
                        
                        
                        
                        
                        if var==1:ilanNo.append(c)
                        
                        
                        elif var==2:ilanTarihi.append(c)
                        
                        
                        elif var==3:modelYili.append(c)
                        

                        #Excelden verileri çekerken km verisini float olarak algılıyor ve 28.000 değeri 28'e dönüşüyor.Bu sorunu önelemek için c'nin sonuna ' x' ekleyerek string olarak kaydettim.
                        elif var==4:
                            c=c+' x'
                            km.append(c)
                        
                        
                        elif var==5:yakitTuru.append(c)
                        
                        
                        elif var==6:vitesTipi.append(c)
                        
                        
                        elif var==7:motorHacmi.append(c)
                        
                        
                        elif var==8:motorGucu.append(c)
                        
                        
                        elif var==9:renk.append(c)
                        
                        
                        elif var==10:kasaTipi.append(c)
                        
                        
                        elif var==11:kimden.append(c)
    
    
                        elif var==12:durumu.append(c)                    
                        
        sayacx+=1
fiyat2=[]
deger=0
x1=''

#İkişer defa kaydedilen fiyat listesini temziliyor.    
for fiyat_del in fiyat:
    try:
        fiyat2.append(fiyat[deger])
        deger+=2
    except:break
for fiyat_deneme in fiyat:
    if fiyat_deneme==x1:fiyat.remove(fiyat_deneme)
    x1=fiyat_deneme
    
#Bütün listelerden DataFrame oluşturuyorum. 
df=pd.DataFrame(fiyat2,columns=['Fiyat'])
df['Marka']=marka2
df['Model']=model
df['Motor']=motor
df['Paket']=paket
df['İlan No']=ilanNo
df['İlan Tarihi']=ilanTarihi
df['Model Yili']=modelYili
df['Kilometre']=km
df['Yakit Turu']=yakitTuru
df['Vites Tipi']=vitesTipi
df['Motor Hacmi']=motorHacmi
df['Motor Gucu']=motorGucu
df['Renk']=renk
df['Kasa Tipi']=kasaTipi
df['Kimden']=kimden
df['Durumu']=durumu

#DataFrame'i Excel dosyası olarak kaydediyorum.
df.to_excel('last4.xlsx')
