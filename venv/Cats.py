import random
class Cats:
    def __init__(self, asleep, height, setting, sound_after_eating):
        self.asleep= asleep
        self.height = height
        self.setting = setting
        self.sound_after_eating = sound_after_eating

    def Is_Asleep(self):
        return self.asleep

    def Go_To_Sleep(self):
        self.asleep = True

    def Wakeup(self):
        self.asleep = False

    def Get_Setting(self):
        return self.setting

    def Set_Setting(self, setting):
        self.setting = setting

    def Get_Average_Height(self):
        return self.height

    def Set_Average_Height(self, height):
        self.height = height

    def Sound_After_Eating(self):
        return self.sound_after_eating

class Lion(Cats):
    def speak(self):
        print("")

class Cheetah(Cats):
    def speak(self):
        print("")

class Domestic_Cat(Cats):
    def random_sound_after_eating(self, just_eat):
        if just_eat==True:
            choice = random.choice([True, False])
            if choice == True:
                print("it will do i suppose")


L = Lion(False, "wild", 1100, "Roar!!!!")
print(L.sound_after_eating)
C = Cheetah(False, "wild", 0,"Zzzzzzz")
print(C.sound_after_eating)
DC = Domestic_Cat(False, "domestic", 23,"Purrrrrrr")
print(DC.sound_after_eating)
DC.random_sound_after_eating(True)










