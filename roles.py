import random


class Hero:
    def __init__(self, Name, health, damage, defeat, speed):
        self.__Name = Name
        self.__health = health
        self.__damage = damage
        self.__defeat = defeat
        self.__speed = speed
        self.__status = True
        self.__output = 0
        self.__killed = 0
        self.place = self.__speed

    def __lt__(self, other):
        return self.place < other.place

    def setTeam(self, team):
        self.__Team = team

    def getName(self):
        return self.__Name

    def getTeam(self):
        return self.__Team

    def getDamage(self):
        return self.__damage

    def getHealth(self):
        return self.__health

    def getSpeed(self):
        return self.__speed

    def getStatus(self):
        return self.__status

    def getOutput(self):
        return self.__output

    def getKilled(self):
        return self.__killed

    def run(self):
        self.place += self.__speed

    def suffer(self, t, Hero, damage):
        num = max(0, damage - self.__defeat)
        Hero.outputAdd(min(num, self.__health))
        self.__health -= num
        self.__health = max(0, self.__health)
        if self.__health == 0:
            self.__status = False
            t.remove(self)
            Hero.killedAdd(1)

    def cure(self, Hcure):
        self.__health += Hcure

    def outputAdd(self, trueDamage):
        self.__output += trueDamage

    def killedAdd(self, truekilled):
        self.__killed += truekilled

    def useSkill(self):
        pass


class SSX(Hero):
    skills = {
        "普通攻击": [1, 1, False],
        "加强攻击": [2, 1, False],  # 单体伤害
        "停下！": [1, 1, True]  # 晕人
    }

    def __init__(self):
        Hero.__init__(self, "孙尚香", 5000, 2000, 500, 15)
        print("大小姐驾到！")

    def useSkill(self):
        skill = random.choice(tuple(self.skills.keys()))
        return skill


class CXJ(Hero):
    skills = {
        "普通攻击": [1, 1, False],
        "吃大斧子": [0.8, 3, False],  # AOE
        "回血！": [-1, 1, False]  # 回血
    }

    def __init__(self):
        Hero.__init__(self, "程咬金", 10000, 1000, 1000, 30)
        print("爱与正义！")

    def useSkill(self):
        skill = random.choice(tuple(self.skills.keys()))
        return skill


class WZJ(Hero):
    skills = {
        "普通攻击": [1, 1, False],
        "冰雹呼脸": [0.7, 5, False],  # AOE
        "休息一下吧": [1.5, 1, False]  # 单体伤害
    }

    def __init__(self):
        Hero.__init__(self, "王昭君", 6000, 1500, 500, 20)
        print("六月飞霜！")

    def useSkill(self):
        skill = random.choice(tuple(self.skills.keys()))

        return skill


class LP(Hero):
    skills = {
        "普通攻击": [1, 1, False],
        "升龙击": [1, 1, True],  # 晕人
        "痛击": [1.5, 1, False]  # 单体伤害
    }

    def __init__(self):
        Hero.__init__(self, "廉颇", 9000, 1000, 750, 10)
        print("肉的一批，伤害没有！")

    def useSkill(self):
        skill = random.choice(tuple(self.skills.keys()))
        return skill


class CXK(Hero):
    skills = {
        "唱": [1, 1, False],  # 普攻
        "跳": [-1, 5, False],  # 回血
        "Rap": [1, 1, True],  # 晕人
        "篮球": [1, 1, True]  # 晕人，为了写完，和rap一样的
    }

    def __init__(self):
        Hero.__init__(self, "蔡徐坤", 8000, 1000, 750, 25)
        print("我是练习时长两年半的练习生！")

    def useSkill(self):
        skill = random.choice(tuple(self.skills.keys()))
        return skill


class CWJ(Hero):
    print("我是蔡文姬，我是最厉害的辅助！")
    skills = {
        "控制术": [0, 1, True],  # 硬控
        "治疗术": [-1, 3, False]  # 三人回血
    }

    def __init__(self):
        Hero.__init__(self, "蔡文姬", 10000, 1000, 1000, 15)

    def useSkill(self):
        skill = random.choice(tuple(self.skills.keys()))
        return skill


class LB(Hero):
    print("我是鲁班七号，看我的大炮！")
    skills = {
        "机枪扫射": [0.7, 5, False],  # 打5人 0.8
        "大炮攻击": [2, 1, False]  # 单打 200%
    }

    def __init__(self):
        Hero.__init__(self, "鲁班七号", 5000, 1500, 500, 15)

    def useSkill(self):
        skill = random.choice(tuple(self.skills.keys()))
        return skill


class HX(Hero):
    print("你们好，王者峡谷最帅的就是我韩信了~")
    skills = {
        "挑飞": [1.5, 1, False],  # 单打150%
        "横扫": [0, 1, True]  # 硬控
    }

    def __init__(self):
        Hero.__init__(self, "韩信", 8000, 1000, 750, 30)

    def useSkill(self):
        skill = random.choice(tuple(self.skills.keys()))
        return skill


class ZJ(Hero):
    print("我是甄姬，我最美！")
    skills = {
        "冰封术": [1, 3, False],  # 打三个 100%
        "横扫": [0, 1, True]  # 硬控
    }

    def __init__(self):
        Hero.__init__(self, "甄姬", 6000, 1500, 500, 25)

    def useSkill(self):
        skill = random.choice(tuple(self.skills.keys()))
        return skill


class CC(Hero):
    print("我是曹操，我来啦！")
    skills = {
        "斩杀": [1.5, 1, False],  # 单打150%
        "横扫": [-1, 1, False]  # 单人回血
    }

    def __init__(self):
        Hero.__init__(self, "曹操", 9000, 1000, 750, 15)

    def useSkill(self):
        skill = random.choice(tuple(self.skills.keys()))
        return skill
