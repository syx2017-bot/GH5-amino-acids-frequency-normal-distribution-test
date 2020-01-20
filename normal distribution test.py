import numpy as np
from scipy import stats
from scipy.stats import shapiro
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

data=np.genfromtxt("data.csv",delimiter=",")
listp=[]
listw=[]
listf=[]
listr=["Ala","Cys","Asp","Glu","Phe","Gly","His","Ile","Lys","Leu","Met","Asn","Pro","Gln","Arg","Ser","Thr","Val","Trp","Tyr"]
for i in range(0,20):
    aa=data[1:,i]
    fig=plt.figure
    res=stats.probplot(aa,plot=plt)
    plt.show()
    w,p = shapiro(aa)
    listw.append(w)
    listp.append(p)
    if p>=0.05:
        print("normal distribution")
        listf.append("normal distribution")
    else:
        print("abnormal distribution")
        listf.append("abnormal distribution")
    print("w：%f" %w,"p.value：%f" %p)
dic={"residue index":listr,
      "W":listw,
      "P.value":listp,
      "F":listf}
output=DataFrame(dic)
print(output)
