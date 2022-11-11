#trabalho grupo computaçao - Vitor Daniel e Tiago Castro

#import da bibliotecas a ser usadas
import random

#Characters stats = hp, mp, mc(mana cost), ap, wp, Init, UpdateInit, sp(spell power), name
WarriorClass = [32, 5, 2, 5, 2, 0, 0, "warrior"]
PriestClass = [20, 25, 0, 2, 6, 0, 0, "priest"]
OrcClass1 = [15, 0, 0, 2, 2, 2, 0, "orc"]
OrcClass2 = [15, 0, 0, 2, 2, 2, 0, "orc"]
OrcClass3 = [15, 0, 0, 2, 2, 2, 0, "orc"]
ListClass = [WarriorClass, PriestClass, OrcClass1, OrcClass2, OrcClass3]

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
def WarriorAttack(hp1, hp2, hp3, mp, mc, ap, wp, sp):

    print("Choose your action")
    print("1:Magic")
    print("2:Attack")
    Action = input()
    if Action == 1:
        print("Choose your Spell")
        print("1:Rushdown")
        Spell = input()
        if Spell == 1:
            Target = input("Choose target:")
            if Target == 1:
                print("You casted Rushdown on the enemy")
                mc = 5
                mp = mp - mc
                hp1 = hp1 - (sp-ap)
                if hp1 <= 0:
                    print("You killed enemy 1!")
            elif Target == 2:
                print("You casted Rushdown on the enemy")
                mc = 5
                mp = mp - mc
                hp2 = hp2 - (sp-ap)
                if hp2 <= 0:
                    print("You killed enemy 2!")
            elif Target == 3:
                print("You casted Rushdown on the enemy")
                mc = 5
                mp = mp - mc
                hp3 = hp3 - (sp-ap)
                if hp3 <= 0:
                    print("You killed enemy 3!")
    elif Action ==2:
        Target = input("Choose target:")
        if Target == 1:
            print("You struck the enemy")
            hp1 = hp1 - (wp - ap)
            if hp1 <= 0:
                print("You killed an enemy!")
        elif Target == 2:
            print("You struck the enemy")
            hp2 = hp2 - (wp - ap)
            if hp2 <= 0:
                print("You killed an enemy!")
        elif Target == 3:
            print("You struck the enemy")
            hp3 = hp3 - (wp - ap)
            if hp3 <= 0:
                print("You killed an enemy!")
    return[hp1, hp2, hp3, mp, mc, ap, wp, sp]
#ataque do priest
def PriestAttack(hp, hp1, hp2, hp3, hp4, mp, mc, ap, wp, sp):

    print("Choose your action")
    print("1:Magic")
    print("2:Attack")
    Action = input()
    if Action == 1:
        print("Choose your Spell")
        print("1:Mend")
        print("2:Exorcism")
        Spell = input()
        if Spell == 1:
            Target = input("Choose target:")
            if Target == 1:
                print("You healed yourself!")
                mc = 3
                mp = mp - mc
                hp = hp + sp
            elif Target == 2:
                print("You healed warrior!")
                mc = 3
                mp = mp - mc
                hp4 = hp4 + sp
        elif Spell == 2:
            Target = input("Choose target:")
            if Target == 1:
                print("You casted Exorcism on enemy 1")
                hp1 = hp1 - (sp - ap)
                mc = 5
                mp = mp - mc
                if hp1 <= 0:
                    print("You killed enemy 1!")
            elif Target == 2:
                print("You casted Exorcism on enemy 2")
                hp2 = hp2 - (sp - ap)
                mc = 5
                mp = mp - mc
                if hp2 <= 0:
                    print("You killed enemy 2!")
            elif Target == 3:
                print("You casted Exorcism on enemy 3")
                hp3 = hp3 - (sp - ap)
                mc = 5
                mp = mp - mc
                if hp3 <= 0:
                    print("You killed enemy 3!")
    elif Action ==2:
        Target = input("Choose a target:")
        if Target == 1:
            print("You struck enemy 1")
            hp1 = hp1 - (wp - ap)
            if hp1 <= 0:
                print("You killed enemy 1!")
        elif Target == 2:
            print("You struck enemy 2")
            hp2 = hp2 - (wp - ap)
            if hp2 <= 0:
                print("You killed enemy 2!")
        elif Target == 3:
            print("You struck enemy 3!")
            hp3 = hp3 - (wp - ap)
            if hp3 <= 0:
                print("You killed enemy 3!")
        else:
            print("Choose a target!")
    return[hp, hp1, hp2, hp3, hp4, mp]

#ataque do orc 1
def OrcAttack1(hp1, hp2, wp1, ap1, ap2):        
    print("Enemy 1 strikes!")
    print(random.choice(range(0,1)))
    #0 = WarriorClass[0]
    #1 = PriestClass[0]
    if random.choice == 0:
        #hp = hp - (wp - ap)
        hp1 = hp1 - (wp1 - ap1)
        if hp1 <= 0:
            print("Warrior died!")
        return(hp1)
    if random.choice == 1:
        #hp = hp - (wp - ap)
        hp2 = hp2 - (wp1 - ap2)
        if hp2 <= 0:
            print("Priest died!")
        return(hp2)

#ataque do orc 2
def OrcAttack2(hp1, hp2, wp2, ap1, ap2):        
    print("Enemy 2 strikes!")
    print(random.choice(range(0,1)))
    #0 = WarriorClass[0]
    #1 = PriestClass[0]
    if random.choice == 0:
        #hp = hp - (wp - ap)
        hp1 = hp1 - (wp2 - ap1)
        if hp1 <= 0:
            print("Warrior died!")
        return(hp1)
    if random.choice == 1:
        #hp = hp - (wp - ap)
        hp2 = hp2 - (wp2 - ap2)
        if hp2 <= 0:
            print("Priest died!")
        return(hp2)

#ataque do orc 3
def OrcAttack3(hp1, hp2, wp3, ap1, ap2):        
    print("Enemy 3 strikes!")
    print(random.choice(range(0,1)))
    #0 = WarriorClass[0]
    #1 = PriestClass[0]
    if random.choice == 0:
        #hp = hp - (wp - ap)
        hp1 = hp1 - (wp3 - ap1)
        if hp1 <= 0:
            print("Warrior died!")
        return(hp1)
    if random.choice == 1:
        #hp = hp - (wp - ap)
        hp2 = hp2 - (wp3 - ap2)
        if hp2 <= 0:
            print("Priest died!")
        return(hp2)
        

#ciclo principal
while True:
    #atribuir o  valor do novo init a cada classe
    InitFase(ListClass)

    #sort mudar local    
    ListClass.sort(key = lambda CL:CL[6]) #lambda sorts CL[6] inside ListCLass, like for function 
    print(ListClass[0][6], ListClass[0][-1])

    for i in ListClass:
        if i[6] == WarriorClass[6]: 
            warrior = WarriorAttack(OrcClass1[0], OrcClass2[0], OrcClass3[0], WarriorClass[1], WarriorClass[2], WarriorClass[3], WarriorClass[4], WarriorClass[7])
        elif i[6] == PriestClass[6]:
            priest = PriestAttack(PriestClass[0], OrcClass1[0], OrcClass2[0], OrcClass3[0], WarriorClass[0], WarriorClass[1], WarriorClass[2], WarriorClass[3], WarriorClass[4], WarriorClass[7])
        elif i[6] == OrcClass1[6]:
            orc1 = OrcAttack1(WarriorClass[0], PriestClass[0], OrcClass1[4], WarriorClass[3], PriestClass[3])
        elif i[6] == OrcClass2[6]:
            orc2 = OrcAttack2(WarriorClass[0], PriestClass[0], OrcClass2[4], WarriorClass[3], PriestClass[3])
        elif i[6] == OrcClass3[6]:
            orc3 = OrcAttack3(WarriorClass[0], PriestClass[0], OrcClass3[4], WarriorClass[3], PriestClass[3])
        else:
            quit()