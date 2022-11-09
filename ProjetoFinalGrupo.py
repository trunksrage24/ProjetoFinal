#trabalho grupo computaçao - Vitor Daniel e Tiago Castro

#import da bibliotecas a ser usadas
import random
from operator import itemgetter

#Characters stats = hp, mp, mc(mana cost), ap, wp, Init, UpdateInit, sp(spell power)
WarriorClass = [32, 5, 0, 0, 2, 5, 2, 0]
PriestClass = [20, 25, 0, 0, 0, 2, 6, 0]
OrcClass = [15, 0, 0, 2, 2, 2, 0]

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

# listas dentro de lista
def sortList(turnOrder):
    ListClass = [WarriorClass, PriestClass, OrcClass]
    print("Sorted ListClass based on index 0: % s" % (sorted(ListClass, key=itemgetter(0))))

