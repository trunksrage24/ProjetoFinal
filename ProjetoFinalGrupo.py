# trabalho grupo computaçao - Vitor Daniel e Tiago Castro

# import da bibliotecas a ser usadas
import random

#Characters stats = hp, mp, mc(mana cost), ap, wp, Init, UpdateInit, sp(spell power), name
WarriorClass = [32, 5, 0, 2, 5, 2, 0, 0, "warrior"]
PriestClass = [20, 25, 0, 0, 2, 6, 0, 0, "priest"]
OrcClass1 = [15, 0, 0, 2, 2, 2, 0, 0, "orc1"]
OrcClass2 = [15, 0, 0, 2, 2, 2, 0, 0, "orc2"]
OrcClass3 = [15, 0, 0, 2, 2, 2, 0, 0, "orc3"]
OrcClass4 = [15, 0, 0, 2, 2, 2, 0, 0, "orc4"]
GhostClass = [10, 20, 0, 0, 0, 8, 0, 0, "ghost"]
#copy lists to update, so aqui e que vao mudar os valores
warrior = WarriorClass.copy()
priest = PriestClass.copy()
orc1 = OrcClass1.copy()
orc2 = OrcClass2.copy()
orc3 = OrcClass3.copy()
orc4 = OrcClass4.copy()
ghost = GhostClass.copy()
ListClass = [warrior, priest, orc1, orc2, orc3, orc4, ghost]

#fases iniciantes:

#def dados:
def DiceRoll(d):
    return random.randint(1, d)

#fase iniciante:dice roll
def RollInit(character):
    Init = DiceRoll(20) + character[5]
    character[6] = Init
    
#fase iniciante: sort
def InitFase (ListOfCharacter):
    for character in ListOfCharacter:
        RollInit(character)

#fases atacantes:

#ataque do warrior
def WarriorAttack(hp1, hp2, hp3, hp4, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpP, hpW, hpG):
    print("Your Warrior is getting ready to attack...")
    print("What will you have him do?")
    print("1: Use a powerfull magic learnt by the best Warriors only.")
    print("2: Attack without mercy on thy enemies.")
    Action = input()
    if Action == "1":
        print("Choose which spell you'd like your Warrior to use?")
        print("1:Rushdown - gain imense speed")
        Spell = input()
        if Spell == "1":
            Target = input("Choose target:")
            if Target == "1":
                print("You casted Rushdown on orc 1")
                mc = 5
                mp = mp - mc
                hp1 = hp1 - (wp -DiceRoll(4))
                if hp1 <= 0:
                    hp1 = 0
                    print("You killed orc 1!")
            elif Target == "2":
                print("You casted Rushdown on orc 2")
                mc = 5
                mp = mp - mc
                hp2 = hp2 - (wp -DiceRoll(4))
                if hp2 <= 0:
                    hp2 = 0
                    print("You killed orc 2!")
            elif Target == "3":
                print("You casted Rushdown on orc 3")
                mc = 5
                mp = mp - mc
                hp3 = hp3 - (wp -DiceRoll(4))
                if hp3 <= 0:
                    hp3 = 0
                    print("You killed orc 3!")
            elif Target == "4":
                print("You casted Rushdown on orc 4")
                mc = 5
                mp = mp - mc
                hp4 = hp4 - (wp -DiceRoll(4))
                if hp4 <= 0:
                    hp4 = 0
                    print("You killed orc 4!")
            elif Target == "5":
                print("You casted Rushdown on ghost")
                mc = 5
                mp = mp - mc
                hpG = hpG - (wp -DiceRoll(4))
                if hpG <= 0:
                    hpG = 0
                    print("You killed the ghost!")
            else:
                print("choose between 1 and 4")
    elif Action =="2":
        Target = input("Choose target:")
        if Target == "1":
            print("You struck orc 1")
            hp1 = hp1 - (wp - ap1)
            if hp1 <= 0:
                hp1 = 0
                print("You killed orc 1!")
        elif Target == "2":
            print("You struck orc 2")
            hp2 = hp2 - (wp - ap2)
            if hp2 <= 0:
                hp2 = 0
                print("You killed orc 2!")
        elif Target == "3":
            print("You struck orc 3")
            hp3 = hp3 - (wp - ap3)
            if hp3 <= 0:
                hp3 = 0
                print("You killed orc 3!")
        elif Target == "4":
            print("You struck orc 4")
            hp4 = hp4 - (wp - ap3)
            if hp4 <= 0:
                hp4 = 0
                print("You killed orc 4!")
    
    print("Warrior has", hpW, "life left")
    print("Priest has", hpP, "life left")
    print("Orc 1 has", hp1, "life left")
    print("Orc 2 has", hp2, "life left")
    print("Orc 3 has", hp3, "life left")
    print("Orc 4 has", hp4, "life left")
    print("Ghost has", hpG, "life left")
    
    return[hp1, hp2, hp3, hp4, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpP, hpW, hpG]

#ataque do priest
def PriestAttack(hp, hp1, hp2, hp3, hp4, hpW, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpG):
    print("Your Priest is getting ready to attack...")
    print("Choose your action")
    print("1:Magic")
    print("2:Attack")
    Action = input()
    if Action == "1":
        print("Choose your Spell")
        print("1:Mend")
        print("2:Exorcism")
        Spell = input()
        if Spell == "1":
            print("The priest casts mend, using the lord's grace to heal")
            Target = input("Choose target:")
            if Target == "1":
                print("You healed yourself!")
                mc = 3
                mp = mp - mc
                hp = hp + (DiceRoll(6) + wp)
            elif Target == "2":
                print("You healed the Warrior!")
                mc = 3
                mp = mp - mc
                hpW = hpW + (DiceRoll(6) + wp)
        elif Spell == "2":
            Target = input("Choose target:")
            if Target == "1":
                print("You casted Exorcism on orc 1 with the power of god at his hand using the Holy bible and his cross, dealing damage to the enemy")
                hp1 = hp1 - (DiceRoll(4) * 2)
                mc = 5
                mp = mp - mc
                if hp1 <= 0:
                    hp1 = 0
                    print("You killed orc 1!")
            elif Target == "2":
                print("You casted Exorcism on orc 2 with the power of god at his hand using the Holy bible and his cross, dealing damage to the enemy")                
                hp2 = hp2 - (DiceRoll(4) * 2)
                mc = 5
                mp = mp - mc
                if hp2 <= 0:
                    hp2 = 0
                    print("You killed orc 2!")
            elif Target == "3":
                print("You casted Exorcism on orc 3 with the power of god at his hand using the Holy bible and his cross, dealing damage to the enemy")
                hp3 = hp3 - (DiceRoll(4) * 2)
                mc = 5
                mp = mp - mc
                if hp3 <= 0:
                    hp3 = 0
                    print("You killed orc 3!")
            elif Target == "4":
                print("You casted Exorcism on orc 4 with the power of god at his hand using the Holy bible and his cross, dealing damage to the enemy")
                hp4 = hp4 - (DiceRoll(4) * 2)
                mc = 5
                mp = mp - mc
                if hp4 <= 0:
                    hp4 = 0
                    print("You killed orc 4!")
            elif Target == "5":
                print("You casted Exorcism on ghost")
                hpG = hpG - (DiceRoll(4) * 2)
                mc = 5
                mp = mp - mc
                if hpG <= 0:
                    hpG = 0
                    print("You killed the ghost!")

        print("Warrior has", hpW, "life left")
        print("Priest has", hp, "life left")
        print("Orc 1 has", hp1, "life left")
        print("Orc 2 has", hp2, "life left")
        print("Orc 3 has", hp3, "life left")
        print("Orc 4 has", hp4, "life left")
        print("Ghost has", hpG, "life left")

    elif Action == "2":
        Target = input("Choose a target:")
        if Target == "1":
            print("You struck orc 1")
            mc = 3
            mp = mp - mc
            hp1 = hp1 - (wp - ap1)
            if hp1 <= 0:
                hp1 = 0
                print("You killed orc 1!")
        elif Target == "2":
            print("You struck orc 2")
            hp2 = hp2 - (wp - ap2)
            if hp2 <= 0:
                hp2 = 0
                print("You killed orc 2!")
        elif Target == "3":
            print("You struck orc 3!")
            hp3 = hp3 - (wp - ap3)
            if hp3 <= 0:
                hp3 = 0
                print("You killed orc 3!")
        elif Target == "4":
            print("You struck orc 3!")
            hp4 = hp4 - (wp - ap4)
            if hp4 <= 0:
                hp4 = 0
                print("You killed orc 3!")
        else:
            print("Choose a target!")

        print("Warrior has", hpW, "life left")
        print("Priest has", hp, "life left")
        print("Orc 1 has", hp1, "life left")
        print("Orc 2 has", hp2, "life left")
        print("Orc 3 has", hp3, "life left")
        print("Orc 4 has", hp4, "life left")
        print("Ghost has", hpG, "life left")

    return[hp, hp1, hp2, hp3, hp4, hpW, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpG]

#ataque do orc 1
def OrcAttack1(hp, hp1, hp2, wp1, ap1, ap2, hpO2, hpO3, hpO4, hpG):        
    print("Orc 1 is getting ready to attack...")
    print("Orc 1 strikes!")
    print("... on ... ")
    dice = DiceRoll(2)
    if dice == 1:
        print("Orc1 attacks Warrior.")
        #hp = hp - (wp - ap)
        hp1 = hp1 - (wp1 - ap1)
        if hp1 <= 0:
            hp1 = 0
            print("Warrior died!")
        return[hp, hp1, hp2, wp1, ap1, ap2, hpO2, hpO3, hpO4, hpG]
    elif dice == 2:
        print("Orc1 attacks Priest.")
        #hp = hp - (wp - ap)
        hp2 = hp2 - (wp1 - ap2)
        if hp2 <= 0:
            hp2 = 0
            print("Priest died!")                                              
        return[hp, hp1, hp2, wp1, ap1, ap2, hpO2, hpO3, hpO4, hpG]
    
    print("Warrior has", hp1, "life left")
    print("Priest has", hp2, "life left")
    print("Orc 1 has", hp, "life left")
    print("Orc 2 has", hpO2, "life left")
    print("Orc 3 has", hpO3, "life left")
    print("Orc 4 has", hpO4, "life left")
    print("Ghost has", hpG, "life left")

#ataque do orc 2
def OrcAttack2(hp, hp1, hp2, wp2, ap1, ap2, hpO1, hpO3, hpO4, hpG):        
    print("Orc 2 is getting ready to attack...")
    print("Orc 2 strikes!")
    print("... on ... ")
    dice = DiceRoll(2)
    if dice == 1:
        print("Orc2 attacks Warrior.")
        #hp = hp - (wp - ap)
        hp1 = hp1 - (wp2 - ap1)
        if hp1 <= 0:
            hp1 = 0
            print("Warrior died!")
        return[hp, hp1, hp2, wp2, ap1, ap2, hpO1, hpO3, hpO4, hpG]

    elif dice == 2:
        print("Orc2 attacks Priest.")
        #hp = hp - (wp - ap)
        hp2 = hp2 - (wp2 - ap2)
        if hp2 <= 0:
            hp2 = 0
            print("Priest died!")
        return[hp, hp1, hp2, wp2, ap1, ap2, hpO1, hpO3, hpO4, hpG]

    print("Warrior has", hp1, "points of hp")
    print("Priest has", hp2, "points of hp")
    print("Orc 1 has", hpO1, "points of hp")
    print("Orc 2 has", hp, "points of hp")
    print("Orc 3 has", hpO3, "points of hp")
    print("Orc 4 has", hpO4, "points of hp")
    print("Ghost has", hpG, "life left")

#ataque do orc 3
def OrcAttack3(hp, hp1, hp2, wp3, ap1, ap2, hpO1, hpO2, hpO4, hpG):        
    print("Orc 3 is getting ready to attack...")
    print("Orc 3 strikes!")
    print("... on ... ")
    dice = DiceRoll(2)
    if dice == 1:
        print("Orc3 attacks Warrior.")
        #hp = hp - (wp - ap)
        hp1 = hp1 - (wp3 - ap1)
        if hp1 <= 0:
            hp1 = 0
            print("Warrior died!")
        return[hp, hp1, hp2, wp3, ap1, ap2, hpO1, hpO2, hpO4, hpG]
    if dice == 2:
        print("Orc3 attacks Priest.")
        #hp = hp - (wp - ap)
        hp2 = hp2 - (wp3 - ap2)
        if hp2 <= 0:
            hp2 = 0
            print("Priest died!")
        return[hp, hp1, hp2, wp3, ap1, ap2, hpO1, hpO2, hpO4, hpG]
    print("Warrior has", hp1, "points of hp")
    print("Priest has", hp2, "points of hp")
    print("Orc 1 has", hpO1, "points of hp")
    print("Orc 2 has", hpO2, "points of hp")
    print("Orc 3 has", hp, "points of hp")
    print("Orc 4 has", hpO4, "points of hp")
    print("Ghost has", hpG, "life left")

#ataque do orc 4
def OrcAttack4(hp, hp1, hp2, wp4, ap1, ap2, hpO1, hpO2, hpO3, hpG):        
    print("Orc 4 is getting ready to attack...")
    print("Orc 4 strikes!")
    print("... on ... ")
    dice = DiceRoll(2)
    if dice == 1:
        print("Orc4 attacks Warrior.")
        #hp = hp - (wp - ap)
        hp1 = hp1 - (wp4 - ap1)
        if hp1 <= 0:
            hp1 = 0
            print("Warrior died!")
        return[hp, hp1, hp2, wp4, ap1, ap2, hpO1, hpO2, hpO3, hpG]
    if dice == 2:
        print("Orc4 attacks Priest.")
        #hp = hp - (wp - ap)
        hp2 = hp2 - (wp4 - ap2)
        if hp2 <= 0:
            hp2 = 0
            print("Priest died!")
        return[hp, hp1, hp2, wp4, ap1, ap2, hpO1, hpO2, hpO3, hpG]
        
    print("Warrior has", hp1, "life left")
    print("Priest has", hp2, "life left")
    print("Orc 1 has", hpO1, "life left")
    print("Orc 2 has", hpO2, "life left")
    print("Orc 3 has", hpO3, "life left")
    print("Orc 4 has", hp, "life left")
    print("Ghost has", hpG, "life left")

#ataque do ghost
def GhostAttack(hp1, hp2, mp, mc, hpG, hpO1, hpO2, hpO3, hpO4):
    print("Enemy Ghost is getting ready to attack...")
    print("Ghost is preparing his attack...")
    dice = DiceRoll(2)
    if dice == 1:
        print("Ghost used Cursed Wave on Warrior!")
        print("This spell surrounds its enemy with a dark cloud which poisons whomever is in it.")
        mc = 6
        mp = mp - mc
        hp1 = hp1 - (DiceRoll(6) * 2)
        if hp1 <= 0:
            hp1 = 0
            print("Warrior died!")
        return[hp1, hp2, mp, mc, hpG, hpO1, hpO2, hpO3, hpO4]
    if dice == 2:
        print("Ghost used Cursed Wave on Priest!")
        print("This spell surrounds its enemy with a dark cloud which poisons whomever is in it.")
        mc = 6
        mp = mp - mc
        hp2 = hp2 - (DiceRoll(6) * 2)
        if hp2 <= 0:
            hp2 = 0
            print("Priest died!")
        return[hp1, hp2, mp, mc, hpG, hpO1, hpO2, hpO3, hpO4]

    print("Ghost has", hpG, "life left")
    print("Warrior has", hp1, "life left")
    print("Priest has", hp2, "life left") 
    print("Orc 1 has", hpO1, "life left")   
    print("Orc 2 has", hpO2, "life left")    
    print("Orc 3 has", hpO3, "life left")    
    print("Orc 4 has", hpO4, "life left")

    
#ciclo principal, n atualiza os valores
while (warrior[0] > 0 and priest[0] > 0) or (orc1[0] <= 0 and orc2[0] <= 0 and orc3[0] <= 0 and orc4[0] <= 0 and ghost[0] <= 0):

    #atribuir o  valor do novo init a cada classe
    InitFase(ListClass)

    #texto introdutorio
    print("The forces of darkness, beings from the beyond, come in search of souls to feed upon and the small town of Roesburg stands right in their path of destruction.")
    print("The helpless citizens, hire two adventurers to help them in their fight against the bringers of doom.")
    print("")
    print("The priest, a man of god believer in what is divine, his power comes from his faith, and he is determined to banish what is unholy using the power of his exorcism.")
    print("As a man of god, his first priority is to give others the lord's grace with his healing ability.")
    print("")
    print("The warrior, a man of honor and courage, represents what the people look up to, a shield for the week and frail. ")
    print("")
    print("Midnight approaches and the evil that comes with it, our adventures feel a chill down their spines as from the shadows four orcs appear, mindless creatures that arise do to the bedding of their lord , the ghost! .")
    print("Face to face with the host of darkness, our heroes only hope is that their power his enough to protect the townsfolk and survive")
    print("")
    print("Your adventure stars now! The dices has been thrown and the turns have been decided...")
    print("May the best player survive...")

    #sort mudar local    
    ListClass.sort(key=lambda CL : CL[6], reverse = True) #lambda sorts CL[6] inside ListCLass, like for function 
    print(ListClass[0][-1], "starts first. He has", ListClass[0][6], "points of Initiative")
    for i in ListClass:
        if i[6] == warrior[6]:
            
            #warrior = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #WarriorAttack = hp1, hp2, hp3, hp4, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpP, hpG
            W_attack = WarriorAttack(orc1[0], orc2[0], orc3[0], orc4[0], warrior[1], warrior[2], orc1[4], orc2[4], orc3[4], orc4[4], warrior[4], warrior[7], priest[0], warrior[0], ghost[0])
            
            #priest = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #PriestAttack = hp, hp1, hp2, hp3, hp4, hpW, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpG
            P_attack = PriestAttack(priest[0], orc1[0], orc2[0], orc3[0], orc4[0], warrior[0], priest[1], priest[2], orc1[5], orc2[5], orc3[5], orc4[5], priest[4], priest[7], ghost[0])
            
            #orc1 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack1 = hp, hp1, hp2, wp1, ap1, ap2, hpO2, hpO3, hpO4, hpG
            O1_attack = OrcAttack1(orc1[0], warrior[0], priest[0], orc1[4], warrior[3], priest[3], orc2[0], orc3[0], orc4[0], ghost[0])
            
            #orc2 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack2 = hp, hp1, hp2, wp1, ap1, ap2, hpO1, hpO3, hpO4, hpG          
            O2_attack = OrcAttack2(orc2[0], warrior[0], priest[0], orc2[4], warrior[3], priest[3], orc1[0], orc3[0], orc4[0], ghost[0])
            
            #orc3 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack3 = hp, hp1, hp2, wp3, ap1, ap2, hpO1, hpO2, hpO4, hpG
            O3_attack = OrcAttack3(orc3[0], warrior[0], priest[0], orc3[4], warrior[3], priest[3], orc1[0], orc2[0], orc4[0], ghost[0])
            
            #orc4 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack4 = hp, hp1, hp2, wp4, ap1, ap2, hpO1, hpO2, hpO3, hpG
            O4_attack = OrcAttack4(orc4[0], warrior[0], priest[0], orc4[4], warrior[3], priest[3], orc1[0], orc2[0], orc3[0], ghost[0])

            #ghost = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #GhostAttack = hp1, hp2, mp, mc, hpG, hpO1, hpO2, hpO3, hpO4
            G_attack = GhostAttack(warrior[0], priest[0], ghost[1], ghost[2], ghost[0], orc1[0], orc2[0], orc3[0], orc4[0])

            #update hp
            hp_warrior = (warrior[0] - O1_attack[1] - O2_attack[1] - O3_attack[1] - O4_attack[1] - G_attack[0] + priest[7])
            hp_priest = (P_attack[0] - O1_attack[2] - O2_attack[2] - O3_attack[2] - O4_attack[2] - G_attack[1] + priest[7])
            hp_orc1 = (O1_attack[0] - W_attack[0] - P_attack[1])
            hp_orc2 = (O2_attack[0] - W_attack[1] - P_attack[2])
            hp_orc3 = (O3_attack[0] - W_attack[2] - P_attack[3])
            hp_orc4 = (O4_attack[0] - W_attack[3] - P_attack[4])
            hp_ghost = (ghost[0] - warrior[13] - priest[14])
            #update armor
            ap_warrior = (warrior[3] - orc1[4] - orc2[4] - orc3[4] - orc4[4])
            ap_priest = (priest[3] - orc1[5] - orc2[5] - orc3[5] - orc4[5])
            ap_orc1 = (orc1[3] - W_attack[6] - P_attack[8])
            ap_orc2 = (orc2[3] - W_attack[7] - P_attack[9])
            ap_orc3 = (orc3[3] - W_attack[8] - P_attack[10])
            ap_orc4 = (orc4[3] - W_attack[9] - P_attack[11])

            #update all stats
            #player = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            warrior = [hp_warrior, W_attack[4], W_attack[5], W_attack[6], ap_warrior, warrior[5], i[6], W_attack[8], warrior[8]]
            priest = [hp_priest, P_attack[6], P_attack[7], ap_priest, P_attack[9], priest[5], i[6], P_attack[10], priest[8]]
            orc1 = [hp_orc1, orc1[1], orc1[2], ap_orc1, O1_attack[3], orc1[5], i[6], orc1[7], orc1[8]]
            orc2 = [hp_orc2, orc2[1], orc2[2], ap_orc2, O2_attack[3], orc2[5], i[6], orc2[7], orc2[8]]
            orc3 = [hp_orc3, orc3[1], orc3[2], ap_orc3, O3_attack[3], orc3[5], i[6], orc3[7], orc3[8]]
            orc4 = [hp_orc4, orc4[1], orc4[2], ap_orc4, O4_attack[3], orc4[5], i[6], orc4[7], orc4[8]]
            ghost = [hp_ghost, G_attack[1], G_attack[2], G_attack[3], G_attack[4], G_attack[5], G_attack[6], G_attack[7], G_attack[8]]

            #print do hp das listas atualizadas
            print("Warrior has", warrior[0], "life left")
            print("Priest has", priest[0], "life left")
            print("Orc 1 has", orc1[0], "life left")
            print("Orc 2 has", orc2[0], "life left")
            print("Orc 3 has", orc3[0], "life left")
            print("Orc 4 has", orc4[0], "life left")
            print("Ghost has", ghost[0], "life left")
        
        elif i[6] == priest[6]:
           
            #warrior = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #WarriorAttack = hp1, hp2, hp3, hp4, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpP, hpG
            W_attack = WarriorAttack(orc1[0], orc2[0], orc3[0], orc4[0], warrior[1], warrior[2], orc1[4], orc2[4], orc3[4], orc4[4], warrior[4], warrior[7], priest[0], warrior[0], ghost[0])
            
            #priest = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #PriestAttack = hp, hp1, hp2, hp3, hp4, hpW, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpG
            P_attack = PriestAttack(priest[0], orc1[0], orc2[0], orc3[0], orc4[0], warrior[0], priest[1], priest[2], orc1[5], orc2[5], orc3[5], orc4[5], priest[4], priest[7], ghost[0])
            
            #orc1 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack1 = hp, hp1, hp2, wp1, ap1, ap2, hpO2, hpO3, hpO4, hpG
            O1_attack = OrcAttack1(orc1[0], warrior[0], priest[0], orc1[4], warrior[3], priest[3], orc2[0], orc3[0], orc4[0], ghost[0])
            
            #orc2 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack2 = hp, hp1, hp2, wp1, ap1, ap2, hpO1, hpO3, hpO4, hpG          
            O2_attack = OrcAttack2(orc2[0], warrior[0], priest[0], orc2[4], warrior[3], priest[3], orc1[0], orc3[0], orc4[0], ghost[0])
            
            #orc3 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack3 = hp, hp1, hp2, wp3, ap1, ap2, hpO1, hpO2, hpO4, hpG
            O3_attack = OrcAttack3(orc3[0], warrior[0], priest[0], orc3[4], warrior[3], priest[3], orc1[0], orc2[0], orc4[0], ghost[0])
            
            #orc4 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack4 = hp, hp1, hp2, wp4, ap1, ap2, hpO1, hpO2, hpO3, hpG
            O4_attack = OrcAttack4(orc4[0], warrior[0], priest[0], orc4[4], warrior[3], priest[3], orc1[0], orc2[0], orc3[0], ghost[0])

            #ghost = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #GhostAttack = hp1, hp2, mp, mc, hpG, hpO1, hpO2, hpO3, hpO4
            G_attack = GhostAttack(warrior[0], priest[0], ghost[1], ghost[2], ghost[0], orc1[0], orc2[0], orc3[0], orc4[0])

            #update hp
            hp_warrior = (warrior[0] - O1_attack[1] - O2_attack[1] - O3_attack[1] - O4_attack[1] - G_attack[0] + priest[7])
            hp_priest = (P_attack[0] - O1_attack[2] - O2_attack[2] - O3_attack[2] - O4_attack[2] - G_attack[1] + priest[7])
            hp_orc1 = (O1_attack[0] - W_attack[0] - P_attack[1])
            hp_orc2 = (O2_attack[0] - W_attack[1] - P_attack[2])
            hp_orc3 = (O3_attack[0] - W_attack[2] - P_attack[3])
            hp_orc4 = (O4_attack[0] - W_attack[3] - P_attack[4])
            hp_ghost = (ghost[0] - warrior[13] - priest[14])
            #update armor
            ap_warrior = (warrior[3] - orc1[4] - orc2[4] - orc3[4] - orc4[4])
            ap_priest = (priest[3] - orc1[5] - orc2[5] - orc3[5] - orc4[5])
            ap_orc1 = (orc1[3] - W_attack[6] - P_attack[8])
            ap_orc2 = (orc2[3] - W_attack[7] - P_attack[9])
            ap_orc3 = (orc3[3] - W_attack[8] - P_attack[10])
            ap_orc4 = (orc4[3] - W_attack[9] - P_attack[11])

            #update all stats
            #player = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            warrior = [hp_warrior, W_attack[4], W_attack[5], W_attack[6], ap_warrior, warrior[5], i[6], W_attack[8], warrior[8]]
            priest = [hp_priest, P_attack[6], P_attack[7], ap_priest, P_attack[9], priest[5], i[6], P_attack[10], priest[8]]
            orc1 = [hp_orc1, orc1[1], orc1[2], ap_orc1, O1_attack[3], orc1[5], i[6], orc1[7], orc1[8]]
            orc2 = [hp_orc2, orc2[1], orc2[2], ap_orc2, O2_attack[3], orc2[5], i[6], orc2[7], orc2[8]]
            orc3 = [hp_orc3, orc3[1], orc3[2], ap_orc3, O3_attack[3], orc3[5], i[6], orc3[7], orc3[8]]
            orc4 = [hp_orc4, orc4[1], orc4[2], ap_orc4, O4_attack[3], orc4[5], i[6], orc4[7], orc4[8]]
            ghost = [hp_ghost, G_attack[1], G_attack[2], G_attack[3], G_attack[4], G_attack[5], G_attack[6], G_attack[7], G_attack[8]]

            #print do hp das listas atualizadas
            print("Warrior has", warrior[0], "life left")
            print("Priest has", priest[0], "life left")
            print("Orc 1 has", orc1[0], "life left")
            print("Orc 2 has", orc2[0], "life left")
            print("Orc 3 has", orc3[0], "life left")
            print("Orc 4 has", orc4[0], "life left")
            print("Ghost has", ghost[0], "life left")

        elif i[6] == orc1[6]:

            #warrior = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #WarriorAttack = hp1, hp2, hp3, hp4, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpP, hpG
            W_attack = WarriorAttack(orc1[0], orc2[0], orc3[0], orc4[0], warrior[1], warrior[2], orc1[4], orc2[4], orc3[4], orc4[4], warrior[4], warrior[7], priest[0], warrior[0], ghost[0])
            
            #priest = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #PriestAttack = hp, hp1, hp2, hp3, hp4, hpW, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpG
            P_attack = PriestAttack(priest[0], orc1[0], orc2[0], orc3[0], orc4[0], warrior[0], priest[1], priest[2], orc1[5], orc2[5], orc3[5], orc4[5], priest[4], priest[7], ghost[0])
            
            #orc1 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack1 = hp, hp1, hp2, wp1, ap1, ap2, hpO2, hpO3, hpO4, hpG
            O1_attack = OrcAttack1(orc1[0], warrior[0], priest[0], orc1[4], warrior[3], priest[3], orc2[0], orc3[0], orc4[0], ghost[0])
            
            #orc2 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack2 = hp, hp1, hp2, wp1, ap1, ap2, hpO1, hpO3, hpO4, hpG          
            O2_attack = OrcAttack2(orc2[0], warrior[0], priest[0], orc2[4], warrior[3], priest[3], orc1[0], orc3[0], orc4[0], ghost[0])
            
            #orc3 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack3 = hp, hp1, hp2, wp3, ap1, ap2, hpO1, hpO2, hpO4, hpG
            O3_attack = OrcAttack3(orc3[0], warrior[0], priest[0], orc3[4], warrior[3], priest[3], orc1[0], orc2[0], orc4[0], ghost[0])
            
            #orc4 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack4 = hp, hp1, hp2, wp4, ap1, ap2, hpO1, hpO2, hpO3, hpG
            O4_attack = OrcAttack4(orc4[0], warrior[0], priest[0], orc4[4], warrior[3], priest[3], orc1[0], orc2[0], orc3[0], ghost[0])

            #ghost = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #GhostAttack = hp1, hp2, mp, mc, hpG, hpO1, hpO2, hpO3, hpO4
            G_attack = GhostAttack(warrior[0], priest[0], ghost[1], ghost[2], ghost[0], orc1[0], orc2[0], orc3[0], orc4[0])

            #update hp
            hp_warrior = (warrior[0] - O1_attack[1] - O2_attack[1] - O3_attack[1] - O4_attack[1] - G_attack[0] + priest[7])
            hp_priest = (P_attack[0] - O1_attack[2] - O2_attack[2] - O3_attack[2] - O4_attack[2] - G_attack[1] + priest[7])
            hp_orc1 = (O1_attack[0] - W_attack[0] - P_attack[1])
            hp_orc2 = (O2_attack[0] - W_attack[1] - P_attack[2])
            hp_orc3 = (O3_attack[0] - W_attack[2] - P_attack[3])
            hp_orc4 = (O4_attack[0] - W_attack[3] - P_attack[4])
            hp_ghost = (ghost[0] - warrior[13] - priest[14])
            #update armor
            ap_warrior = (warrior[3] - orc1[4] - orc2[4] - orc3[4] - orc4[4])
            ap_priest = (priest[3] - orc1[5] - orc2[5] - orc3[5] - orc4[5])
            ap_orc1 = (orc1[3] - W_attack[6] - P_attack[8])
            ap_orc2 = (orc2[3] - W_attack[7] - P_attack[9])
            ap_orc3 = (orc3[3] - W_attack[8] - P_attack[10])
            ap_orc4 = (orc4[3] - W_attack[9] - P_attack[11])

            #update all stats
            #player = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            warrior = [hp_warrior, W_attack[4], W_attack[5], W_attack[6], ap_warrior, warrior[5], i[6], W_attack[8], warrior[8]]
            priest = [hp_priest, P_attack[6], P_attack[7], ap_priest, P_attack[9], priest[5], i[6], P_attack[10], priest[8]]
            orc1 = [hp_orc1, orc1[1], orc1[2], ap_orc1, O1_attack[3], orc1[5], i[6], orc1[7], orc1[8]]
            orc2 = [hp_orc2, orc2[1], orc2[2], ap_orc2, O2_attack[3], orc2[5], i[6], orc2[7], orc2[8]]
            orc3 = [hp_orc3, orc3[1], orc3[2], ap_orc3, O3_attack[3], orc3[5], i[6], orc3[7], orc3[8]]
            orc4 = [hp_orc4, orc4[1], orc4[2], ap_orc4, O4_attack[3], orc4[5], i[6], orc4[7], orc4[8]]
            ghost = [hp_ghost, G_attack[1], G_attack[2], G_attack[3], G_attack[4], G_attack[5], G_attack[6], G_attack[7], G_attack[8]]

            #print do hp das listas atualizadas
            print("Warrior has", warrior[0], "life left")
            print("Priest has", priest[0], "life left")
            print("Orc 1 has", orc1[0], "life left")
            print("Orc 2 has", orc2[0], "life left")
            print("Orc 3 has", orc3[0], "life left")
            print("Orc 4 has", orc4[0], "life left")
            print("Ghost has", ghost[0], "life left")

        elif i[6] == orc2[6]:
            
            #warrior = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #WarriorAttack = hp1, hp2, hp3, hp4, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpP, hpG
            W_attack = WarriorAttack(orc1[0], orc2[0], orc3[0], orc4[0], warrior[1], warrior[2], orc1[4], orc2[4], orc3[4], orc4[4], warrior[4], warrior[7], priest[0], warrior[0], ghost[0])
            
            #priest = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #PriestAttack = hp, hp1, hp2, hp3, hp4, hpW, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpG
            P_attack = PriestAttack(priest[0], orc1[0], orc2[0], orc3[0], orc4[0], warrior[0], priest[1], priest[2], orc1[5], orc2[5], orc3[5], orc4[5], priest[4], priest[7], ghost[0])
            
            #orc1 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack1 = hp, hp1, hp2, wp1, ap1, ap2, hpO2, hpO3, hpO4, hpG
            O1_attack = OrcAttack1(orc1[0], warrior[0], priest[0], orc1[4], warrior[3], priest[3], orc2[0], orc3[0], orc4[0], ghost[0])
            
            #orc2 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack2 = hp, hp1, hp2, wp1, ap1, ap2, hpO1, hpO3, hpO4, hpG          
            O2_attack = OrcAttack2(orc2[0], warrior[0], priest[0], orc2[4], warrior[3], priest[3], orc1[0], orc3[0], orc4[0], ghost[0])
            
            #orc3 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack3 = hp, hp1, hp2, wp3, ap1, ap2, hpO1, hpO2, hpO4, hpG
            O3_attack = OrcAttack3(orc3[0], warrior[0], priest[0], orc3[4], warrior[3], priest[3], orc1[0], orc2[0], orc4[0], ghost[0])
            
            #orc4 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack4 = hp, hp1, hp2, wp4, ap1, ap2, hpO1, hpO2, hpO3, hpG
            O4_attack = OrcAttack4(orc4[0], warrior[0], priest[0], orc4[4], warrior[3], priest[3], orc1[0], orc2[0], orc3[0], ghost[0])

            #ghost = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #GhostAttack = hp1, hp2, mp, mc, hpG, hpO1, hpO2, hpO3, hpO4
            G_attack = GhostAttack(warrior[0], priest[0], ghost[1], ghost[2], ghost[0], orc1[0], orc2[0], orc3[0], orc4[0])

            #update hp
            hp_warrior = (warrior[0] - O1_attack[1] - O2_attack[1] - O3_attack[1] - O4_attack[1] - G_attack[0] + priest[7])
            hp_priest = (P_attack[0] - O1_attack[2] - O2_attack[2] - O3_attack[2] - O4_attack[2] - G_attack[1] + priest[7])
            hp_orc1 = (O1_attack[0] - W_attack[0] - P_attack[1])
            hp_orc2 = (O2_attack[0] - W_attack[1] - P_attack[2])
            hp_orc3 = (O3_attack[0] - W_attack[2] - P_attack[3])
            hp_orc4 = (O4_attack[0] - W_attack[3] - P_attack[4])
            hp_ghost = (ghost[0] - warrior[13] - priest[14])
            #update armor
            ap_warrior = (warrior[3] - orc1[4] - orc2[4] - orc3[4] - orc4[4])
            ap_priest = (priest[3] - orc1[5] - orc2[5] - orc3[5] - orc4[5])
            ap_orc1 = (orc1[3] - W_attack[6] - P_attack[8])
            ap_orc2 = (orc2[3] - W_attack[7] - P_attack[9])
            ap_orc3 = (orc3[3] - W_attack[8] - P_attack[10])
            ap_orc4 = (orc4[3] - W_attack[9] - P_attack[11])

            #update all stats
            #player = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            warrior = [hp_warrior, W_attack[4], W_attack[5], W_attack[6], ap_warrior, warrior[5], i[6], W_attack[8], warrior[8]]
            priest = [hp_priest, P_attack[6], P_attack[7], ap_priest, P_attack[9], priest[5], i[6], P_attack[10], priest[8]]
            orc1 = [hp_orc1, orc1[1], orc1[2], ap_orc1, O1_attack[3], orc1[5], i[6], orc1[7], orc1[8]]
            orc2 = [hp_orc2, orc2[1], orc2[2], ap_orc2, O2_attack[3], orc2[5], i[6], orc2[7], orc2[8]]
            orc3 = [hp_orc3, orc3[1], orc3[2], ap_orc3, O3_attack[3], orc3[5], i[6], orc3[7], orc3[8]]
            orc4 = [hp_orc4, orc4[1], orc4[2], ap_orc4, O4_attack[3], orc4[5], i[6], orc4[7], orc4[8]]
            ghost = [hp_ghost, G_attack[1], G_attack[2], G_attack[3], G_attack[4], G_attack[5], G_attack[6], G_attack[7], G_attack[8]]

            #print do hp das listas atualizadas
            print("Warrior has", warrior[0], "life left")
            print("Priest has", priest[0], "life left")
            print("Orc 1 has", orc1[0], "life left")
            print("Orc 2 has", orc2[0], "life left")
            print("Orc 3 has", orc3[0], "life left")
            print("Orc 4 has", orc4[0], "life left")
            print("Ghost has", ghost[0], "life left")

        elif i[6] == orc3[6]:
            
            #warrior = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #WarriorAttack = hp1, hp2, hp3, hp4, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpP, hpG
            W_attack = WarriorAttack(orc1[0], orc2[0], orc3[0], orc4[0], warrior[1], warrior[2], orc1[4], orc2[4], orc3[4], orc4[4], warrior[4], warrior[7], priest[0], warrior[0], ghost[0])
            
            #priest = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #PriestAttack = hp, hp1, hp2, hp3, hp4, hpW, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpG
            P_attack = PriestAttack(priest[0], orc1[0], orc2[0], orc3[0], orc4[0], warrior[0], priest[1], priest[2], orc1[5], orc2[5], orc3[5], orc4[5], priest[4], priest[7], ghost[0])
            
            #orc1 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack1 = hp, hp1, hp2, wp1, ap1, ap2, hpO2, hpO3, hpO4, hpG
            O1_attack = OrcAttack1(orc1[0], warrior[0], priest[0], orc1[4], warrior[3], priest[3], orc2[0], orc3[0], orc4[0], ghost[0])
            
            #orc2 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack2 = hp, hp1, hp2, wp1, ap1, ap2, hpO1, hpO3, hpO4, hpG          
            O2_attack = OrcAttack2(orc2[0], warrior[0], priest[0], orc2[4], warrior[3], priest[3], orc1[0], orc3[0], orc4[0], ghost[0])
            
            #orc3 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack3 = hp, hp1, hp2, wp3, ap1, ap2, hpO1, hpO2, hpO4, hpG
            O3_attack = OrcAttack3(orc3[0], warrior[0], priest[0], orc3[4], warrior[3], priest[3], orc1[0], orc2[0], orc4[0], ghost[0])
            
            #orc4 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack4 = hp, hp1, hp2, wp4, ap1, ap2, hpO1, hpO2, hpO3, hpG
            O4_attack = OrcAttack4(orc4[0], warrior[0], priest[0], orc4[4], warrior[3], priest[3], orc1[0], orc2[0], orc3[0], ghost[0])

            #ghost = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #GhostAttack = hp1, hp2, mp, mc, hpG, hpO1, hpO2, hpO3, hpO4
            G_attack = GhostAttack(warrior[0], priest[0], ghost[1], ghost[2], ghost[0], orc1[0], orc2[0], orc3[0], orc4[0])

            #update hp
            hp_warrior = (warrior[0] - O1_attack[1] - O2_attack[1] - O3_attack[1] - O4_attack[1] - G_attack[0] + priest[7])
            hp_priest = (P_attack[0] - O1_attack[2] - O2_attack[2] - O3_attack[2] - O4_attack[2] - G_attack[1] + priest[7])
            hp_orc1 = (O1_attack[0] - W_attack[0] - P_attack[1])
            hp_orc2 = (O2_attack[0] - W_attack[1] - P_attack[2])
            hp_orc3 = (O3_attack[0] - W_attack[2] - P_attack[3])
            hp_orc4 = (O4_attack[0] - W_attack[3] - P_attack[4])
            hp_ghost = (ghost[0] - warrior[13] - priest[14])
            #update armor
            ap_warrior = (warrior[3] - orc1[4] - orc2[4] - orc3[4] - orc4[4])
            ap_priest = (priest[3] - orc1[5] - orc2[5] - orc3[5] - orc4[5])
            ap_orc1 = (orc1[3] - W_attack[6] - P_attack[8])
            ap_orc2 = (orc2[3] - W_attack[7] - P_attack[9])
            ap_orc3 = (orc3[3] - W_attack[8] - P_attack[10])
            ap_orc4 = (orc4[3] - W_attack[9] - P_attack[11])

            #update all stats
            #player = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            warrior = [hp_warrior, W_attack[4], W_attack[5], W_attack[6], ap_warrior, warrior[5], i[6], W_attack[8], warrior[8]]
            priest = [hp_priest, P_attack[6], P_attack[7], ap_priest, P_attack[9], priest[5], i[6], P_attack[10], priest[8]]
            orc1 = [hp_orc1, orc1[1], orc1[2], ap_orc1, O1_attack[3], orc1[5], i[6], orc1[7], orc1[8]]
            orc2 = [hp_orc2, orc2[1], orc2[2], ap_orc2, O2_attack[3], orc2[5], i[6], orc2[7], orc2[8]]
            orc3 = [hp_orc3, orc3[1], orc3[2], ap_orc3, O3_attack[3], orc3[5], i[6], orc3[7], orc3[8]]
            orc4 = [hp_orc4, orc4[1], orc4[2], ap_orc4, O4_attack[3], orc4[5], i[6], orc4[7], orc4[8]]
            ghost = [hp_ghost, G_attack[1], G_attack[2], G_attack[3], G_attack[4], G_attack[5], G_attack[6], G_attack[7], G_attack[8]]

            #print do hp das listas atualizadas
            print("Warrior has", warrior[0], "life left")
            print("Priest has", priest[0], "life left")
            print("Orc 1 has", orc1[0], "life left")
            print("Orc 2 has", orc2[0], "life left")
            print("Orc 3 has", orc3[0], "life left")
            print("Orc 4 has", orc4[0], "life left")
            print("Ghost has", ghost[0], "life left")
        
        elif i[6] == orc4[6]:
            
            #warrior = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #WarriorAttack = hp1, hp2, hp3, hp4, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpP, hpG
            W_attack = WarriorAttack(orc1[0], orc2[0], orc3[0], orc4[0], warrior[1], warrior[2], orc1[4], orc2[4], orc3[4], orc4[4], warrior[4], warrior[7], priest[0], warrior[0], ghost[0])
            
            #priest = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #PriestAttack = hp, hp1, hp2, hp3, hp4, hpW, mp, mc, ap1, ap2, ap3, ap4, wp, sp, hpG
            P_attack = PriestAttack(priest[0], orc1[0], orc2[0], orc3[0], orc4[0], warrior[0], priest[1], priest[2], orc1[5], orc2[5], orc3[5], orc4[5], priest[4], priest[7], ghost[0])
            
            #orc1 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack1 = hp, hp1, hp2, wp1, ap1, ap2, hpO2, hpO3, hpO4, hpG
            O1_attack = OrcAttack1(orc1[0], warrior[0], priest[0], orc1[4], warrior[3], priest[3], orc2[0], orc3[0], orc4[0], ghost[0])
            
            #orc2 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack2 = hp, hp1, hp2, wp1, ap1, ap2, hpO1, hpO3, hpO4, hpG          
            O2_attack = OrcAttack2(orc2[0], warrior[0], priest[0], orc2[4], warrior[3], priest[3], orc1[0], orc3[0], orc4[0], ghost[0])
            
            #orc3 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack3 = hp, hp1, hp2, wp3, ap1, ap2, hpO1, hpO2, hpO4, hpG
            O3_attack = OrcAttack3(orc3[0], warrior[0], priest[0], orc3[4], warrior[3], priest[3], orc1[0], orc2[0], orc4[0], ghost[0])
            
            #orc4 = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #OrcAttack4 = hp, hp1, hp2, wp4, ap1, ap2, hpO1, hpO2, hpO3, hpG
            O4_attack = OrcAttack4(orc4[0], warrior[0], priest[0], orc4[4], warrior[3], priest[3], orc1[0], orc2[0], orc3[0], ghost[0])

            #ghost = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            #GhostAttack = hp1, hp2, mp, mc, hpG, hpO1, hpO2, hpO3, hpO4
            G_attack = GhostAttack(warrior[0], priest[0], ghost[1], ghost[2], ghost[0], orc1[0], orc2[0], orc3[0], orc4[0])

            #update hp
            hp_warrior = (warrior[0] - O1_attack[1] - O2_attack[1] - O3_attack[1] - O4_attack[1] - G_attack[0] + priest[7])
            hp_priest = (P_attack[0] - O1_attack[2] - O2_attack[2] - O3_attack[2] - O4_attack[2] - G_attack[1] + priest[7])
            hp_orc1 = (O1_attack[0] - W_attack[0] - P_attack[1])
            hp_orc2 = (O2_attack[0] - W_attack[1] - P_attack[2])
            hp_orc3 = (O3_attack[0] - W_attack[2] - P_attack[3])
            hp_orc4 = (O4_attack[0] - W_attack[3] - P_attack[4])
            hp_ghost = (ghost[0] - warrior[13] - priest[14])
            #update armor
            ap_warrior = (warrior[3] - orc1[4] - orc2[4] - orc3[4] - orc4[4])
            ap_priest = (priest[3] - orc1[5] - orc2[5] - orc3[5] - orc4[5])
            ap_orc1 = (orc1[3] - W_attack[6] - P_attack[8])
            ap_orc2 = (orc2[3] - W_attack[7] - P_attack[9])
            ap_orc3 = (orc3[3] - W_attack[8] - P_attack[10])
            ap_orc4 = (orc4[3] - W_attack[9] - P_attack[11])

            #update all stats
            #player = hp, mp, mc, ap, wp, Init, UpdateInit, sp(spell power), name
            warrior = [hp_warrior, W_attack[4], W_attack[5], W_attack[6], ap_warrior, warrior[5], i[6], W_attack[8], warrior[8]]
            priest = [hp_priest, P_attack[6], P_attack[7], ap_priest, P_attack[9], priest[5], i[6], P_attack[10], priest[8]]
            orc1 = [hp_orc1, orc1[1], orc1[2], ap_orc1, O1_attack[3], orc1[5], i[6], orc1[7], orc1[8]]
            orc2 = [hp_orc2, orc2[1], orc2[2], ap_orc2, O2_attack[3], orc2[5], i[6], orc2[7], orc2[8]]
            orc3 = [hp_orc3, orc3[1], orc3[2], ap_orc3, O3_attack[3], orc3[5], i[6], orc3[7], orc3[8]]
            orc4 = [hp_orc4, orc4[1], orc4[2], ap_orc4, O4_attack[3], orc4[5], i[6], orc4[7], orc4[8]]
            ghost = [hp_ghost, G_attack[1], G_attack[2], G_attack[3], G_attack[4], G_attack[5], G_attack[6], G_attack[7], G_attack[8]]

            #print do hp das listas atualizadas
            print("Warrior has", warrior[0], "life left")
            print("Priest has", priest[0], "life left")
            print("Orc 1 has", orc1[0], "life left")
            print("Orc 2 has", orc2[0], "life left")
            print("Orc 3 has", orc3[0], "life left")
            print("Orc 4 has", orc4[0], "life left")
            print("Ghost has", ghost[0], "life left")
        
    #quando perdes o jogo
    print("Game Over!!!")
    print("Better luck next time...")       
    break