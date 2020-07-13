
#Gerekli kütüphanelerin kurulumu
import pandas as pd
import numpy as np


#Excel dosyasını tanıtıyorum.
df=pd.read_excel('last4.xlsx')

#İndex değerlerini temizliyorum.
df=df.iloc[:,1:]


data=df.copy()


#Fiyat sütunundaki her verinin sonundaki Tl,dolar ve euro simgesini kaldırıyorum.
data['Fiyat']=data['Fiyat'].apply(lambda x: x[:-2])

#'.' karakterini silip integer değere dönüştürüyorum.
data['Fiyat']=data['Fiyat'].apply(lambda x: int(x.replace('.','')))


#Fiyat sütunundaki her verinin sonundaki ' x' karakterini kaldırıyorum ve integer değere dönüştürüyorum.
data['Kilometre']=data['Kilometre'].apply(lambda x: x[:-2])
data['Kilometre']=data['Kilometre'].apply(lambda x: int(x.replace('.','')))

#Marka, model ve motor değerlerindeki gereksiz boşlukları temizliyorum.
data['Marka']=data['Marka'].apply(lambda x: x.strip())
data['Model']=data['Model'].apply(lambda x: x.strip())
data['Motor']=data['Motor'].apply(lambda x: str(x).strip())



motor2=[]
#'Bilmiyorum' değerine np.nan değerini veriyorum.Diğerlerini float veri tipine dönüştürerek kaydediyorum.
for i in data.Motor:
    try:
        i=float(i)
        if i<10:
            motor2.append(i)
        else:motor2.append(np.nan)
    except:
        motor2.append(np.nan)
        
#Motor sütununu motor2 listesi ile güncelliyorum.        
data['Motor']=motor2  



#MOTOR GUCU
#Motor Gücü içerisindeki değerleri integer veri tipine dönüştürüyorum ve motorGucu listesine ekliyorum.
motorGucu=[]
for i in data['Motor Gucu']:
    
    if i=='Bilmiyorum' or i=='-':
        i=np.NaN
        
    elif 'altı' in i:
        i=i[:-11]
        i=round(int(i)-(int(i)/5))
        
    elif 'üzeri' in i:
        i=i[:-11]
        i=round(int(i)+(int(i)/5))
        
    else:
        i=i[:-3]
        x1,x2=i.split('-')
        i=int((int(x1)+int(x2))/2)
        
    motorGucu.append(i)



#MOTOR HACMİ
#Motor Hacmi içerisindeki değerleri integer veri tipine dönüştürüyorum ve motorHacmi listesine ekliyorum.
motorHacmi=[]
for i in data['Motor Hacmi']:
    
    
    if i=='Bilmiyorum' or  i == '-':
        i=np.nan
        
    elif 'altı' in i:
        i=i[:-11]
        i=round(int(i)-(int(i)/5))
        i=i/1000
        
        
    else:
        
        i=i[:-3]
        x3,x4=i.split('-')
        i=int((int(x3)+int(x4))/2)
        i=i/1000
        
        
        
            
        
    motorHacmi.append(i)

#Motor Hacmi ve Motor Gücü sütununu güncelliyorum.    
data['Motor Gucu']=motorGucu
data['Motor Hacmi']=motorHacmi  


motor3=[]

#Motor sütunundaki np.nan değerleri motor hacmindeki değerleri 1000'e bölerek dolduruyorum.
for x,y in zip(data['Motor'],data['Motor Hacmi']):
    
    x=str(x)
    if 'nan' in x:
        motor3.append(y)
    else:motor3.append(x)

#Motor Sütununu güncelliyorum.    
data['Motor']=motor3


       
ilanNo=data['İlan No']
#DataFrame'i düzeltek için ikiye ayırıyorum.
part_2=data.iloc[:,5:17]
part_1=data.iloc[:,:5]


data=pd.concat([ilanNo,part_1],axis=1)
data=pd.concat([data,part_2],axis=1)

#nan değerleri temizliyorum.
data=data.dropna(axis=0,how='any')

#Fiyat üzerinde herhangi bir etki sağlamayacak veri sütunlarını temizliyorum.
data.drop('İlan Tarihi',axis=1,inplace=True)
data.drop('Motor Hacmi',axis=1,inplace=True)
data.drop('Kimden',axis=1,inplace=True)

#Sütun isimlerini düzenliyorum.
data.columns = ['İlan No', 'Fiyat', 'Marka', 'Model', 'Motor', 'Paket', 'xxx',
       'Model Yili', 'Kilometre', 'Yakit Turu', 'Vites Tipi', 'Motor Gucu',
       'Renk', 'Kasa Tipi', 'Durumu']

data.drop('xxx',axis=1,inplace=True)



data['Motor']=data['Motor'].astype(float)

#get_dummies fonksiyonu ile bütün verileri integer'a dönüştürüyorum.
data=pd.get_dummies(data,columns=['Marka', 'Model', 'Motor', 'Paket',
       'Model Yili', 'Yakit Turu', 'Vites Tipi', 'Motor Gucu',
       'Renk', 'Kasa Tipi', 'Durumu'])

#Excel dosyası olarak kaydediyorum.
data.to_excel('output2.xlsx')






