import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *

from Platform import *
from Character import *
from Hat import *
from Weapon import *
from Enemy import *

'''
main.py
Creates the outermost frame for the world
'''

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 459  # only to show bottommost layer, for all intensive purposes, the height is 450 pixels

"""
Graphics
"""
size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)
background = pygame.image.load('Images/background.png')
background2 = pygame.image.load('Images/night.png')
grass = pygame.image.load('Images/Grass tile.png')
ice = pygame.image.load('Images/Ice tile.png')
brick = pygame.image.load('Images/Brick tile.png')
player = pygame.image.load('Images/Player.png')
wall = pygame.image.load('Images/wall.png')
ceiling = pygame.image.load('Images/Ceiling.png')
gel = pygame.image.load('Images/Blob Player.png')
blobert = pygame.image.load('Images/Blobert.png')
enemy = pygame.image.load('Images/Enemy.png')

tophat = pygame.image.load('Images/topHat.png')

sword = pygame.image.load('Weapon Pics/Sword.png')
dagger = pygame.image.load('Weapon Pics/Dagger.png')
spear = pygame.image.load('Weapon Pics/Spear.png')

blobFist = pygame.image.load('Weapon Pics/blobertFist.png')
gelFist = pygame.image.load('Weapon Pics/Gel Fist.png')
stickFist = pygame.image.load('Weapon Pics/Stick Fist.png')

bow = pygame.image.load('Weapon Pics/Bow.png')
arrow = pygame.image.load('Weapon Pics/Arrow.png')

characterName = 'blobert'  # blobert, gel or player

# read in plats from arena file
f = open("arena_1.txt", "r")
plat_strings = []
for i in range(9):  # 9 IS THE LENGTH OF PLAT - NEEDS TO BE CHANGED IF NUMBER OF ROWS CHANGES
    plat_strings.append(f.readline())
plat_strings.remove(plat_strings[0])
for p in range(len(plat_strings)):
    for c in range(len(plat_strings[p])):
        img = None
        if plat_strings[p][c] == "i":
            img = Platform(ice, c * 30, 30 + p * 60)
        elif plat_strings[p][c] == "g":
            img = Platform(grass, c * 30, 30 + p * 60)
        elif plat_strings[p][c] == "b":
            img = Platform(brick, c * 30, 30 + p * 60)
        if img is not None:
            all_plats.add(img)
# adding walls
all_plats.add(Platform(wall, -5, -125))
all_plats.add(Platform(wall, 600, -125))
all_plats.add(Platform(ceiling, -100, -100))

if characterName == 'blobert':
    Dude = Character(blobert, 300, 400)
    Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(blobFist, 300, 425, 5, "blobFist")
elif characterName == 'gel':
    Dude = Character(gel, 300, 400)
    #Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(gelFist, 300, 425, 5, "gelFist")
elif characterName == 'player':
    Dude = Character(player, 300, 400)
    #Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(stickFist, 300, 425, 5, "stickFist")
    
Enemy1 = Enemy(enemy, 285, 60, "vampire")
    
Fist.setOwner(Dude)

Sword = MeleeWeapon(sword, 150, 65, 8, "Sword")
Dagger = MeleeWeapon(dagger, 450, 65, 10, "Dagger")
Spear = MeleeWeapon(spear, 15, 210, 5, "Spear")
HandGun = RangeWeapon(blobFist, stickFist, 570, 60, 2, "HandGun", "Hand", 5)
BowAndArrow = RangeWeapon(bow, arrow, 15, 425, 3, "Bow and Arrow", "Arrow", 1)

while True:
    time.sleep(.01)
    screen.blit(background2, (0, 0))
    all_weapons.draw(screen)
    all_plats.draw(screen)
    all_projs.draw(screen)
    all_chars.draw(screen)
    all_hats.draw(screen)
    all_enemies.draw(screen)
    Dude.platformCheck = False
    for e in all_enemies.sprites():
        e.platformCheck = False

    key = pygame.key.get_pressed()
    for e in all_enemies.sprites():
        e.updateSpeed(Dude)
    Dude.update(key, all_plats)

    if key[K_ESCAPE]:
        sys.exit()

    if key[K_SPACE]:
        for w in all_weapons.sprites():
            w.activate()
    
    if key[K_h]:
        print Enemy1.HP

    for p in all_plats:
        for e in all_enemies.sprites():
            e.checkCollision(p)
            e.platformCheck = False
            e.checkOnPlatform(p)
            if e.platformCheck:
                e.land = True

    Dude.update(key, all_plats)
    for w in all_weapons.sprites():
        if(w.owner == Dude):
            w.setDirection(Dude.direction)
    if characterName == 'blobert':
        Top.updateLocation()

    for w in all_weapons.sprites():
        w.contactPlayer(Dude)
        for e in all_enemies.sprites():
            w.contactPlayer(e)
        w.updateLocation()
        w.tickTimer()

    for p in all_plats:
        pygame.sprite.spritecollide(p, all_projs, True)
    for c in all_chars:
        pygame.sprite.spritecollide(c, all_projs, True)
    for e in all_enemies:
        pygame.sprite.spritecollide(e, all_projs, True)

    pygame.display.update()
    pygame.event.pump()
