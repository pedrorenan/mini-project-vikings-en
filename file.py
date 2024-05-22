from vikingsClasses import Soldier, Viking, Saxon, War
import random

def generate_vikings():
    viking_names = ["Ragnar","Lagertha","Bjorn","Ivar", "Ubbe","Hvitserk","Sigurd","Harald","Halfdan","Floki"]
    return [Viking(random.choice(viking_names), random.randint(50, 100), random.randint(50, 100)) for i in range(1,random.randint(2, 50))]

def generate_saxons():
    return [Saxon(random.randint(50, 100), random.randint(50, 100)) for i in range(1,random.randint(2, 50))]    

def prepare_battle(war):
    vikings = generate_vikings()
    saxons = generate_saxons()
    for viking in vikings:
        war.addViking(viking)
    for saxon in saxons:
        war.addSaxon(saxon)

def battle(war):
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(war.vikingAttack())
        print(war.saxonAttack())
        print(war.showStatus())



war = War()
prepare_battle(war)
battle(war)
