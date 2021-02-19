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
'''
from prototype import *
import random as rn
#prov=('nome','classe','razza','background.txt',tuple([rn.choice(range(15))in range(6)]))



def dice(num):
    return rn.choice(range(1,num+1))


class _class():
    #aggiungere le altre classi poi
    stat_initial={'fighter':{'bonus_life':10,'hit_dice':10},
                  'rogue':{'bonus_life':8,'hit_dice':8}
                  }

    def __init__(self,choice):
        self.life_dice=self.stat_initial[choice]['bonus_life']
        self.hit_dice_size=self.stat_initial[choice]['hit_dice']
        del(self.stat_initial)
        return


class Skill_list():
    def __init__(self):
        return

class Player(_class):

    def __init__(self,choice,id):
        self.reset(self,choice,id)
    
    def bonus(self,num):
        return int((num-10)/2)
    
    def __repr__(self):
        return
    
    def reset(self,choice,id):

        #initializing parent classes
        super().__init__(choice[1])

        
        
        
        
        return
    
    print('aloha')
