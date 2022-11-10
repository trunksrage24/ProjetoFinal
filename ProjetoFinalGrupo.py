#trabalho grupo computaçao - Vitor Daniel e Tiago Castro

#import da bibliotecas a ser usadas
import random

#Characters stats = hp, mp, mc(mana cost), ap, wp, Init, UpdateInit, sp(spell power)
WarriorClass = [32, 5, 0, 2, 5, 2, 0, 0]
PriestClass = [20, 25, 0, 0, 2, 6, 0, 0]
OrcClass = [15, 0, 0, 2, 2, 2, 0]
ListClass = [WarriorClass, PriestClass, OrcClass]
#fases iniciantes:

#def dados:
def DiceRoll(d):
    return random.randint(1, d)

#fase iniciante: definir tipos
def ClassInit(ClassType):
    if ClassType == "Warrior":
        return WarriorClass.copy()
    elif ClassType == "Priest":
        return PriestClass.copy()
    elif ClassType == "Orc":
        return OrcClass.copy()
    else:
        return []    

#fase iniciante:dice roll
def RollInit(character):
    Init = DiceRoll(20) + character[5]
    character[6] = Init
    
#fase iniciante: sort
def InitFase (ListOfCharacter):
    for character in ListOfCharacter:
        RollInit(character)

# listas dentro de lista
def Init_Updated(IU):
    return IU[6]
#sort mudar local
ListClass.sort(key = Init_Updated)

#fases atacantes:
#ataque do warrior

def WarriorAttack(hp, wp, mp, mc, ap, sp):
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
                mp = mp - mc
                hp = hp - (sp-ap)
            elif Target == 2:
                print("You casted Rushdown on the enemy")
                mp = mp - mc
                hp = hp - (sp-ap)
    elif Action ==2:
         Target = input("Choose target:")
         print("You struck the enemy")
         hp = hp - (wp - ap)
    return(hp,mp)

#ataque do priest
def PriestAttack(hp, wp, mp, mc, ap, sp):
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
                print("You healed yourself")
                mp = mp - mc
                hp = hp + sp
            elif Target == 2:
                print("You healed yourself")
                mp = mp - mc
                hp = hp + sp
        elif Spell == 2:
            Target = input("Choose target:")
            if Target == 1:
                print("You casted Exorcism")
                hp = hp - (sp - ap)
                mp = mp - mc
            elif Target == 2:
                print("You casted Exorcism")
                hp = hp - (sp - ap)
                mp = mp - mc
    elif Action ==2:
         Target = input("Choose target:")
         print("You struck the enemy")
         hp = hp - (wp - ap)
    return(hp,mp)

#ataque do orc
def OrcTurn(hp, wp, mp, ap):
            print("The enemy strikes!")
            print(random.choice(range("Priest", "Warrior")))
            hp = hp - (wp - ap)
            return(hp)  