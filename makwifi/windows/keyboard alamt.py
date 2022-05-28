import pygame
import sys
screen=pygame.display.set_mode((640,429))
screen.fill((255,255,255))
base=pygame.image.load("photo_2014-09-20_10-11-57.jpg")
base=pygame.transform.smoothscale(base,(640,429))
screen.blit(base,(0,0))
pygame.display.update()     
while 1==1:
    
    for event in pygame.event.get():
   
        if event.type==pygame.MOUSEBUTTONDOWN :
            j1,k2= event.pos[0],event.pos[1]
            if 7<=j1<=56 and 21<=k2<=96:
                print "1",
            if 70<=j1<=121 and 21<=k2<=96 :
                print "2",
            if 135<=j1<=184 and 21<=k2<=96 :
                print "3",
            if 198<=j1<=248 and 21<=k2<=96 :
                print "4",
            if 263<=j1<=311 and 21<=k2<=96 :
                print "5",
            if 326<=j1<=377 and 21<=k2<=96 :
                print "6",
            if 390<=j1<=441 and 21<=k2<=96 :
                print "7",
            if 452<=j1<=505 and 21<=k2<=96 :
                print "8",
            if 518<=j1<=569 and 21<=k2<=96 :
                print "9",
            if 582<=j1<=632 and 21<=k2<=96 :
                print "0",
            if 7<=j1<=56 and 129<=k2<=216:
                print "-",
            if 70<=j1<=121 and 129<=k2<=216 :
                print "/",
            if 135<=j1<=184 and 129<=k2<=216 :
                print ":",
            if 198<=j1<=248 and 129<=k2<=216 :
                print ";",
            if 263<=j1<=311 and 129<=k2<=216 :
                print "(",
            if 326<=j1<=377 and 129<=k2<=216 :
                print ")",
            if 390<=j1<=441 and 129<=k2<=216 :
                print "$",
            if 452<=j1<=505 and 129<=k2<=216 :
                print "&",
            if 518<=j1<=569 and 129<=k2<=216 :
                print "@",
            if 582<=j1<=632 and 129<=k2<=216 :
                print "''",
            if 101<=j1<=180 and 239<=k2<=315 :
                print ".",
            if 191<=j1<=269 and 239<=k2<=315 :
                print ",",
            if 278<=j1<=359 and 239<=k2<=315 :
                print "?",
            if 370<=j1<=450 and 239<=k2<=315 :
                print "!",
            if 422<=j1<=473 and 239<=k2<=315 :
                print "back",
            if 486<=j1<=634 and 347<=k2<423 :
                print "\n" ,
            if 86<=j1<=472 and 346<=k2<=423 :
                print " ",
            if 462<=j1<=540 and 239<=k2<=315 :
                print "'",
                
    pygame.display.update()
