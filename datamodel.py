import pandas as pd
import numpy as np
import xgboost as xg
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import svm
data=pd.read_csv("mydata.csv")
newdata=data.apply(LabelEncoder().fit_transform)
x=newdata.drop(["Unnamed: 0","HTFG"],axis=1)
y=newdata.iloc[:,3:4]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=20
)
model=xg.XGBClassifier(params={'max_depth': 10})

model.fit(x_train,y_train)
score=model.score(x_test,y_test)
print("THE MODEL SCORE IS:\params=n", score)

li=[]
for i in range(0,2):
    ele=int(input("INPUT THE VALUE OF HOMETEAM, AWAYTEAM IDs:"))
    li.append(ele)
arr = np.array([li])
pred=model.predict(arr)
print("the prediction is :\n",pred) 




