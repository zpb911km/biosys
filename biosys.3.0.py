from threading import Thread as th
import matplotlib.pyplot as plt
import random as rand
from time import time
from tqdm import trange, tqdm
from numpy import sqrt
from os import system
#plt.figure(figsize=(8, 8), dpi=80)
#plt.scatter(1, 1, c='black', s=0)
#plt.scatter(150, 150, c='black', s=0)
#fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
#ax.set(aspect='equal', xbound=(0, 150), ybound=(0, 150))
# ax.set_axis_off()

x = 100
y = 100# 大小设定
E0 = 200
#个体格式[x_position,y_position,level(-1: death),energy]

producer = []
for x0 in trange(0, x):
    for y0 in range(0, y):
        producer.insert(len(producer), [3*x0+25, 3*y0+25, 0, E0])

# 生产者(均匀)分布

consumer = []
for a in trange(9):
    consumer.insert(len(consumer), [rand.randint(
        0, 3*x)+25, rand.randint(0, 3*y)+25, 1, 50])


# 初级消费者

gen = 1#代

try:
    while True:# 生命周期
        fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
        ax.set(aspect='equal', xbound=(0, 3*x+50), ybound=(0, 3*y+50))
        ax.set_axis_off()
        if gen % 10 == 1:
            Es = 10
        elif gen % 10 == 4:
            Es = 20
        for pro in producer:
            if pro[2] == 0:
                if pro[3] >= 0:
                    pro[3] += Es  # 生产者捕获太阳能
                else:
                    pro[2] = -1
        for con in consumer:
            if con[2] == 1:
                for pro in producer:
                    if ((con[0]-pro[0])**2+(con[1]-pro[1])**2) <= 5**2:  # 捕食者捕食半径
                        con[3] += 0.05*pro[3]  # 一次吃一“口”能量
                        pro[3] -= 0.2*pro[3]  # 能量传递效率0.2
                if con[3] >= 300: # 消费者分裂
                    con[3] = 50
                    consumer.insert(len(consumer), [con[0]+rand.randint(
                        0, 8)-4, con[1]+rand.randint(0, 8)-4, 1, 50])  
                for conneighbor in consumer:
                    if conneighbor[2] == 1:
                        r = (con[0]-conneighbor[0])**2+(con[1]-conneighbor[1])**2
                        if r <= 9**2:  # 消费者密集半径
                            con[3] -= 0.1*(81-r)
                con[0] += rand.randint(0, 2)-1
                con[1] += rand.randint(0, 2)-1  # 消费者随机移动
                if con[3] <= 5:  # die
                    con[3] = 0
                    con[2] = -1
                con[3] -= 10  # 消费者固定消耗
        ax.clear()
        for a in tqdm(producer):
            if a[3] > 5:
                ax.scatter(a[0], a[1], c='green', s=a[3])
            else:
                producer.remove(a)
        for a in consumer:
            if a[2] == 1 and a[0] >= 25 and a[0] <= 3*x+22 and a[1] >= 25 and a[1] <= 3*y+22 and a[3]>0:
                ax.scatter(a[0], a[1], c='red', s=a[3], alpha=0.5)
            else:
                consumer.remove(a)
        #plt.show()


        if gen != 1:
            task.join()
        def innerfuc():
            plt.savefig(r'E:\myfiles\python\biosys\img\pic_%d.jpg' % gen)
            #  ffmpeg -r <帧数> -f image2 -i image_%d.png -pix_fmt yuv420p <输出文件（带后缀）>
        if len(consumer) <= 2:
            break
        task = th(target=innerfuc)
        task.start()
        #print(len(consumer))
        #plt.savefig(r'E:\myfiles\python\biosys\img\pic_%d.png' % gen)
        gen += 1
        plt.close()
except KeyboardInterrupt:
    system('ffmpeg -r 24 -f image2 -i E:\\myfiles\\python\\biosys\\img\\pic_%d.jpg -pix_fmt yuv420p E:\\myfiles\\python\\biosys\\img\\out0.mp4')