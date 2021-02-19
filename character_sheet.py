def bonus(num):
    return int((num-10)/2)

def proficiency_bonus(lvl):
    return 2+int((lvl-1)/4)

class character_sheet():

    def __init__(self,stat_choice):
        
        self.lvl=1
        self.proficiency=proficiency_bonus(self.lvl)
        self.speed=30
        #unpacking attributes chosen by player

        (self.strength,
        self.dexterity,
        self.constitution,
        self.intelligence,
        self.wisdom,
        self.charisma) = stat_choice
        
        #computating bonus attributes
        (self.bon_strength,
        self.bon_dexterity,
        self.bon_constitution,
        self.bon_intelligence,
        self.bon_wisdom,
        self.bon_charisma) = [bonus(i) for i in stat_choice]
        
        #initializing saving throws and stuff
        
        (self.st_strength,
        self.st_dexterity,
        self.st_constitution,
        self.st_intelligence,
        self.st_wisdom,
        self.st_charisma) = [bonus(i) for i in stat_choice]
        
        #strength
        self.athletics=self.bon_strength

        #dexterity
        self.acrobatics=self.sleigh_of_hand=self.stealth=self.bon_dexterity
        
        self.initiative=self.bon_dexterity      #initiative
        self.armor_class=10+self.bon_dexterity  #armor class
        
        #constitution
        self.hp=self.constitution * self.lvl

        #intelligence
        self.arcana=self.history=self.investigation=self.bon_intelligence
        self.nature=self.religion=self.bon_intelligence 

        #wisdom
        self.animal_handling=self.insight=self.medicine=self.bon_wisdom
        self.perception=self.survival=self.bon_wisdom
        
        #charisma
        self.deception=self.intimidation=self.performance=self.bon_charisma
        self.persuasion=self.bon_charisma
        



        return

