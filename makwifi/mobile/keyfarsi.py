# -*- coding: cp1256 -*-
import pygame
pygame.init()
base=pygame.image.load("persian.png")

pygame.display.set_caption("wifi mouse pro")
screen=pygame.display.set_mode((640,432))
screen.blit(base,(0,0))
pygame.display.update()

while 1==1:
                         for event in pygame.event.get():
                             if event.type==pygame.MOUSEBUTTONDOWN :
                                 j1,k2= event.pos[0],event.pos[1]
                                 if 6<=j1<=53 and 24<=k2<=99:
                                     print ("�"),
                                 if 64<=j1<=111 and 24<=k2<=99:
                                     print("�"),
                                 if 122<=j1<=149 and 24<=k2<=99  :
                                     print("�"),
                                 if 181<=j1<=227 and 24<=k2<=99:
                                     print("�"),
                                 if 238<=j1<=285 and 24<=k2<=99:
                                     print("�"),
                                 if 296<=j1<=343 and 24<=k2<=9:
                                     print("�"),
                                 if 354<=j1<=401 and 24<=k2<=99:
                                     print("�"),
                                 if 412<=j1<=459 and 24<=k2<=99:
                                     print("�"),
                                 if 470<=j1<=517 and 24<=k2<=99:
                                     print("�"),
                                 if 527<=j1<=575 and 24<=k2<=99:
                                     print("�"),
                                 if 586<=j1<=633 and 24<=k2<=99:
                                     print("�"),
                                 if 6<=j1<=53 and 132<=k2<=208:
                                     print("�"),  
                                 if 64<=j1<=111 and 132<=k2<=208:
                                     print("�"),
                                 if 122<=j1<=169 and 132<=k2<=208:
                                     print("�"),
                                 if 180<=j1<=227 and 132<=k2<=208:
                                     print("�"),
                                 if 238<=j1<=285 and 132<=k2<=208:
                                     print("�"),
                                 if 296<=j1<=343 and 132<=k2<=208:
                                     print("�"),
                                 if 354<=j1<=402 and 132<=k2<=208:
                                     print("�"),
                                 if 412<=j1<=460 and 132<=k2<=208:
                                     print("�"),
                                 if 470<=j1<=517 and 132<=k2<=208:
                                     print("�"),
                                 if 528<=j1<=575 and 132<=k2<=208:
                                     print("�"),
                                 if 585<=j1<=636 and 132<=k2<=208:
                                     print("�"),
                                 if 7<=j1<=53 and 240<=k2<=316:
                                     print("�"),
                                 if 64<=j1<=111 and 240<=k2<=316:
                                     print("�"),
                                 if 121<=j1<=169 and 240<=k2<=316 :
                                     print("�"),
                                 if 180<=j1<=228 and 240<=k2<=316 :
                                     print("�"),
                                 if 237<=j1<=286 and 240<=k2<=316 :
                                     print("�"),
                                 if 296<=j1<=344 and 240<=k2<=316 :
                                     print("�"),
                                 if 353<=j1<=402 and 240<=k2<=316 :
                                     print("�"),
                                 if 411<=j1<=460 and 240<=k2<=316:
                                     print("�"),
                                 if 469<=j1<=517 and 240<=k2<=316:
                                     print("�"),
                                 if 88<=j1<=348 and 391<=k2<=423:
                                     print(" "),
                                 if 486<=j1<=633 and 348<=k2<=424:
                                     print "\n",
                                 pygame.display.update() 
