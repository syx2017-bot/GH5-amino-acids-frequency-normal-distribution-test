import numpy as np
from scipy import stats
from scipy.stats import mannwhitneyu
from pandas.core.frame import DataFrame
data1=np.genfromtxt("data1.csv",delimiter=',')
data2=np.genfromtxt("=data2.csv",delimiter=',')
da1=[]
da2=[]
listr=["Ala","Cys","Asp","Glu","Phe","Gly","His","Ile","Lys","Leu","Met","Asn","Pro","Gln","Arg","Ser","Thr","Val","Trp","Tyr"]
listf=[]
listu=[]
listp=[]
for i in range(0,20):
    da1=data1[:,i]
    da2=data2[:,i]
    u,p=mannwhitneyu(da1,da2)
    listu.append(u)
    listp.append(p)
    if p>=0.05:
        listf.append("no significant difference")
    else:
        listf.append("significant difference")
dic={"residue ":listr,
    "U.value":listu,
     "P.value":listp,
      "significant difference result":listf}
output=DataFrame(dic)
print(output)
