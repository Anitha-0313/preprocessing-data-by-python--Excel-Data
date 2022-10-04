import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
d=pd.read_excel("data.xlsx")
df=pd.DataFrame(d)
X=d[['input1','input2']]
Y=d['output'].values
print('-'*80)
print('shape of X is',X.shape)
print('shape of Y is',Y.shape)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
print('-'*80)
print('length of X_test',len(X_test))
print('length of X_train',len(X_train))
print('length of Y_test',len(Y_test))
print('length of Y_train',len(Y_train))
print('-'*80)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)
for i in range (10):
  print(X_train[i])
print('-'*80)
for i in range(3):
 print(X_test[i])