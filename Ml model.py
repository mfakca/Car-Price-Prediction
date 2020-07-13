#Gerekli kütüphaneleri kuruyorum.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_excel('output2.xlsx',index_col=1)

df=df.iloc[:,1:]
data=df.copy()

#Bağımlı ve bağımsız değişkeni tanımlıyorum.
y=data['Fiyat']
X=data.drop('Fiyat',axis=1)


#Test-train olarak parçalıyorum.
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

#######XGBM#######



from xgboost import XGBRegressor

model=XGBRegressor(colsample_bytree=0.6,learning_rate=0.1,max_depth=4,n_estimators=1500,random_state=42).fit(X_train,y_train)


#CV sonrasında elde edilen optimum değerler.
#{'colsample_bytree': 0.6, 'learning_rate': 0.1, 'max_depth': 4, 'n_estimators': 1000}


#Optimum değerleri bulmak için Cross Validation işlemi uyguluyorum.
'''
from sklearn.model_selection import GridSearchCV

params={'colsample_bytree': [0.4,0.5,0.6,0.9,1],
'n_estimators':[100,200,500,1000],
'max_depth':[2,3,4,5,6],
'learning_rate':[0.1,0.01,0.5]
}

xgb_grid=GridSearchCV(model,params,n_jobs=-1,verbose=2).fit(X_train,y_train)
print(xgb_grid.best_params_)

'''



#######catboost#######
'''
from catboost import CatBoostRegressor

from sklearn.model_selection import GridSearchCV


catb=CatBoostRegressor()
catb_grid={'iterations':[200,500,1000,2000],
           'learning_rate':[0.01,0.03,0.05,0.1],
           'depth':[3,4,5,6,7,8]}







grid=GridSearchCV(estimator=catb,param_grid=catb_grid,n_jobs=-1,cv=2)
grid.fit(X_train,y_train)


print(grif.best_params_)

'''

#######GBM#######


from sklearn.ensemble import GradientBoostingRegressor
model= GradientBoostingRegressor(learning_rate=0.1,max_depth=3,n_estimators=1500,subsample=0.5,random_state=42).fit(X_train,y_train)

#CV sonrasında elde edilen optimum değerler.
#{'learning_rate': 0.1, 'max_depth': 3, 'n_estimators': 1500, 'subsample': 0.5}

'''
from sklearn.model_selection import GridSearchCV
gbm_params={'learning_rate':[0.001,0.01,0.1,0.2,0.3],
           'max_depth':[3,5,8,10,15,20,50,100],
           'n_estimators':[100,200,500,1000,1500,2000],
           'subsample':[0.5,0.75,1]}
gbm_cv_model=GridSearchCV(model,gbm_params,cv=10,n_jobs=-1).fit(X_train,y_train)

print(gbm_cv_model.best_params_)
'''

#y_pred değeri oluşturuyorum.
y_pred=model.predict(X_test)



from sklearn.metrics import mean_squared_error

#Ortalama hata karesini hesaplıyorum.
print(np.sqrt(mean_squared_error(y_test,y_pred)))

#r2 skorunu hesaplıyorum.
from sklearn.metrics import r2_score
print(r2_score(y_test, y_pred)) 

#Genel yapıyı görmek için 20 değerden oluşan bir tablo çizdiriyorum.
plt.plot(y_pred[57:77])
plt.plot(y_test[57:77],'red')
plt.xlabel('Birim etiketleri')
plt.ylabel('Fiyatlar')
plt.show()



