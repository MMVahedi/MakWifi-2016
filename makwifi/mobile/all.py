import pygame
import sys
screen=pygame.display.set_mode((640,429))
screen.fill((255,255,255))
base=pygame.image.load("english a.png")
screen.blit(base,(0,0))
pygame.display.update()     
while 1==1:
    
    for event in pygame.event.get():
   
        if event.type==pygame.MOUSEBUTTONDOWN :
            j1,k2= event.pos[0],event.pos[1]
            if 7<=j1<=56 and 21<=k2<=96:
                print "Q",
            if 70<=j1<=121 and 21<=k2<=96 :
                print "W",
            if 135<=j1<=184 and 21<=k2<=96 :
                print "E",
            if 198<=j1<=248 and 21<=k2<=96 :
                print "R",
            if 263<=j1<=311 and 21<=k2<=96 :
                print "T",
            if 326<=j1<=377 and 21<=k2<=96 :
                print "Y",
            if 390<=j1<=441 and 21<=k2<=96 :
                print "U",
            if 452<=j1<=505 and 21<=k2<=96 :
                print "I",
            if 518<=j1<=569 and 21<=k2<=96 :
                print "O",
            if 582<=j1<=632 and 21<=k2<=96 :
                print "P",
            if 38<=j1<=89 and 129<=k2<=205 :
                print "A",
            if 102<=j1<=153 and 129<=k2<=205 :
                print "S",
            if 166<=j1<=217 and 129<=k2<=205 :
                print "D",
            if 230<=j1<=281 and 129<=k2<=205 :
                print "F",
            if 294<=j1<=345 and 129<=k2<=205 :
                print "G",
            if 358<=j1<=409 and 129<=k2<=205 :
                print "H",
            if 422<=j1<=473 and 129<=k2<=205 :
                print "J",
            if 486<=j1<=537 and 129<=k2<=205 :
                print "K",
            if 549<=j1<=601 and 129<=k2<=205 :
                print "L",
            if 102<=j1<=153 and 237<=k2<=312 :
                print "Z",
            if 165<=j1<=217 and 237<=k2<=312 :
                print "X",
            if 229<=j1<=282 and 237<=k2<=312 :
                print "C",
            if 293<=j1<=345 and 237<=k2<=312 :
                print "V",
            if 358<=j1<=409 and 237<=k2<=312 :
                print "B",
            if 422<=j1<=473 and 237<=k2<=312 :
                print "N",
            if 486<=j1<=537 and 237<=k2<=312 :
                print "M",
            if 230<=j1<=473 and 345<=k2<=421 :
                print " ",
            if 486<=j1<=632 and 345<=k2<=422 :
                print chr(13)
                
    pygame.display.update()
