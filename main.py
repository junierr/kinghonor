import math
import queue
import random
import time
from roles import *

print("红队:")
h1 = SSX()
h2 = CXJ()
h3 = WZJ()
h4 = LP()
h5 = CXK()
time.sleep(0.5)
print("蓝队:")
h6 = CWJ()
h7 = LB()
h8 = HX()
h9 = ZJ()
h10 = CC()
time.sleep(0.5)

red = [h1, h2, h3, h4, h5]
blue = [h6, h7, h8, h9, h10]

r = [h1, h2, h3, h4, h5]
b = [h6, h7, h8, h9, h10]

queue = queue.PriorityQueue()

for h in red:
    queue.put(h)
    h.setTeam("Red")
for h in blue:
    queue.put(h)
    h.setTeam("Blue")


def attack(Hero):
    if Hero.getTeam() == "Red":
        tarTeam = b
        selfTeam = r
    if Hero.getTeam() == "Blue":
        tarTeam = r
        selfTeam = b
    skill = Hero.useSkill()
    for i in range(0, Hero.skills[skill][1]):
        tarHero = random.choice(tarTeam)
        if (Hero.skills[skill][0] < 0):
            tarHero = random.choice(selfTeam)
            num = (random.random() *
                   abs(Hero.skills[skill][0])*Hero.getDamage())
            tarHero.cure(num)
            print("%s 队的 %s 对 %s 使用了 %s 恢复了 %d 的血量" %
                  (Hero.getTeam(), Hero.getName(), tarHero.getName(), skill, num))

        else:
            tarHero = random.choice(tarTeam)
            num = int(random.random()*Hero.skills[skill][0]*Hero.getDamage())
            tarHero.suffer(tarTeam,Hero,num)
            print("%s 队的 %s 对 敌方的 %s 使用了 %s 造成了 %d 的伤害" %
                  (Hero.getTeam(), Hero.getName(), tarHero.getName(), skill, num))
            if (Hero.skills[skill][2]):
                tarHero.run()
                print("敌方的 %s 被减速了" %
                      tarHero.getName())
            
time.sleep(0.1)
print("战斗开始！")
print()

while (True):
    f1 = False
    f2 = False
    for h in red:
        if h.getStatus():
            f1 = True
    for h in blue:
        if h.getStatus():
            f2 = True
    if f1 == False:
        print()
        print("蓝队胜利！")
        break
    if f2 == False:
        print()
        print("红队胜利！")
        break
    now = queue.get()
    now.run()
    attack(now)
    while(not queue.empty()):
        queue.get()
    for h in red:
        if h.getStatus():
            queue.put(h)
    for h in blue:
        if h.getStatus():
            queue.put(h) 
print()
print("红队 击杀&输出:")
time.sleep(0.5)
for h in red:
    print("%3s %d&%d"%(h.getName(),h.getKilled(),h.getOutput()))
print()
print("蓝队 击杀&输出:")
time.sleep(0.5)   
for h in blue:
    print("%3s %d&%d"%(h.getName(),h.getKilled(),h.getOutput()))
