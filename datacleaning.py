import pandas as pd
import numpy as np
data=pd.read_csv("betikadata.csv")
data[["HT","AT"]]=data.team.str.split("vs.",expand=True)
data[["FG","HtT","FT"]]=data.Cols.str.split("|",expand=True)
data[["HTFG","ATFG"]]=data.FG.str.split(":",expand=True)
newdata=data.drop(["team","Cols","FG","FT","HtT","ATFG"],axis=1)
newdata.to_csv("mydata.csv")
