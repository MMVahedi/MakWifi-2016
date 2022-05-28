# -*- coding: cp1256 -*-
class makwifi1:
        from easygui import enterbox
        global makwifi
        def menu (self):
              from easygui import enterbox , ynbox
              import pygame
              a=0
              x=0
              global screen
              #1138 388
              pygame.init()
              pygame.display.set_caption("wifi mouse pro")
              screen=pygame.display.set_mode((380,554))
              screen.fill((16,18,33))
              base=pygame.image.load("b.png")
              base1=pygame.image.load("408899.jpg")
              base2=pygame.image.load("408899 - Copy (1).jpg")
              base3=pygame.image.load("Untitled-2.jpg")
              base7=pygame.image.load("1.jpg")
              screen.blit(base,(0,0))
              pygame.display.update()
              k=0
              p=0
              c=0
              while 1==1:
                  for event in pygame.event.get():
                      if event.type==pygame.MOUSEBUTTONDOWN :
                          j,k= event.pos[0],event.pos[1]
                          if 87<=j<=295 and 279<=k<=325 and p==0:
                              global result
                              global result2
                              result =enterbox("Enter server IP,please like this 122.133.144.155","server IP")
                              result2 =enterbox("Enter server port","port")
                              p=1
                              makwifi.keyboard()
                          if 87<=j<=295 and 422<=k<=467 and p==0 :
                                   global result
                                   global result2
                                   result =enterbox("Enter server IP,please like this 122.133.144.155","server IP")
                                   result2 =enterbox("Enter server port","port")
                                   makwifi.mouse()
                                   p=1
                          if 87<=j<=295 and 352<=k<=397 and p==0 :
                                   global result
                                   global result2
                                   result =enterbox("Enter server IP,please like this 122.133.144.155","server IP")
                                   result2 =enterbox("Enter server port","port")
                                   makwifi.keyapple()
                                   p=1
                          if 87<=j<=295 and 492<=k<=537 and p==0:
                              global result
                              global result2
                              result =enterbox("Enter server IP,please like this 122.133.144.155","server IP")
                              result2 =enterbox("Enter server port","port")
                              p=1
                              makwifi.girande()
        def keyboard (self):
          #in defe keyboardandroidengelisi ast
          # _*_ coding: utf8 _*_
          k10=[]
          from easygui import enterbox , ynbox
          global makwifi
          import pygame
          import sys
          pygame.init()
          base=pygame.image.load("Untitled-2.jpg")
          screen=pygame.display.set_mode((1150,400))
          screen.blit(base,(0,0))
          pygame.display.update()
          while 1==1:
                         for event in pygame.event.get():
                             if event.type==pygame.MOUSEBUTTONDOWN :
                                 j1,k2= event.pos[0],event.pos[1]
                                 if 12<=j1<=119 and 317<=k2<=386:
                                     makwifi.keyandroidalamat()
                                 if 138<=j1<=247 and 321<=k2<=387:
                                     makwifi.keyandroidfarsi1()
                                 if 12<=j1<=95 and 70<=k2<=140:
                                     makwifi.network("q")
                                 if 115<=j1<=195 and 70<=k2<=140:
                                     makwifi.network("w")
                                 if 215<=j1<=298 and 70<=k2<=140:
                                     makwifi.network("e")
                                 if 317<=j1<=400 and 70<=k2<=140:
                                     makwifi.network("r")
                                 if 420<=j1<=500 and 70<=k2<=140:
                                     makwifi.network("t")
                                 if 520<=j1<=603 and 70<=k2<=140:
                                     makwifi.network("y")
                                 if 622<=j1<=704 and 70<=k2<=140:
                                     makwifi.network("u")
                                 if 723<=j1<=806 and 70<=k2<=140:
                                     makwifi.network("i")
                                 if 825<=j1<=908 and 70<=k2<=140:
                                     makwifi.network("o")
                                 if 927<=j1<=1009 and 70<=k2<=140:
                                     makwifi.network("p")
                                 if 59<=j1<=142 and 152<=k2<=223:
                                     makwifi.network("a")
                                 if 160<=j1<=243 and 152<=k2<=223:
                                     makwifi.network("s")
                                 if 262<=j1<=345 and 152<=k2<=223:
                                     makwifi.network("s")  
                                 if 364<=j1<=446 and 152<=k2<=223:
                                     makwifi.network("f")
                                 if 465<=j1<=548 and 152<=k2<=223:
                                     makwifi.network("g")
                                 if 567<=j1<=650 and 152<=k2<=223:
                                     makwifi.network("h")
                                 if 669<=j1<=751 and 152<=k2<=223:
                                     makwifi.network("j")
                                 if 770<=j1<=853 and 152<=k2<=223:
                                     makwifi.network("k")
                                 if 872<=j1<=954 and 152<=k2<=223:
                                     makwifi.network("l")
                                 if 114<=j1<=196 and 234<=k2<=305:
                                     makwifi.network("z")
                                 if 215<=j1<=298 and 234<=k2<=305:
                                     makwifi.network("x")
                                 if 317<=j1<=399 and 234<=k2<=305:
                                     makwifi.network("c")
                                 if 419<=j1<=501 and 234<=k2<=305:
                                     makwifi.network("v")
                                 if 520<=j1<=602 and 234<=k2<=305:
                                     makwifi.network("b")
                                 if 622<=j1<=704 and 234<=k2<=305:
                                     makwifi.network("n")
                                 if 723<=j1<=806 and 234<=k2<=305:
                                     makwifi.network("m")
                                 if 826<=j1<=908 and 234<=k2<=305:
                                     makwifi.network(",")
                                 if 927<=j1<=1009 and 234<=k2<=305:
                                     makwifi.network(".")
                                 if 267<=j1<=880 and 316<=k2<=387:
                                     makwifi.network(" ")
                                 if 973<=j1<=1138 and 152<=k2<=223:
                                     makwifi.network("\n")
                                 if 900<=j1<=1009 and 317<=k2<=387:
                                     makwifi.menu()
                                 if 12<=j1<=107 and 8<=k2<=59:
                                     makwifi.network("1")
                                 if 125<=j1<=225 and 8<=k2<=59:
                                     makwifi.network("2")
                                 if 240<=j1<=336 and 8<=k2<=59:
                                     makwifi.network("3")
                                 if 355<=j1<=450 and 8<=k2<=59:
                                         makwifi.network("4")
                                 if 468<=j1<=565 and 8<=k2<=59:
                                     makwifi.network("5")
                                 if 585<=j1<=680 and 8<=k2<=59:
                                     makwifi.network("6")
                                 if 700<=j1<=795 and 8<=k2<=59:
                                     makwifi.network("7")
                                 if 815<=j1<=910 and 8<=k2<=59:
                                     makwifi.network("8")
                                 if 930<=j1<=1025 and 8<=k2<=59:
                                     makwifi.network("9")
                                 if 1045<=j1<=1140 and 8<=k2<=59:
                                     makwifi.network("0")
                                 if  1028<=j1<=1138 and 316<=k2<=387:
                                        makwifi.mouse()
                                 if (12<=j1<=95 and 234<=k2<=305) or (1028<=j1<=1138 and 234<=k2<=305):
                                             makwifi.keyandroidcaptalengelisi()
                                 pygame.display.update()
                                 
        def keyandroidcaptalengelisi(self):
                  # _*_ coding: utf8 _*_
                  from easygui import enterbox , ynbox
                  global makwifi
                  import pygame
                  import sys
                  pygame.init()
                  base=pygame.image.load("english1.jpg")
                  screen=pygame.display.set_mode((1150,400))
                  screen.blit(base,(0,0))
                  pygame.display.update()
                  while 1==1:
                                 for event in pygame.event.get():
                                     if event.type==pygame.MOUSEBUTTONDOWN :
                                         j1,k2= event.pos[0],event.pos[1]
                                         if 12<=j1<=107 and 8<=k2<=59 :
                                             makwifi.network("1")
                                         if 125<=j1<=225 and 8<=k2<=59  :
                                             makwifi.network("2")
                                         if 240<=j1<=336 and 8<=k2<=59 :
                                             makwifi.network("3")
                                         if 355<=j1<=450 and 8<=k2<=59 :
                                                 makwifi.network("4")
                                         if 468<=j1<=565 and 8<=k2<=59  :
                                             makwifi.network("5")
                                         if 585<=j1<=680 and 8<=k2<=59  :
                                             makwifi.network("6")
                                         if 700<=j1<=795 and 8<=k2<=59  :
                                             makwifi.network("7")
                                         if 815<=j1<=910 and 8<=k2<=59 :
                                             makwifi.network("8")
                                         if 930<=j1<=1025 and 8<=k2<=59 :
                                             makwifi.network("9")
                                         if 1045<=j1<=1140 and 8<=k2<=59 :
                                             makwifi.network("0")
                                         if 12<=j1<=95 and 70<=k2<=140:
                                             makwifi.network("Q")
                                         if 115<=j1<=195 and 70<=k2<=140:
                                             makwifi.network("W")
                                         if 215<=j1<=298 and 70<=k2<=140:
                                             makwifi.network("E")
                                         if 317<=j1<=400 and 70<=k2<=140:
                                             makwifi.network("R")
                                         if 420<=j1<=500 and 70<=k2<=140:
                                             makwifi.network("T")
                                         if 520<=j1<=603 and 70<=k2<=140:
                                             makwifi.network("Y")
                                         if 622<=j1<=704 and 70<=k2<=140:
                                             makwifi.network("U")
                                         if 723<=j1<=806 and 70<=k2<=140:
                                             makwifi.network("I")
                                         if 825<=j1<=908 and 70<=k2<=140:
                                             makwifi.network("O")
                                         if 927<=j1<=1009 and 70<=k2<=140:
                                             makwifi.network("P")
                                         if 59<=j1<=142 and 152<=k2<=223:
                                             makwifi.network("A")
                                         if 160<=j1<=243 and 152<=k2<=223:
                                             makwifi.network("S")
                                         if 262<=j1<=345 and 152<=k2<=223:
                                             makwifi.network("D")
                                         if 364<=j1<=446 and 152<=k2<=223:
                                             makwifi.network("F")
                                         if 465<=j1<=548 and 152<=k2<=223:
                                             makwifi.network("G")
                                         if 567<=j1<=650 and 152<=k2<=223:
                                             makwifi.network("H")
                                         if 669<=j1<=751 and 152<=k2<=223:
                                             makwifi.network("J")
                                         if 770<=j1<=853 and 152<=k2<=223:
                                             makwifi.network("K")
                                         if 872<=j1<=954 and 152<=k2<=223:
                                             makwifi.network("L")
                                         if 114<=j1<=196 and 234<=k2<=305:
                                             makwifi.network("Z")
                                         if 215<=j1<=298 and 234<=k2<=305:
                                             makwifi.network("X")
                                         if 317<=j1<=399 and 234<=k2<=305:
                                             makwifi.network("C")
                                         if 419<=j1<=501 and 234<=k2<=305:
                                             makwifi.network("V")
                                         if 520<=j1<=602 and 234<=k2<=305:
                                             makwifi.network("B")
                                         if 622<=j1<=704 and 234<=k2<=305:
                                             makwifi.network("N")
                                         if 723<=j1<=806 and 234<=k2<=305:
                                             makwifi.network("M")
                                         if 826<=j1<=908 and 234<=k2<=305:
                                             makwifi.network("!")
                                         if 927<=j1<=1009 and 234<=k2<=305:
                                             makwifi.network("?")
                                         if 267<=j1<=880 and 316<=k2<=387:
                                             makwifi.network(" ")
                                         if 973<=j1<=1138 and 152<=k2<=223:
                                             makwifi.network("\n")
                                         if (12<=j1<=95 and 234<=k2<=305) or (1028<=j1<=1138 and 234<=k2<=305):
                                             makwifi.keyboard()
                                         if 900<=j1<=1009 and 317<=k2<=387 :
                                             makwifi.menu()
                                         if  1028<=j1<=1138 and 316<=k2<=387:
                                                makwifi.mouse()
                                         if 12<=j1<=119 and 317<=k2<=386:
                                             makwifi.keyandroidalamat()
                                         if 138<=j1<=247 and 321<=k2<=387:
                                             makwifi.keyandroidfarsi1()
                                         pygame.display.update()
        def keyandroidfarsi1(self):
                  # _*_ coding: utf8 _*_
                  k10=[]
                  from easygui import enterbox , ynbox
                  global makwifi
                  import pygame
                  import sys
                  pygame.init()
                  base=pygame.image.load("persian2.jpg")
                  screen=pygame.display.set_mode((1150,400))
                  screen.blit(base,(0,0))
                  pygame.display.update()
                  while 1==1:
                                 for event in pygame.event.get():
                                     if event.type==pygame.MOUSEBUTTONDOWN :
                                         j1,k2= event.pos[0],event.pos[1]
                                         if 12<=j1<=107 and 8<=k2<=59 :
                                             makwifi.network("1")
                                         if 125<=j1<=225 and 8<=k2<=59  :
                                             makwifi.network("2")
                                         if 240<=j1<=336 and 8<=k2<=59 :
                                             makwifi.network("3")
                                         if 355<=j1<=450 and 8<=k2<=59 :
                                             makwifi.network("4")
                                         if 468<=j1<=565 and 8<=k2<=59  :
                                             makwifi.network("5")
                                         if 585<=j1<=680 and 8<=k2<=59  :
                                             makwifi.network("6")
                                         if 700<=j1<=795 and 8<=k2<=59  :
                                             makwifi.network("7")
                                         if 815<=j1<=910 and 8<=k2<=59 :
                                             makwifi.network("8")
                                         if 930<=j1<=1025 and 8<=k2<=59 :
                                             makwifi.network("9")
                                         if 1045<=j1<=1140 and 8<=k2<=59 :
                                             makwifi.network("0")
                                         if 12<=j1<=95 and 70<=k2<=141:
                                                makwifi.network( ".w")
                                         if 114<=j1<=196 and 70<=k2<=141:
                                                makwifi.network( ".e")
                                         if 215<=j1<=298 and 70<=k2<=141:
                                                makwifi.network( ".r")
                                         if 317<=j1<=399 and 70<=k2<=141:
                                                makwifi.network( ".t")
                                         if 419<=j1<=501 and 70<=k2<=141:
                                                makwifi.network(".u")
                                         if 520<=j1<=603 and 70<=k2<=141:
                                                makwifi.network( ".i")
                                         if 623<=j1<=704 and 70<=k2<=141:
                                                makwifi.network( ".o")
                                         if 723<=j1<=806 and 70<=k2<=141:
                                                makwifi.network( ".p")
                                         if 825<=j1<=909 and 70<=k2<=141:
                                                makwifi.network( ".6")
                                                #.6=jim
                                         if 927<=j1<=1010 and 70<=k2<=141:
                                                makwifi.network( ".5")
                                                #.5=che
                                         if 12<=j1<=95 and 152<=k2<=223:
                                                makwifi.network( ".a")
                                         if 114<=j1<=196 and 152<=k2<=223:
                                                makwifi.network( ".s")
                                         if 215<=j1<=298 and 152<=k2<=223:
                                                makwifi.network( ".d")
                                         if 317<=j1<=399 and 152<=k2<=223:
                                                makwifi.network( ".f")
                                         if 419<=j1<=501 and 152<=k2<=223:
                                                makwifi.network( ".g")
                                         if 520<=j1<=603 and 152<=k2<=223:
                                                makwifi.network( ".h")
                                         if 623<=j1<=704 and 152<=k2<=223:
                                                makwifi.network( ".j")
                                         if 723<=j1<=806 and 152<=k2<=223:
                                                makwifi.network( ".k")
                                         if 825<=j1<=909 and 152<=k2<=223:
                                                makwifi.network( ".l")
                                         if 927<=j1<=1010 and 152<=k2<=223:
                                                makwifi.network( ".3")
                                                #.3=pe
                                         if 114<=j1<=196 and 223<=k2<=305:
                                                makwifi.network( ".x")
                                         if 215<=j1<=297 and 223<=k2<=305:
                                                makwifi.network( ".c")
                                         if 317<=j1<=399 and 223<=k2<=305:
                                                makwifi.network( ".v")
                                         if 419<=j1<=501 and 223<=k2<=305:
                                                makwifi.network( ".n")
                                         if 520<=j1<=602 and 223<=k2<=305:
                                                makwifi.network(".2")
                                                #.2=ve
                                         if 622<=j1<=704 and 223<=k2<=305:
                                                makwifi.network( ".1")
                                                #.1=ke
                                         if 724<=j1<=805 and 223<=k2<=305:
                                                makwifi.network( ".0")
                                         if 267<=j1<=880 and 316<=k2<=387:
                                             makwifi.network(" ")
                                         if 973<=j1<=1138 and 152<=k2<=223:
                                             makwifi.network("\n")
                                         if 826<=j1<=908 and 234<=k2<=305:
                                             makwifi.network(",")
                                         if 927<=j1<=1009 and 234<=k2<=305:
                                             makwifi.network(".")
                                         if 900<=j1<=1009 and 317<=k2<=387:
                                             makwifi.menu()
                                         if  1028<=j1<=1138 and 316<=k2<=387:
                                                makwifi.mouse()
                                         if 12<=j1<=119 and 317<=k2<=386:
                                             makwifi.keyandroidalamat()
                                         if 138<=j1<=247 and 321<=k2<=387:
                                             makwifi.keyboard()
                                         pygame.display.update()
        def keyapple(self):
                import pygame
                pygame.init()
                base=pygame.image.load("english .png")
                pygame.display.set_caption("wifi mouse pro")
                screen=pygame.display.set_mode((640,430))
                screen.blit(base,(0,0))
                pygame.display.update()
                while 1==1:
                                         for event in pygame.event.get():
                                             if event.type==pygame.MOUSEBUTTONDOWN :
                                                 j1,k2= event.pos[0],event.pos[1]
                                                 if 8<=j1<=57 and 21<=k2<=97:
                                                     makwifi.network("q"),
                                                 #if 12<=j1<=119 and 317<=k2<=386:
                                                     makwifi.network("q"),
                                                 ##if 8<=j1<=57 and 21<=k2<=97:
                                                     makwifi.network("q"),
                                                 #if 8<=j1<=57 and 21<=k2<=97:
                                                     makwifi.network("q"),
                                                 #if 8<=j1<=57 and 21<=k2<=97:
                                                     makwifi.network("q"),
                                                 if 70<=j1<=121 and 21<=k2<=97:
                                                     makwifi.network("w"),
                                                 if 134<=j1<=186 and 21<=k2<=97:
                                                     makwifi.network("e"),
                                                 if 199<=j1<=255 and 21<=k2<=97:
                                                     makwifi.network("r"),
                                                 if 262<=j1<=313 and 21<=k2<=97:
                                                     makwifi.network("t"),
                                                 if 325<=j1<=377 and 21<=k2<=97:
                                                     makwifi.network("y"),
                                                 if 390<=j1<=441 and 21<=k2<=97:
                                                     makwifi.network("u"),
                                                 if 453<=j1<=505 and 21<=k2<=97:
                                                     makwifi.network("i"),
                                                 if 517<=j1<=569 and 21<=k2<=97:
                                                     makwifi.network("o"),
                                                 if 582<=j1<=633 and 21<=k2<=97:
                                                     makwifi.network("p"),
                                                 if 38<=j1<=90 and 130<=k2<=205:
                                                     makwifi.network("a"),
                                                 if 102<=j1<=153 and 130<=k2<=205:
                                                     makwifi.network("s"),
                                                 if 166<=j1<=217 and 130<=k2<=205:
                                                     makwifi.network("d"),  
                                                 if 230<=j1<=282 and 130<=k2<=205:
                                                     makwifi.network("f"),
                                                 if 294<=j1<=346 and 130<=k2<=205:
                                                     makwifi.network("g"),
                                                 if 358<=j1<=410 and 130<=k2<=205:
                                                     makwifi.network("h"),
                                                 if 421<=j1<=473 and 130<=k2<=205:
                                                     makwifi.network("j"),
                                                 if 486<=j1<=537 and 130<=k2<=205:
                                                     makwifi.network("k"),
                                                 if 548<=j1<=601 and 130<=k2<=205:
                                                     makwifi.network("l"),
                                                 if 101<=j1<=154 and 237<=k2<=314:
                                                     makwifi.network("z"),
                                                 if 165<=j1<=218 and 237<=k2<=314:
                                                     makwifi.network("x"),
                                                 if 230<=j1<=282 and 237<=k2<=314:
                                                     makwifi.network("c"),
                                                 if 294<=j1<=346 and 237<=k2<=314:
                                                     makwifi.network("v"),
                                                 if 357<=j1<=410 and 237<=k2<=314:
                                                     makwifi.network("b"),
                                                 if 421<=j1<=474 and 237<=k2<=314:
                                                     makwifi.network("n"),
                                                 if 486<=j1<=538 and 237<=k2<=314:
                                                     makwifi.network("m"),
                                                 if 486<=j1<=633 and 345<=k2<=422:
                                                     makwifi.network("\n"),
                                                 if  230<=j1<=474 and 345<=k2<=422 :
                                                     makwifi.network(" "),
                                                 if  6<=j1<=78 and 237<=k2<=315 :
                                                     makwifi.keyapplecaptal()
                                                 if 86<=j1<=154 and 345<=k2<=423:
                                                        makwifi.keyapplefarsi()
                                                 if 5<=j1<=74 and 345<=k2<=423:
                                                        makwifi.keyapplealamat()
                                             pygame.display.update() 
        def keyandroidalamat (self):
          # _*_ coding: utf8 _*_
          from easygui import enterbox , ynbox
          global makwifi
          import pygame
          import sys
          pygame.init()
          base=pygame.image.load("alamatandroid.png")
          screen2=pygame.display.set_mode((1150,400))
          screen2.blit(base,(0,0))
          pygame.display.update()
          while 1==1:
                  for event in pygame.event.get():
                             if event.type==pygame.MOUSEBUTTONDOWN :
                                 j1,k2= event.pos[0],event.pos[1]
                                 if 267<=j1<=880 and 316<=k2<=387 :
                                     makwifi.network(" ")
                                 if 973<=j1<=1138 and 152<=k2<=223:
                                     makwifi.network("\n")
                                 if 12<=j1<=107 and 8<=k2<=59 :
                                     makwifi.network("1")
                                 if 125<=j1<=225 and 8<=k2<=59  :
                                     makwifi.network("2")
                                 if 240<=j1<=336 and 8<=k2<=59 :
                                     makwifi.network("3")
                                 if 355<=j1<=450 and 8<=k2<=59 :
                                     makwifi.network("4")
                                 if 468<=j1<=565 and 8<=k2<=59  :
                                     makwifi.network("5")
                                 if 585<=j1<=680 and 8<=k2<=59  :
                                     makwifi.network("6")
                                 if 700<=j1<=795 and 8<=k2<=59  :
                                     makwifi.network("7")
                                 if 815<=j1<=910 and 8<=k2<=59 :
                                     makwifi.network("8")
                                 if 930<=j1<=1025 and 8<=k2<=59 :
                                     makwifi.network("9")
                                 if 1045<=j1<=1140 and 8<=k2<=59 :
                                     makwifi.network("0")
                                 if 12<=j1<=95 and 70<=k2<=140:
                                     makwifi.network("+")
                                 if 115<=j1<=195 and 70<=k2<=140:
                                     makwifi.network("[")
                                 if 215<=j1<=298 and 70<=k2<=140:
                                     makwifi.network("]")
                                 if 317<=j1<=400 and 70<=k2<=140:
                                     makwifi.network("=")
                                 if 420<=j1<=500 and 70<=k2<=140:
                                     makwifi.network("%")
                                 if 520<=j1<=603 and 70<=k2<=140:
                                     makwifi.network("_")
                                 if 622<=j1<=704 and 70<=k2<=140:
                                     makwifi.network("<")
                                 if 723<=j1<=806 and 70<=k2<=140:
                                     makwifi.network(">")
                                 if 825<=j1<=908 and 70<=k2<=140:
                                     makwifi.network("{")
                                 if 927<=j1<=1009 and 70<=k2<=140:
                                     makwifi.network("}")
                                 if 59<=j1<=142 and 152<=k2<=223:
                                     makwifi.network("@")
                                 if 160<=j1<=243 and 152<=k2<=223:
                                     makwifi.network("#")
                                 if 262<=j1<=345 and 152<=k2<=223:
                                     makwifi.network("$")
                                 if 364<=j1<=446 and 152<=k2<=223:
                                     makwifi.network("/")
                                 if 465<=j1<=548 and 152<=k2<=223:
                                     makwifi.network("^")
                                 if 567<=j1<=650 and 152<=k2<=223:
                                     makwifi.network("&")
                                 if 669<=j1<=751 and 152<=k2<=223:
                                     makwifi.network("*")
                                 if 770<=j1<=853 and 152<=k2<=223:
                                     makwifi.network("(")
                                 if 872<=j1<=954 and 152<=k2<=223:
                                     makwifi.network(")")
                                 if 114<=j1<=196 and 234<=k2<=305:
                                     makwifi.network("-")
                                 if 215<=j1<=298 and 234<=k2<=305:
                                     makwifi.network("'")
                                 if 317<=j1<=399 and 234<=k2<=305:
                                     makwifi.network("''")
                                 if 419<=j1<=501 and 234<=k2<=305:
                                     makwifi.network(":")
                                 if 520<=j1<=602 and 234<=k2<=305:
                                     makwifi.network(";")
                                 if 622<=j1<=704 and 234<=k2<=305:
                                     makwifi.network("!")
                                 if 723<=j1<=806 and 234<=k2<=305:
                                     makwifi.network("?")
                                 if 826<=j1<=908 and 234<=k2<=305:
                                     makwifi.network(",")
                                 if 927<=j1<=1009 and 234<=k2<=305:
                                     makwifi.network(".")
                                 if 900<=j1<=1009 and 317<=k2<=387 :
                                             makwifi.menu()
                                 if  1028<=j1<=1138 and 316<=k2<=387:
                                                makwifi.mouse()
                                 if 12<=j1<=119 and 317<=k2<=386:
                                             makwifi.keyboard()
                                 if 138<=j1<=247 and 321<=k2<=387:
                                             makwifi.keyandroidfarsi1()
        def keyapplealamat(self):
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
                                makwifi.network("1"),
                            if 70<=j1<=121 and 21<=k2<=96 :
                                makwifi.network("2"),
                            if 135<=j1<=184 and 21<=k2<=96 :
                                makwifi.network("3"),
                            if 198<=j1<=248 and 21<=k2<=96 :
                                makwifi.network("4"),
                            if 263<=j1<=311 and 21<=k2<=96 :
                                makwifi.network("5"),
                            if 326<=j1<=377 and 21<=k2<=96 :
                                makwifi.network("6"),
                            if 390<=j1<=441 and 21<=k2<=96 :
                                makwifi.network("7"),
                            if 452<=j1<=505 and 21<=k2<=96 :
                                makwifi.network("8"),
                            if 518<=j1<=569 and 21<=k2<=96 :
                                makwifi.network("9"),
                            if 582<=j1<=632 and 21<=k2<=96 :
                                makwifi.network("0"),
                            if 7<=j1<=56 and 129<=k2<=216:
                                makwifi.network("-"),
                            if 70<=j1<=121 and 129<=k2<=216 :
                                makwifi.network("/"),
                            if 135<=j1<=184 and 129<=k2<=216 :
                                makwifi.network(":"),
                            if 198<=j1<=248 and 129<=k2<=216 :
                                makwifi.network(";"),
                            if 263<=j1<=311 and 129<=k2<=216 :
                                makwifi.network("("),
                            if 326<=j1<=377 and 129<=k2<=216 :
                                makwifi.network(")"),
                            if 390<=j1<=441 and 129<=k2<=216 :
                                makwifi.network("$"),
                            if 452<=j1<=505 and 129<=k2<=216 :
                                makwifi.network("&"),
                            if 518<=j1<=569 and 129<=k2<=216 :
                                makwifi.network("@"),
                            if 582<=j1<=632 and 129<=k2<=216 :
                                makwifi.network("''"),
                            if 101<=j1<=180 and 239<=k2<=315 :
                                makwifi.network("."),
                            if 191<=j1<=269 and 239<=k2<=315 :
                                makwifi.network(","),
                            if 278<=j1<=359 and 239<=k2<=315 :
                                makwifi.network("?"),
                            if 370<=j1<=450 and 239<=k2<=315 :
                                makwifi.network("!"),
                            if 422<=j1<=473 and 239<=k2<=315 :
                                makwifi.network("back"),
                            if 486<=j1<=634 and 347<=k2<423 :
                                makwifi.network("\n") ,
                            if 86<=j1<=472 and 346<=k2<=423 :
                                makwifi.network(" "),
                            if 462<=j1<=540 and 239<=k2<=315 :
                                makwifi.network("'"),
                            if 5<=j1<=74 and 345<=k2<=422 :
                                makwifi.keyapple()
                            pygame.display.update()    
                    pygame.display.update()
        def keyapplefarsi(self):
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
                                                     makwifi.network(".q"),
                                                 if 64<=j1<=111 and 24<=k2<=99:
                                                     makwifi.network(".w"),
                                                 if 122<=j1<=149 and 24<=k2<=99  :
                                                     makwifi.network(".e"),
                                                 if 181<=j1<=227 and 24<=k2<=99:
                                                     makwifi.network(".r"),
                                                 if 238<=j1<=285 and 24<=k2<=99:
                                                     makwifi.network(".t"),
                                                 if 296<=j1<=343 and 24<=k2<=9:
                                                     makwifi.network(".y"),
                                                 if 354<=j1<=401 and 24<=k2<=99:
                                                     makwifi.network(".u"),
                                                 if 412<=j1<=459 and 24<=k2<=99:
                                                     makwifi.network(".i"),
                                                 if 470<=j1<=517 and 24<=k2<=99:
                                                     makwifi.network(".o"),
                                                 if 527<=j1<=575 and 24<=k2<=99:
                                                     makwifi.network(".p"),
                                                 if 586<=j1<=633 and 24<=k2<=99:
                                                     makwifi.network(".6"),
                                                 if 6<=j1<=53 and 132<=k2<=208:
                                                     makwifi.network(".a"),  
                                                 if 64<=j1<=111 and 132<=k2<=208:
                                                     makwifi.network(".s"),
                                                 if 122<=j1<=169 and 132<=k2<=208:
                                                     makwifi.network(".d"),
                                                 if 180<=j1<=227 and 132<=k2<=208:
                                                     makwifi.network(".f"),
                                                 if 238<=j1<=285 and 132<=k2<=208:
                                                     makwifi.network(".g"),
                                                 if 296<=j1<=343 and 132<=k2<=208:
                                                     makwifi.network(".h"),
                                                 if 354<=j1<=402 and 132<=k2<=208:
                                                     makwifi.network(".j"),
                                                 if 412<=j1<=460 and 132<=k2<=208:
                                                     makwifi.network(".k"),
                                                 if 470<=j1<=517 and 132<=k2<=208:
                                                     makwifi.network(".l"),
                                                 if 528<=j1<=575 and 132<=k2<=208:
                                                     makwifi.network(".1"),
                                                 if 585<=j1<=636 and 132<=k2<=208:
                                                     makwifi.network(".0"),
                                                 if 7<=j1<=53 and 240<=k2<=316:
                                                     makwifi.network(".3"),
                                                 if 64<=j1<=111 and 240<=k2<=316:
                                                     makwifi.network(".z"),
                                                 if 121<=j1<=169 and 240<=k2<=316 :
                                                     makwifi.network(".x"),
                                                 if 180<=j1<=228 and 240<=k2<=316 :
                                                     makwifi.network(".b"),
                                                 if 237<=j1<=286 and 240<=k2<=316 :
                                                     makwifi.network(".n"),
                                                 if 296<=j1<=344 and 240<=k2<=316 :
                                                     makwifi.network(".c"),
                                                 if 353<=j1<=402 and 240<=k2<=316 :
                                                     makwifi.network(".v"),
                                                 if 411<=j1<=460 and 240<=k2<=316:
                                                     makwifi.network(".2"),
                                                 if 469<=j1<=517 and 240<=k2<=316:
                                                     makwifi.network(".5"),
                                                 if 88<=j1<=348 and 391<=k2<=423:
                                                     makwifi.network(" "),
                                                 if 486<=j1<=633 and 348<=k2<=424:
                                                     makwifi.network("\n"),
                                                 if 407<=j1<=475 and 348<=k2<=424:
                                                     makwifi.keyapple()
                                                 if 5<=j1<=74 and 345<=k2<=422:
                                                     makwifi.keyapplealamat()
                                                 pygame.display.update() 
        def keyapplecaptal(self):
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
                                makwifi.network("Q"),
                            if 70<=j1<=121 and 21<=k2<=96 :
                                makwifi.network("W"),
                            if 135<=j1<=184 and 21<=k2<=96 :
                                makwifi.network("E"),
                            if 198<=j1<=248 and 21<=k2<=96 :
                                makwifi.network("R"),
                            if 263<=j1<=311 and 21<=k2<=96 :
                                makwifi.network("T"),
                            if 326<=j1<=377 and 21<=k2<=96 :
                                makwifi.network("Y"),
                            if 390<=j1<=441 and 21<=k2<=96 :
                                makwifi.network("U"),
                            if 452<=j1<=505 and 21<=k2<=96 :
                                makwifi.network("I"),
                            if 518<=j1<=569 and 21<=k2<=96 :
                                makwifi.network("O"),
                            if 582<=j1<=632 and 21<=k2<=96 :
                                makwifi.network("P"),
                            if 38<=j1<=89 and 129<=k2<=205 :
                                makwifi.network("A"),
                            if 102<=j1<=153 and 129<=k2<=205 :
                                makwifi.network("S"),
                            if 166<=j1<=217 and 129<=k2<=205 :
                                makwifi.network("D"),
                            if 230<=j1<=281 and 129<=k2<=205 :
                                makwifi.network("F"),
                            if 294<=j1<=345 and 129<=k2<=205 :
                                makwifi.network("G"),
                            if 358<=j1<=409 and 129<=k2<=205 :
                                makwifi.network("H"),
                            if 422<=j1<=473 and 129<=k2<=205 :
                                makwifi.network("J"),
                            if 486<=j1<=537 and 129<=k2<=205 :
                                makwifi.network("K"),
                            if 549<=j1<=601 and 129<=k2<=205 :
                                makwifi.network("L"),
                            if 102<=j1<=153 and 237<=k2<=312 :
                                makwifi.network("Z"),
                            if 165<=j1<=217 and 237<=k2<=312 :
                                makwifi.network("X"),
                            if 229<=j1<=282 and 237<=k2<=312 :
                                makwifi.network("C"),
                            if 293<=j1<=345 and 237<=k2<=312 :
                                makwifi.network("V"),
                            if 358<=j1<=409 and 237<=k2<=312 :
                                makwifi.network("B"),
                            if 422<=j1<=473 and 237<=k2<=312 :
                                makwifi.network("N"),
                            if 486<=j1<=537 and 237<=k2<=312 :
                                makwifi.network("M"),
                            if 230<=j1<=473 and 345<=k2<=421 :
                                makwifi.network(" "),
                            if 486<=j1<=632 and 345<=k2<=422 :
                                makwifi.network("\n"),
                            if 6<=j1<=78 and 237<=k2<=315:
                                makwifi.keyapple()
                            if 86<=j1<=154 and 345<=k2<=423:
                                makwifi.keyapplefarsi()
                            if 5<=j1<=74 and 345<=k2<=423:
                                makwifi.keyapplealamat()
                    pygame.display.update()
        def network(self,o):
                from socket import *
                sn=result
                gg=int(result2)
                sp=gg
                cs=socket(AF_INET,SOCK_STREAM)
                cs.connect((sn,sp))
                str=o
                cs.send(str)
                ms=cs.recv(1024)
                cs.close()
        def girande(self):
                from socket import *
                a=raw_input()
                sp=12619
                ss=socket(AF_INET,SOCK_STREAM)
                ss.bind(('',sp))
                ss.listen(1)
                while True:
                    f=open(a,"a")
                    sp+=1
                    cs,addr=ss.accept()
                    data=cs.recv(1024)
                    if len(data)==1:
                        f.write(data)
                    if len(data)==2:
                        if data[1]=="0":
                            f.write("گ")
                        if data[1]=="1":
                            f.write("ک")
                        if data[1]=="2":
                            f.write("و")
                        if data[1]=="3":
                            f.write("پ")
                        if data[1]=="5":
                            f.write("چ")
                        if data[1]=="6":
                            f.write("ج")
                        if data[1]=="w":
                            f.write("ص")
                        if data[1]=="q":
                            f.write("ض")
                        if data[1]=="e":
                            f.write("ث")
                        if data[1]=="r":
                            f.write("ق")
                        if data[1]=="t":
                            f.write("ف")
                        if data[1]=="y":
                            f.write("غ")
                        if data[1]=="u":
                            f.write("ع")
                        if data[1]=="i":
                            f.write("ه")
                        if data[1]=="o":
                            f.write("خ")
                        if data[1]=="p":
                            f.write("ح")
                        if data[1]=="a":
                            f.write("ش")
                        if data[1]=="s":
                            f.write("س")
                        if data[1]=="d":
                            f.write("ي")
                        if data[1]=="f":
                            f.write("ب")
                        if data[1]=="g":
                            f.write("ل")
                        if data[1]=="h":
                            f.write("ا")
                        if data[1]=="j":
                            f.write("ت")
                        if data[1]=="k":
                            f.write("ن")
                        if data[1]=="l":
                            f.write("م")
                        if data[1]=="z":
                            f.write("ظ")
                        if data[1]=="x":
                            f.write("ط")
                        if data[1]=="c":
                            f.write("ز")
                        if data[1]=="v":
                           f.write("ر")
                        if data[1]=="b":
                            f.write("ذ")
                        if data[1]=="n":
                            f.write("د")
                        if data[1]=="m":
                            f.write("ئ")   
                    f.close()
                    cs.send(data)
                    cs.close()

        def mouse (self):
          import pygame
          import sys
          from easygui import enterbox , ynbox
          a=0
          global screen
          x=0
          #1138 388
          pygame.init()
          pygame.display.set_caption("wifi mouse pro")
          screen4=pygame.display.set_mode((380,554))
          screen4.fill((16,18,33))
          base7=pygame.image.load("1.jpg")
          base=pygame.image.load("b.png")
          base1=pygame.image.load("408899.jpg")
          base2=pygame.image.load("408899 - Copy (1).jpg")
          base3=pygame.image.load("Untitled-2.jpg")
          a="yes"
          p=1
          screen4.blit(base1,(0,0))
          screen4.blit(base2,(0,499))
          screen4.blit(base7,(332,8))
          pygame.display.update()
          while 1==1:
               for event in pygame.event.get():
                         if event.type==pygame.MOUSEBUTTONDOWN :
                                 m,n= event.pos[0],event.pos[1]
                                 if 332<=m<=365 and 8<=n<=30:
                                         jj=ynbox('Do you want to go to keyboard?', 'keyboard', ('Yes', 'No'))
                                         if jj==True:
                                                 makwifi.keyboard()
                                 if 0<=m<=190 and 499<=n<=554 :
                                     makwifi.network("kilik chap")
                                 if 191<=m<=380 and 499<=n<=554 :
                                     makwifi.network("kilik rast")
                                 if 0<=m<=378 and 0<=n<=498 :
                                     makwifi.network("lamse vasat")  
makwifi=makwifi1()
makwifi.menu()



