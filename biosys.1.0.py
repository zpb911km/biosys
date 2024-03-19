import matplotlib.pyplot as plt
import numpy as np

n0=eval(input('init_num:'))
k0=eval(input('K:'))
gens0=1
x0=[]
y0=[]
n1=eval(input('init_num:'))
gens1=1
x1=[]
y1=[]
gensr=1
k1=0.05*n0
while True:
    
    while True:
        gensr+=1
        if n0<k0-0.01:
        
            n0=n0*1.1**((k0-n0)/k0)
            x0.append(gens0)
            y0.append(n0)
            if k0-n0<0.01:
                k1=0.01*n0-100
                break
            gens0+=1
            k1=0.01*n0-100
        if n1<k1-0.01 and gens1%3==0:
        
            n1=n1*2.7**((k1-n1)/k1)
            x1.append(gens1)
            y1.append(n1)
            if k1-n1<0.01:
                n0=n0-1*n1
                break
            gens1+=1
            n0=n0-10*n1
        
        if n0>k0+0.01:
        
            n0=n0*0.9**((n0-k0)/k0)
            x0.append(gens0)
            y0.append(n0)
            if n0-k0<0.01:
                k1=0.01*n0-100
                break
            gens0+=1
            k1=0.01*n0-100
        if n1>k1+0.01 and gens1%3==0:
        
            n1=n1*0.9**((n1-k1)/k1)
            x1.append(gens1)
            y1.append(n1)
            if n1-k1<0.01:
                n0=n0-1*n1
                break
            gens1+=1
            n0=n0-10*n1
        else:
            x1.append(gens1)
            y1.append(n1)
            n0-=10*n1
            gens1+=1
        if n0<0 or k0<0 or n1<0 or k1<0:
            exit()
        if gensr>=100:
            npx0=np.array(x0)
            npy0=np.array(y0)
            plt.scatter(x0, y0,c='r',s=1)#生产者
            npx1=np.array(x1)
            npy1=np.array(y1)
            plt.scatter(x1, y1,c='b',s=1)#初级消费者
            #plt.scatter(y0, y1,c='b',s=1)
            plt.show()
            gensr-=100

            
