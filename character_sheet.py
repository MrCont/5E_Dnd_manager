from character_pdf_print import export_player_to_pdf

# float range() function
def frange(start,stop,step):
    while start>stop:
        yield float(start)
        start+=step


def bonus(num):
    return int((num-10)/2)


def proficiency_func(lvl):
    return 2+int((lvl-1)/4)


def excess_avg(dice_size):
    return 1+int((1+dice_size)/2)


#choice = (nome,razza,classe,bg,stats)
class character_sheet():

    def __init__(self,base_choices,stat_choice):

        self.pc_name , self.pc_race , self.pc_class , self.pc_background  = base_choices
        self.lvl=1
        self.hit_dice_number , self.hit_dice_size = self.lvl , 0 
        self.proficiency_bonus = proficiency_func(self.lvl)
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
        self.hp=self.bon_constitution #* self.lvl

        #intelligence
        self.arcana=self.history=self.investigation=self.bon_intelligence
        self.nature=self.religion=self.bon_intelligence 

        #wisdom
        self.animal_handling=self.insight=self.medicine=self.bon_wisdom
        self.perception=self.survival=self.bon_wisdom
        
        #charisma
        self.deception=self.intimidation=self.performance=self.bon_charisma
        self.persuasion=self.bon_charisma


        race_mod(self)
        class_mod(self)
        return
    

    def __repr__(self):
        print("character sheet")
        print(f"name:{self.pc_name}\t race:{self.pc_race}\t class:{self.pc_class}")
        print(f"prof_bonus:+{self.proficiency_bonus}")
        print(f"hp:{self.hp}")
        print(f"str: +{self.bon_strength}({self.strength})")
        print(f"dex: +{self.bon_dexterity}({self.dexterity})")
        print(f"con: +{self.bon_constitution}({self.constitution})")
        print(f"int: +{self.bon_intelligence}({self.intelligence})")
        print(f"wis: +{self.bon_wisdom}({self.wisdom})")
        print(f"cha: +{self.bon_charisma}({self.charisma})")
        return '_'*40


    def export_pdf(self):
        #quick generators to make y pos 
        y_bon_stats = frange(595,595-6*71.5,-71.5)
        x_stats = 50
        y_stats = frange(620,620-6*71,-71)
        y_skills = frange(463.0,463.0-13.5*18,-13.5)
        x_skills = 116
        attr_pos = (
                    #SKILLS
                    (x_skills,next(y_skills),str(self.acrobatics)),
                    (x_skills,next(y_skills),str(self.animal_handling)),
                    (x_skills,next(y_skills),str(self.arcana)),
                    (x_skills,next(y_skills),str(self.athletics)),
                    (x_skills,next(y_skills),str(self.deception)),
                    (x_skills,next(y_skills),str(self.history)),
                    (x_skills,next(y_skills),str(self.insight)),
                    (x_skills,next(y_skills),str(self.intimidation)),
                    (x_skills,next(y_skills),str(self.investigation)),
                    (x_skills,next(y_skills),str(self.medicine)),
                    (x_skills,next(y_skills),str(self.nature)),
                    (x_skills,next(y_skills),str(self.perception)),
                    (x_skills,next(y_skills),str(self.performance)),
                    (x_skills,next(y_skills),str(self.persuasion)),
                    (x_skills,next(y_skills),str(self.religion)),
                    (x_skills,next(y_skills),str(self.sleigh_of_hand)),
                    (x_skills,next(y_skills),str(self.stealth)),
                    (x_skills,next(y_skills),str(self.survival)),

                    #STATS
                    (x_stats,next(y_stats),str(self.strength)),
                    (x_stats,next(y_stats),str(self.dexterity)),
                    (x_stats,next(y_stats),str(self.constitution)),
                    (x_stats,next(y_stats),str(self.intelligence)),
                    (x_stats,next(y_stats),str(self.wisdom)),
                    (x_stats,next(y_stats),str(self.charisma)), 

                    #BONUS STATS
                    (x_stats+2,next(y_bon_stats),str(self.bon_strength)),
                    (x_stats+2,next(y_bon_stats),str(self.bon_dexterity)),
                    (x_stats+2,next(y_bon_stats),str(self.bon_constitution)),
                    (x_stats+2,next(y_bon_stats),str(self.bon_intelligence)),
                    (x_stats+2,next(y_bon_stats),str(self.bon_wisdom)),
                    (x_stats+2,next(y_bon_stats),str(self.bon_charisma)) 
                    )
        export_player_to_pdf("character_sheet.pdf","test.pdf",attr_pos)
        return


def class_mod(char_sheet):
    #hit points assignment
    dice_size = {'fighter':10,'rogue':8}
    char_sheet.hit_dice_size = dice_size[char_sheet.pc_class]
    if char_sheet.lvl == 1:
        char_sheet.hp +=char_sheet.hit_dice_size
    else:
        char_sheet.hp += excess_avg(char_sheet.hit_dice_size) + char_sheet.bon_constitution
    
    #saving throws proficiencies bonus
    #FIGHTER
    if char_sheet.pc_class == 'fighter':
        char_sheet.st_strength      += char_sheet.proficiency_bonus
        char_sheet.st.constitution  += char_sheet.proficiency_bonus

    #ROGUE
    if char_sheet.pc_class == 'rogue':
        char_sheet.st_dexterity     += char_sheet.proficiency_bonus
        char_sheet.st_intelligence  += char_sheet.proficiency_bonus
    return


def race_mod(char_sheet):
    race_modfiers = {'human'    :   [1,1,1,1,1,1],
                     'high_elf' :   [0,2,0,1,0,0]
                     }
    char_sheet.strength         +=  race_modfiers[char_sheet.pc_race][0]
    char_sheet.dexterity        +=  race_modfiers[char_sheet.pc_race][1]
    char_sheet.constitution     +=  race_modfiers[char_sheet.pc_race][2]
    char_sheet.intelligence     +=  race_modfiers[char_sheet.pc_race][3]
    char_sheet.wisdom           +=  race_modfiers[char_sheet.pc_race][4]
    char_sheet.charisma         +=  race_modfiers[char_sheet.pc_race][5]

    char_sheet.bon_strength         =   bonus(char_sheet.strength)
    char_sheet.bon_dexterity        =   bonus(char_sheet.dexterity)
    char_sheet.bon_constitution     =   bonus(char_sheet.constitution)
    char_sheet.bon_intelligence     =   bonus(char_sheet.intelligence)
    char_sheet.bon_wisdom           =   bonus(char_sheet.wisdom)
    char_sheet.bon_charisma         =   bonus(char_sheet.charisma)
    return
    
    
#playground
scelte_base = ['gigi','high_elf','rogue','tarallo']
array_statistiche = [8,14,13,15,12,10]
tizio = character_sheet(scelte_base,array_statistiche)
tizio.export_pdf()
print("BASE")
print(tizio)

'''
print("BONUS RAZZA")
race_mod(tizio)
print(tizio)

print("BONUS CLASSE")
class_mod(tizio)
print(tizio)
'''
