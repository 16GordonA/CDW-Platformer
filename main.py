import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *
from pygame.font import *

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
SCREEN_HEIGHT = 459  # only to show bottommost layer, for all intents andpurposes, the height is 450 pixels

pygame.font.init()
myFont = pygame.font.SysFont("Comic Sans", 18)
all_projs_offscreen = pygame.sprite.Group() #will not be rendered to make game faster

"""
Graphics
"""
size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)

print "Loading Images..."
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
heart = pygame.image.load('Images/Heart.png')

sword = pygame.image.load('Weapon Pics/Sword.png')
dagger = pygame.image.load('Weapon Pics/Dagger.png')
spear = pygame.image.load('Weapon Pics/Spear.png')
shuriken = pygame.image.load('Weapon Pics/Shuriken.png')

blobFist = pygame.image.load('Weapon Pics/blobertFist.png')
gelFist = pygame.image.load('Weapon Pics/Gel Fist.png')
stickFist = pygame.image.load('Weapon Pics/Stick Fist.png')

blobRock = pygame.image.load('Weapon Pics/blobRock.png')
gelRock = pygame.image.load('Weapon Pics/gelRock.png')
stickRock = pygame.image.load('Weapon Pics/stickRock.png')
evilRock = pygame.image.load('Weapon Pics/evilRock.png')

bow = pygame.image.load('Weapon Pics/Bow.png')
arrow = pygame.image.load('Weapon Pics/Arrow.png')

sniper = pygame.image.load('Weapon Pics/Sniper.png')
sshot = pygame.image.load('Weapon Pics/sshot.png')

minigun = pygame.image.load('Weapon Pics/Minigun.png')

characterName = 'gel'  # blobert, gel or player

# read in plats from arena file
print "Complete!"
print "Generating Arena..."

f = open("arena_2.txt", "r")
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

print "Complete!"
print "Setting up Characters and Weapons..."

if characterName == 'blobert':
    Dude = Character(blobert, 150, 400, 4)
    Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(blobFist, 999, 999, 5, "blobFist")
    Rock = RangeWeapon(blobRock, blobRock, 999, 999, 1, "Rock", "blobRock", 8, 0, 1)
elif characterName == 'gel':
    Dude = Character(gel, 150, 400, 4)
    #Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(gelFist, 999, 999, 5, "gelFist")
    Rock = RangeWeapon(gelRock, gelRock, 999, 999, 1, "Rock", "gelRock", 8, 0, 1)
elif characterName == 'player':
    Dude = Character(player, 150, 400, 4)
    #Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(stickFist, 999, 999, 5, "stickFist")
    Rock = RangeWeapon(stickRock, stickRock, 999, 999, 1, "Rock", "stickRock", 8, 0, 1)
    
evilRock1 = RangeWeapon(evilRock, evilRock, 999,999, 1, "Rock", "evilRock", 8, 0, 1)
evilRock2 = RangeWeapon(evilRock, evilRock, 999,999, 1, "Rock", "evilRock1", 8, 0, 1)
    

Enemy1 = Enemy(enemy, 450, 400, 1, "enemy1")
Enemy2 = Enemy(enemy, 150, 200, 1, "enemy2")
Rock.setOwner(Dude)
evilRock1.setOwner(Enemy1)
evilRock2.setOwner(Enemy2)

#Sword = MeleeWeapon(sword, 150, 65, 8, "Sword")
Shuriken = RangeWeapon(shuriken, shuriken, 150, 65, 1, "Shuriken", "Shuriken", 3, 2, 1)
Dagger = RangeWeapon(dagger, dagger, 450, 65, 5, "Dagger", "Dagger", 15, 1, 1)
Spear = RangeWeapon(spear, spear, 15, 360, 8, "Javelin", "Javelin", 24, 5, 1)
HandGun = RangeWeapon(blobFist, stickFist, 570, 120, 2, "HandGun", "Hand", 6, 10, 1)
BowAndArrow = RangeWeapon(bow, arrow, 300, 425, 3, "Bow and Arrow", "Arrow", 9, 3, 1)

Sniper = RangeWeapon(sniper, sshot, 280, 300, 20, "Sniper", "sniper shot", 60, 0, 1)
Mini1 = RangeWeapon(minigun, sshot, 240, 180, 1, "Minigun1", "shot", 3, 8, 2)
Mini2 = RangeWeapon(minigun, sshot, 360, 180, 1, "Minigun2", "shot", 3, 8, 2)


print "Complete!"
print "Game Beginning..."

Dude.setHP(150)
Enemy1.setHP(150)

while Dude.alive and (Enemy1.alive or Enemy2.alive):
    
    if Dude.item == None:
        Rock.setOwner(Dude)
    if Enemy1.item == None:
        evilRock1.setOwner(Enemy1)
    if Enemy2.item == None:
        evilRock2.setOwner(Enemy2)
    
    #time.sleep(.01)
    screen.blit(background2, (0, 0))
    all_weapons.draw(screen)
    all_plats.draw(screen)
    #all_projs.draw(screen)
    all_chars.draw(screen)
    all_hats.draw(screen)
    all_enemies.draw(screen)
    Dude.platformCheck = False
    for e in all_enemies.sprites():
        e.platformCheck = False

    key = pygame.key.get_pressed()
    for e in all_enemies.sprites():
        e.updateSpeed(Dude, 1) #change the number for difficulty level (from 0 to 10)
    Dude.update(key, all_plats)
    Enemy1.update(key, all_plats)
    Enemy2.update(key, all_plats)
    #Enemy1.updateSpeed(Dude, )

    if key[K_ESCAPE]:
        sys.exit()

    if key[K_DOWN]:
        if Dude.alive:
            for w in all_weapons.sprites():
                if(w.owner == Dude):
                    w.activate()
    
    if key[K_s]:
        if Enemy1.alive:
            for w in all_weapons.sprites():
                if(w.owner == Enemy1):
                    print w.cooldown
                    w.activate()
                    print w.cooldown
    
    if key[K_l]:
        Rock.setOwner(Dude)
    
    if key[K_v]:
        evilRock.setOwner(Enemy1)

    for w in all_weapons.sprites():
        if(w.owner == Dude):
            w.setDirection(Dude.direction)
        if(w.owner == Enemy1):
            w.setDirection(Enemy1.direction)
            
    if characterName == 'blobert' and Dude.alive:
        Top.updateLocation()

    for w in all_weapons.sprites():
        for c in all_chars.sprites():
            w.contactPlayer(c)
        for e in all_enemies.sprites():
            if w.contactPlayer(e):
                w.setOwner(e)
        w.updateLocation()
        w.tickTimer()

    for p in all_plats:
        pygame.sprite.spritecollide(p, all_projs, True)
    for c in all_chars:
        pygame.sprite.spritecollide(c, all_projs, True)
    for e in all_enemies:
        pygame.sprite.spritecollide(e, all_projs, True)

    P1health = myFont.render("Dude Health: "+str(Dude.HP) + "%", 1,(255,0,0))
    screen.blit(P1health, (10, 10))
    
    for i in range(Dude.lives):
        screen.blit(heart, (10 + 20 * i, 18))
    
    count = 0
    
    for e in all_enemies:
        E1health = myFont.render("Vampiric Gel Health: " + str(e.HP) + "%", 1, (255, 0 ,0))
        screen.blit(E1health, (425, 10 + 40 * count))
        for i in range(e.lives):
            screen.blit(heart, (560 - 20 * i, 18 + 40*count))
        count += 1
    
    if Dude.HP > 100:
        Dude.setHP(Dude.HP - 1)
    for e in all_enemies:
        if e.HP > 100:
            e.setHP(e.HP - 1)
    
    pygame.display.update()
    pygame.event.pump()
    
if Dude.alive:
    print "Dude Wins!"
    endpic = pygame.image.load('Images/Dude Wins.png')
    
elif Enemy1.alive or Enemy2.alive:
    print "Vampiric Gels Win!"
    endpic = pygame.image.load('Images/VG Wins.png')
    
else:
    print "It was a tie!"
    endpic = pygame.image.load('Images/Tie.png')
    
while True:
    screen.blit(endpic, (0, 0))
    
    key = pygame.key.get_pressed()
    
    
    if key[K_ESCAPE]:
        sys.exit()
        
    pygame.display.update()
    pygame.event.pump()
