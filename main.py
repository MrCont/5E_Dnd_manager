'''
-nome personaggio, id
-classe
-razza
-livello
-background
-attributi
-bonus proficiency
-saving throws
-proficiency
-
'''
import random as rn
class _class():
    #aggiungere le altre classi poi
    stat_initial={'fighter':{'bonus_life':10,'hit_dice':10},
                  'rogue':{'bonus_life':8,'hit_dice':8}
                  }
prova=('nome','classe','razza','background.txt',tuple([rn.choice(range(15))in range(6)]))

def dice(num):
    return rn.choice(range(1,num+1))

class Player(_class):

    def __init__(self,choice,id):
        self.reset(self,choice,id)
    
    def bonus(self,num):
        return int((num-10)/2)
    
    def __repr__(self):
        return
    
    def reset(self,choice,id):
        super().__init__(choice[1])
        self.strength,self.dexterity,self.constitution,self.intelligence,self.wisdom,self.charisma=choice[4]
        self.proficiency_bonus=2
        self.saving_throws=[bonus(i) for i in choice[4]]
        return
    
    def __init__(self,choice):
        self.life_dice=self.stat_initial[choice]['bonus_life']
        self.hit_dice_size=self.stat_initial[choice]['hit_dice']
        del(self.stat_initial)
        return
    print('aloha')
