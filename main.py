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
bh = 40 #extra height on top for health total blitting

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 459 + bh  # only to show bottommost layer, for all intents andpurposes, the height is 450 pixels

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
header = pygame.image.load('Images/header.png')
grass = pygame.image.load('Images/Grass tile.png')
ice = pygame.image.load('Images/Ice tile.png')
brick = pygame.image.load('Images/Brick tile.png')
player = pygame.image.load('Images/Player.png')
wall = pygame.image.load('Images/wall.png')
ceiling = pygame.image.load('Images/Ceiling.png')
gel = pygame.image.load('Images/Blob Player.png')
gelF = pygame.image.load('Images/Blob PlayerF.png')
blobert = pygame.image.load('Images/Blobert.png')
enemy = pygame.image.load('Images/Enemy.png')
enemyF = pygame.image.load('Images/EnemyF.png')
player3 = pygame.image.load('Images/Smiley.png')
player3F = pygame.image.load('Images/SmileyF.png')

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
smileRock = pygame.image.load('Weapon Pics/smileRock.png')

bow = pygame.image.load('Weapon Pics/Bow.png')
arrow = pygame.image.load('Weapon Pics/Arrow.png')

sniper = pygame.image.load('Weapon Pics/Sniper.png')
sshot = pygame.image.load('Weapon Pics/sshot.png')

minigun = pygame.image.load('Weapon Pics/Minigun.png')
mine = pygame.image.load('Weapon Pics/Mine.png')
grenade = pygame.image.load('Weapon Pics/grenade.png')

characterName = 'gel'  # blobert, gel or player

# read in plats from arena file
print "Complete!"
print "Generating Arena..."

f = open("arena_1.txt", "r")
plat_strings = []
for i in range(9):  # 9 IS THE LENGTH OF PLAT - NEEDS TO BE CHANGED IF NUMBER OF ROWS CHANGES
    plat_strings.append(f.readline())
plat_strings.remove(plat_strings[0])
for p in range(len(plat_strings)):
    for c in range(len(plat_strings[p])):
        img = None
        if plat_strings[p][c] == "i":
            img = Platform(ice, c * 30, 30 + p * 60 + bh)
        elif plat_strings[p][c] == "g":
            img = Platform(grass, c * 30, 30 + p * 60 + bh)
        elif plat_strings[p][c] == "b":
            img = Platform(brick, c * 30, 30 + p * 60 + bh)
        if img is not None:
            all_plats.add(img)
# adding walls
all_plats.add(Platform(wall, -5, -125 + bh))
all_plats.add(Platform(wall, 600, -125 + bh))
all_plats.add(Platform(ceiling, -100, -100 + bh))

print "Complete!"
print "Setting up Characters and Weapons..."

if characterName == 'blobert':
    Dude = Character(blobert, blobert, 150, 400 + bh, 4, 'Dude')
    Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(blobFist, 999, 999, 5, "blobFist", 1, all_plats)
    Rock = RangeWeapon(blobRock, blobRock, 999, 999, 1, "Rock", "blobRock", 8, 0, 1, 5, all_plats, 'P')
elif characterName == 'gel':
    Dude = Character(gel, gelF, 150, 400 + bh, 4, 'Dude')
    #Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(gelFist, 999, 999, 5, "gelFist", 1, all_plats)
    Rock = RangeWeapon(gelRock, gelRock, 999, 999, 1, "Rock", "gelRock", 8, 0, 1, 5, all_plats, 'P')
elif characterName == 'player':
    Dude = Character(player, player, 150, 400 + bh, 4, 'Dude')
    #Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(stickFist, 999, 999, 5, "stickFist", 1)
    Rock = RangeWeapon(stickRock, stickRock, 999, 999, 1, "Rock", "stickRock", 8, 0, 1, 5, all_plats, 'P')
    
evilRock = RangeWeapon(evilRock, evilRock, 999,999, 1, "Rock", "evilRock", 8, 0, 1, 5, all_plats, 'P')
p3Rock = RangeWeapon(smileRock, smileRock, 999, 999, 1, "Rock", "blobRock", 8, 0, 1, 5, all_plats, 'P')    

Enemy1 = Player2(enemy, enemyF, 450, 400 + bh, 4, 'Vampiric Gel')
Player3 = ThirdPlayer(player3, player3F, 570, 400 + bh, 4, 'Smiley')

Rock.setOwner(Dude)
p3Rock.setOwner(Player3)
evilRock.setOwner(Enemy1)

#Sword = MeleeWeapon(sword, 150, 65, 8, "Sword")
Shuriken = RangeWeapon(shuriken, shuriken, 150, 65 +bh, 1, "Shuriken", "Shuriken", 3, 2, 1, 5, all_plats, 'P')
Dagger = RangeWeapon(dagger, dagger, 450, 65+bh, 5, "Dagger", "Dagger", 15, 1, 1, 5, all_plats, 'P')
Spear = RangeWeapon(spear, spear, 15, 360+bh, 8, "Javelin", "Javelin", 24, 5, 1,4, all_plats, 'P')
HandGun = RangeWeapon(blobFist, stickFist, 570, 120+bh, 2, "HandGun", "Hand", 6, 10, 1, 7, all_plats, 'P')
BowAndArrow = RangeWeapon(bow, arrow, 300, 425+bh, 3, "Bow and Arrow", "Arrow", 9, 3, 1, 6, all_plats, 'P')

Sniper = RangeWeapon(sniper, sshot, 280, 300+bh, 20, "Sniper", "sniper shot", 60, 0, 1, 15, all_plats, 'P')
Mini1 = RangeWeapon(minigun, sshot, 240, 180+bh, 1, "Minigun1", "shot", 3, 8, 2, 8, all_plats, 'P')
#Mini2 = RangeWeapon(minigun, sshot, 360, 180+bh, 1, "Minigun2", "shot", 3, 8, 2, 8, all_plats, 'P')
RPG = RangeWeapon(minigun, dagger, 360, 180+bh, 11, "RPG", "RPG", 65, 4, 1, 6, all_plats, 'E')
Mine = ThrowWeapon(mine, mine, 300, 15+bh, 30, "Mine", "Mine", 100, 5, 1, 4, all_plats, 'P')
Grenade = ExplodeWeapon(grenade, grenade, 40, 425+bh, 10, "Grenade", "Grenade", 30, 0, 1, 4, all_plats, 'E')



print "Complete!"
print "Game Beginning..."

living = 0
for char in all_chars:
    char.setHP(0)
    living += 1


while living >= 2:
    
    if Dude.item == None:
        Rock.setOwner(Dude)
    if Enemy1.item == None:
        evilRock.setOwner(Enemy1)
    if Player3.item == None:
        p3Rock.setOwner(Player3)
    
    #time.sleep(.01)
    screen.blit(background2, (0, 0+bh))
    screen.blit(header, (0,0))
    all_weapons.draw(screen)
    all_plats.draw(screen)
    #all_projs.draw(screen)
    all_chars.draw(screen)
    all_hats.draw(screen)
    all_enemies.draw(screen)
    for char in all_chars:
        char.platformCheck = False
    for e in all_enemies.sprites():
        e.platformCheck = False

    key = pygame.key.get_pressed()
    for e in all_enemies.sprites():
        e.updateSpeed(Dude)
        
    for char in all_chars:
        char.update(key, all_plats)

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
                    w.activate()
    if key[K_j]:
        if Player3.alive:
            for w in all_weapons.sprites():
                if(w.owner == Player3):
                    w.activate()

    for w in all_weapons.sprites():
        for char in all_chars:
            if w.owner == char:
                w.setDirection(w.owner.direction)
            
    if characterName == 'blobert' and Dude.alive:
        Top.updateLocation()

    for w in all_weapons.sprites():
        for c in all_chars.sprites():
            w.contactPlayer(c)
        w.updateLocation()
        w.tickTimer()

    for p in all_plats:
        pygame.sprite.spritecollide(p, all_projs, True)
    for c in all_chars:
        pygame.sprite.spritecollide(c, all_projs, True)
    for e in all_enemies:
        pygame.sprite.spritecollide(e, all_projs, True)


    counter = 0
    for char in all_chars:
        htext = myFont.render(char.name + " Damage:" + str(char.HP) + "%", 1, (255,0,0))
        screen.blit(htext, (10+counter * 215, 8))
        for i in range(char.lives):
            screen.blit(heart, (10+counter * 215 +20*i, 18))
        
        counter += 1

    
    for char in all_chars:
        if char.HP < 0:
            char.setHP(char.HP + 1)
        
    living = Dude.alive + Enemy1.alive + Player3.alive
    
    pygame.display.update()
    pygame.event.pump()
    
if Dude.alive:
    print "Dude Wins!"
    endpic = pygame.image.load('Images/Dude Wins.png')
    
elif Enemy1.alive:
    print "Vampiric Gel Wins!"
    endpic = pygame.image.load('Images/VG Wins.png')
    
elif Player3.alive:
    print "Smiley Wins!"
    endpic = pygame.image.load('Images/SmileWins.png')
    
else:
    print "It was a tie!"
    endpic = pygame.image.load('Images/Tie.png')
    
while True:
    screen.blit(endpic, (0, 0+bh))
    
    key = pygame.key.get_pressed()
    
    
    if key[K_ESCAPE]:
        sys.exit()
        
    pygame.display.update()
    pygame.event.pump()
