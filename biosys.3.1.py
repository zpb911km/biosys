import matplotlib.pyplot as plt
import random as rand
from numpy import sqrt
from tqdm import trange

x = 50
y = 50  # 大小设定

# 个体格式[x_position,y_position,level(-1: death),energy]

producer = []
for x0 in trange(0, x):
    for y0 in range(0, y):
        producer.insert(len(producer), [3*x0+25, 3*y0+25, 0, 100])

# 生产者均匀分布

consumer = []
for a in range(3):
    consumer.insert(len(consumer), [rand.randint(
        0, 3*x)+25, rand.randint(0, 3*y)+25, 1, 50])


# 初级消费者
genl = []
pronl = []
proel = []
connl = []
conel = []
gen = 1  # 代
while True:
    s=eval(input('(15,25):'))
    try:
        while True:  # 生命周期
            u=s+rand.randint(-15,15)
            pron = 0
            proe = 0
            conn = 0
            cone = 0
            for pro in producer:
                if pro[2] == 0:
                    if pro[3] >= 0:
                        pro[3] += (u+rand.randint(-5,5))  # 生产者捕获太阳能
                    else:
                        pro[2] = -1
            for con in consumer:
                if con[2] == 1 and con[3] > 5:
                    for pro in producer:
                        if ((con[0]-pro[0])**2+(con[1]-pro[1])**2) <= 5**2:  # 捕食者捕食半径
                            con[3] += 0.02*pro[3]  # 一次吃一“口”能量
                            pro[3] -= 0.1*pro[3]  # 能量传递效率0.2
                    if con[3] >= 300 and ((con[0]-pro[0])**2+(con[1]-pro[1])**2) <= (con[3]*0.01)**2:  # 消费者分裂
                        con[3] = 50
                        consumer.insert(len(consumer), [con[0]+rand.randint(
                            0, 8)-4, con[1]+rand.randint(0, 8)-4, 1, 50])
                    for conneighbor in consumer:
                        if conneighbor[2] == 1:
                            r = (con[0]-conneighbor[0])**2 + \
                                (con[1]-conneighbor[1])**2
                            if r <= 5**2:  # 消费者密集半径
                                con[3] -= 2-sqrt(r)
                    con[0] += rand.randint(0, 2)-1
                    con[1] += rand.randint(0, 2)-1  # 消费者随机移动
                    con[3] -= s  # 消费者固定消耗
                else:
                    con[3] = 0
                    con[2] = -1

            for pro in producer:
                if pro[2] == 0:
                    pron += 1
                    if pro[3] > 0:
                        proe += pro[3]
            for con in consumer:
                if con[2] == 1:
                    conn += 1
                    if con[3] > 5:
                        cone += con[3]

            print(gen, pron, proe, conn, cone, proe/(pron+0.001), cone/(conn+0.001),u)
            genl.append(gen)
            pronl.append(pron)
            proel.append(proe)
            connl.append(conn)
            conel.append(cone)

            # if gen % 1000 == 0:

            gen += 1
            if conn == 0:
                raise ValueError("死光光")
    except ValueError as result:
        print(result)
        plt.scatter(genl, pronl, color='#196F0F', s=2)
        plt.show()
        plt.scatter(genl, proel, color='#26E10F', s=2)
        plt.show()
        plt.scatter(genl, conel, color='#E1240B', s=2)
        plt.show()
        plt.scatter(genl, connl, color='#73190D', s=2)
        plt.show()
        try:
            for a in producer:
                if a[2] == 0 and a[0] >= 25 and a[0] <= 3*x+22 and a[1] >= 25 and a[1] <= 3*y+22 and a[3] > 0:
                    plt.scatter(a[0], a[1], c='green', s=a[3])
            for a in consumer:
                if a[2] == 1 and a[0] >= 25 and a[0] <= 3*x+22 and a[1] >= 25 and a[1] <= 3*y+22 and a[3] > 0:
                    plt.scatter(a[0], a[1], c='red', s=a[3], alpha=0.5)
            plt.show()
            break
        except:
            plt.show()
            break
    except KeyboardInterrupt:
        plt.scatter(genl, pronl, color='#196F0F', s=2)
        plt.show()
        plt.scatter(genl, proel, color='#26E10F', s=2)
        plt.show()
        plt.scatter(genl, conel, color='#E1240B', s=2)
        plt.show()
        plt.scatter(genl, connl, color='#73190D', s=2)
        plt.show()
        try:
            for a in producer:
                if a[2] == 0 and a[0] >= 25 and a[0] <= 3*x+22 and a[1] >= 25 and a[1] <= 3*y+22 and a[3] > 0:
                    plt.scatter(a[0], a[1], c='green', s=a[3])
            for a in consumer:
                if a[2] == 1 and a[0] >= 25 and a[0] <= 3*x+22 and a[1] >= 25 and a[1] <= 3*y+22 and a[3] > 0:
                    plt.scatter(a[0], a[1], c='red', s=a[3], alpha=0.5)
            plt.show()
        except:
            plt.show()
    except Exception as result:
        print("未知错误 %s" % result)
        break
