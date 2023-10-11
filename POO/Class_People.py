from datetime import datetime

class People: 
    corrent_year = datetime.now().year

    def __init__(self, name, year_old,height, work, sexo, speaking = False, Eating = False, walking = False,):
        self.name = name
        self.year_old = year_old
        self.altura = height
        self.work = work
        self.sexo = sexo
        self.speaking = speaking
        self.Eating = Eating
        self.walking = walking
    


    def Eat(self, food):
         if self.Eating:
            print(f'{self.name} already Eating.')
            return
         if self.speaking:
             print(f"{self.name} can't to Eat speaking !")
             return

         print(f'{self.name} is Eating {food}')
         self.Eating = True


    def StopEat(self):
        if not self.Eating:
            print(f'{self.name} not Eating.')
            return
        
        print(f'{self.name} stopped Eating !')
        self.Eating = False



    def Speak(self, about):
        if self.Eating:
            print(f"{self.name} Can't talk while Eating.")
            return
        if self.speaking:
            print(f'{self.name} Already talking.')
            return

        print(f'{self.name} Is talking about {about}')
        self.speaking = True

    def StopSpeak(self):
        if not self.speaking:
            print(f'{self.name} Not talking !')
            return
        
        print(f'{self.name} Stopped talking !')
        self.speaking = False



    def Walk(self):
        if self.walking:
            print(f'You are already walking ! ')
            return
        
        if self.Eating:
            print(f"{self.name} Can't to eat walking ! ")
            return


        print(f'{self.name} are walking')
        self.walking = True


    def StopWalk(self):
        if not self.walking:
            print(f'You are not walking !')
            return
        
        print(f'{self.name} stopped walking !')
        self.walking = False




    def Get_corrent_year(self):
        return self.corrent_year - self.year_old