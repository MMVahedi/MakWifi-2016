# _*_ coding: utf8 _*_
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
              base=pygame.image.load("WiFi-Mouse-Pro.png")
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
                          if 80<=j<=300 and 275<=k<=330 and p==0:
                              result =enterbox("Enter server IP,please like this 1222.1333.1444.1555","server IP")
                              global result
                              p=1
                              makwifi.keyboard()
                          if 80<=j<=300 and 415<=k<=470 and p==0 :
                                   result =enterbox("Enter server IP,please like this 1222.1333.1444.1555","server IP")
                                   global result
                                   makwifi.mouse()
                                   p=1
                          if 86<=j<=294 and 353<=k<=398 and p==0 :
                                  result =enterbox("Enter server IP,please like this 1222.1333.1444.1555","server IP")
                                  global result
                                  makwifi.pc()
                                  p=1
        def keyboard (self):
                                          # _*_ coding: utf8 _*_
                                          k10=[]
                                          from easygui import enterbox , ynbox
                                          global makwifi
                                          import pygame
                                          import sys
                                          a=0
                                          x=0
                                          #1138 388
                                          pygame.init()
                                          base=pygame.image.load("WiFi-Mouse-Pro.png")
                                          base1=pygame.image.load("408899.jpg")
                                          base2=pygame.image.load("408899 - Copy (1).jpg")
                                          base3=pygame.image.load("Untitled-2.jpg")
                                          base4=pygame.image.load("english1.jpg")
                                          base5=pygame.image.load("persian2.jpg")
                                          base6=pygame.image.load("persian1.jpg")
                                          k=0
                                          a="yes"
                                          screen2=pygame.display.set_mode((1150,400))
                                          q=2
                                          screen2.blit(base3,(0,0))
                                          p=1
                                          taipefarsi=1
                                          shart=0
                                          bozorg=1
                                          pygame.display.update()
                                          while 1==1:
                                                         for event in pygame.event.get():
                                                             if event.type==pygame.MOUSEBUTTONDOWN :
                                                                 j1,k2= event.pos[0],event.pos[1]
                                                                 if 12<=j1<=95 and 70<=k2<=140 and q%2==0 and shart==0:
                                                                     makwifi.network("q")
                                                                 if 115<=j1<=195 and 70<=k2<=140 and q%2==0 and shart==0:
                                                                     makwifi.network("w")
                                                                 if 215<=j1<=298 and 70<=k2<=140 and q%2==0 and shart==0:
                                                                     makwifi.network("e")
                                                                 if 317<=j1<=400 and 70<=k2<=140 and q%2==0 and shart==0:
                                                                     makwifi.network("r")
                                                                 if 420<=j1<=500 and 70<=k2<=140 and q%2==0 and shart==0:
                                                                     makwifi.network("t")
                                                                 if 520<=j1<=603 and 70<=k2<=140 and q%2==0 and shart==0:
                                                                     makwifi.network("y")
                                                                 if 622<=j1<=704 and 70<=k2<=140 and q%2==0 and shart==0:
                                                                     makwifi.network("u")
                                                                 if 723<=j1<=806 and 70<=k2<=140 and q%2==0 and shart==0:
                                                                     makwifi.network("i")
                                                                 if 825<=j1<=908 and 70<=k2<=140 and q%2==0 and shart==0:
                                                                     makwifi.network("o")
                                                                 if 927<=j1<=1009 and 70<=k2<=140 and q%2==0 and shart==0:
                                                                     makwifi.network("p")
                                                                 if 59<=j1<=142 and 152<=k2<=223 and q%2==0 and shart==0:
                                                                     makwifi.network("a")
                                                                 if 160<=j1<=243 and 152<=k2<=223 and q%2==0 and shart==0:
                                                                     makwifi.network("s")
                                                                 if 262<=j1<=345 and 152<=k2<=223 and q%2==0 and shart==0:
                                                                     makwifi.network("s")  
                                                                 if 364<=j1<=446 and 152<=k2<=223 and q%2==0 and shart==0:
                                                                     makwifi.network("f")
                                                                 if 465<=j1<=548 and 152<=k2<=223 and q%2==0 and shart==0:
                                                                     makwifi.network("g")
                                                                 if 567<=j1<=650 and 152<=k2<=223 and q%2==0 and shart==0:
                                                                     makwifi.network("h")
                                                                 if 669<=j1<=751 and 152<=k2<=223 and q%2==0 and shart==0:
                                                                     makwifi.network("j")
                                                                 if 770<=j1<=853 and 152<=k2<=223 and q%2==0 and shart==0:
                                                                     makwifi.network("k")
                                                                 if 872<=j1<=954 and 152<=k2<=223 and q%2==0 and shart==0:
                                                                     makwifi.network("l")
                                                                 if 114<=j1<=196 and 234<=k2<=305 and q%2==0 and shart==0:
                                                                     makwifi.network("z")
                                                                 if 215<=j1<=298 and 234<=k2<=305 and q%2==0 and shart==0:
                                                                     makwifi.network("x")
                                                                 if 317<=j1<=399 and 234<=k2<=305 and q%2==0 and shart==0:
                                                                     makwifi.network("c")
                                                                 if 419<=j1<=501 and 234<=k2<=305 and q%2==0 and shart==0:
                                                                     makwifi.network("v")
                                                                 if 520<=j1<=602 and 234<=k2<=305 and q%2==0 and shart==0:
                                                                     makwifi.network("b")
                                                                 if 622<=j1<=704 and 234<=k2<=305 and q%2==0 and shart==0:
                                                                     makwifi.network("n")
                                                                 if 723<=j1<=806 and 234<=k2<=305 and q%2==0 and shart==0:
                                                                     makwifi.network("m")
                                                                 if 826<=j1<=908 and 234<=k2<=305 and q%2==0:
                                                                     makwifi.network(",")
                                                                 if 927<=j1<=1009 and 234<=k2<=305 and q%2==0:
                                                                     makwifi.network(".")
                                                                 if 267<=j1<=880 and 316<=k2<=387 :
                                                                     makwifi.network(" ")
                                                                 if 973<=j1<=1138 and 152<=k2<=223 and q%2==0 :
                                                                     makwifi.network("\n")
                                                                 if 102<=j1<=1137 and 316<=k2<=387 and q%2==0:
                                                                      a="no"
                                                                      ###########booz
                                                                 if 1029<=j1<=1138 and 70<=k2<=140 :
                                                                     print chr()
                                                                 if 12<=j1<=95 and 70<=k2<=140 and q%2!=0 and shart==0:
                                                                     makwifi.network("Q")
                                                                 if 115<=j1<=195 and 70<=k2<=140 and q%2!=0 and shart==0:
                                                                     makwifi.network("W")
                                                                 if 215<=j1<=298 and 70<=k2<=140 and q%2!=0 and shart==0:
                                                                     makwifi.network("E")
                                                                 if 317<=j1<=400 and 70<=k2<=140 and q%2!=0 and shart==0:
                                                                     makwifi.network("R")
                                                                 if 420<=j1<=500 and 70<=k2<=140 and q%2!=0 and shart==0:
                                                                     makwifi.network("T")
                                                                 if 520<=j1<=603 and 70<=k2<=140 and q%2!=0 and shart==0:
                                                                     makwifi.network("Y")
                                                                 if 622<=j1<=704 and 70<=k2<=140 and q%2!=0 and shart==0:
                                                                     makwifi.network("U")
                                                                 if 723<=j1<=806 and 70<=k2<=140 and q%2!=0 and shart==0:
                                                                     makwifi.network("I")
                                                                 if 825<=j1<=908 and 70<=k2<=140 and q%2!=0 and shart==0:
                                                                     makwifi.network("O")
                                                                 if 927<=j1<=1009 and 70<=k2<=140 and q%2!=0 and shart==0:
                                                                     makwifi.network("P")
                                                                 if 59<=j1<=142 and 152<=k2<=223 and q%2!=0 and shart==0:
                                                                     makwifi.network("A")
                                                                 if 160<=j1<=243 and 152<=k2<=223 and q%2!=0 and shart==0:
                                                                     makwifi.network("S")
                                                                 if 262<=j1<=345 and 152<=k2<=223 and q%2!=0 and shart==0:
                                                                     makwifi.network("D")
                                                                 if 364<=j1<=446 and 152<=k2<=223 and q%2!=0 and shart==0:
                                                                     makwifi.network("F")
                                                                 if 465<=j1<=548 and 152<=k2<=223 and q%2!=0 and shart==0:
                                                                     makwifi.network("G")
                                                                 if 567<=j1<=650 and 152<=k2<=223 and q%2!=0 and shart==0:
                                                                     makwifi.network("H")
                                                                 if 669<=j1<=751 and 152<=k2<=223 and q%2!=0 and shart==0:
                                                                     makwifi.network("J")
                                                                 if 770<=j1<=853 and 152<=k2<=223 and q%2!=0 and shart==0:
                                                                     makwifi.network("K")
                                                                 if 872<=j1<=954 and 152<=k2<=223 and q%2!=0 and shart==0:
                                                                     makwifi.network("L")
                                                                 if 114<=j1<=196 and 234<=k2<=305 and q%2!=0 and shart==0:
                                                                     makwifi.network("Z")
                                                                 if 215<=j1<=298 and 234<=k2<=305 and q%2!=0 and shart==0:
                                                                     makwifi.network("X")
                                                                 if 317<=j1<=399 and 234<=k2<=305 and q%2!=0 and shart==0:
                                                                     makwifi.network("C")
                                                                 if 419<=j1<=501 and 234<=k2<=305 and q%2!=0 and shart==0:
                                                                     makwifi.network("V")
                                                                 if 520<=j1<=602 and 234<=k2<=305 and q%2!=0 and shart==0:
                                                                     makwifi.network("B")
                                                                 if 622<=j1<=704 and 234<=k2<=305 and q%2!=0 and shart==0:
                                                                     makwifi.network("N")
                                                                 if 723<=j1<=806 and 234<=k2<=305 and q%2!=0 and shart==0:
                                                                     makwifi.network("M")
                                                                 if 826<=j1<=908 and 234<=k2<=305 and q%2!=0 and shart==0:
                                                                     makwifi.network("!")
                                                                 if 927<=j1<=1009 and 234<=k2<=305 and q%2!=0 and shart==0:
                                                                     makwifi.network("?")
                                                                 if 900<=j1<=1009 and 317<=k2<=387 :
                                                                         jj=ynbox('Do you want to go to menu?', 'menu', ('Yes', 'No'))
                                                                         if jj==True:
                                                                                 makwifi.menu()
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
                                                                 if 12<=j1<=95 and 70<=k2<=141 and bozorg%2!=0 and shart==1:
                                                                     makwifi.network( ".w")
                                                                 if 114<=j1<=196 and 70<=k2<=141 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".e")
                                                                 if 215<=j1<=298 and 70<=k2<=141 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".r")
                                                                 if 317<=j1<=399 and 70<=k2<=141 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".t")
                                                                 if 419<=j1<=501 and 70<=k2<=141 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network(".u")
                                                                 if 520<=j1<=603 and 70<=k2<=141 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".i")
                                                                 if 623<=j1<=704 and 70<=k2<=141 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".o")
                                                                 if 723<=j1<=806 and 70<=k2<=141 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".p")
                                                                 if 825<=j1<=909 and 70<=k2<=141 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".6")
                                                                      #.6=jim
                                                                 if 927<=j1<=1010 and 70<=k2<=141 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".5")
                                                                      #.5=che
                                                                 if 12<=j1<=95 and 152<=k2<=223 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".a")
                                                                 if 114<=j1<=196 and 152<=k2<=223 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".s")
                                                                 if 215<=j1<=298 and 152<=k2<=223 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".d")
                                                                 if 317<=j1<=399 and 152<=k2<=223 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".f")
                                                                 if 419<=j1<=501 and 152<=k2<=223 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".g")
                                                                 if 520<=j1<=603 and 152<=k2<=223 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".h")
                                                                 if 623<=j1<=704 and 152<=k2<=223 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".j")
                                                                 if 723<=j1<=806 and 152<=k2<=223 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".k")
                                                                 if 825<=j1<=909 and 152<=k2<=223 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".l")
                                                                 if 927<=j1<=1010 and 152<=k2<=223 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".3")
                                                                      #.3=pe
                                                                 if 114<=j1<=196 and 223<=k2<=305 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".x")
                                                                 if 215<=j1<=297 and 223<=k2<=305 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".c")
                                                                 if 317<=j1<=399 and 223<=k2<=305 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".v")
                                                                 if 419<=j1<=501 and 223<=k2<=305 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".n")
                                                                 if 520<=j1<=602 and 223<=k2<=305 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network(".2")
                                                                      #.2=ve
                                                                 if 622<=j1<=704 and 223<=k2<=305 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".1")
                                                                      #.1=ke
                                                                 if 724<=j1<=805 and 223<=k2<=305 and bozorg%2!=0 and shart==1:
                                                                      makwifi.network( ".0")
                                                                      #.0=ge
                                                                 #if 114<=j1<=196 and 70<=k2<=141 and bozorg%2!=0 and shart==1:
                                                                 if  12<=j1<=95 and 234<=k2<=305 and shart==0:
                                                                     q=q+1
                                                                     if q%2!=0:
                                                                          screen2.blit(base4,(0,0))
                                                                          pygame.display.update()
                                                                     else:
                                                                          screen2.blit(base3,(0,0))
                                                                          pygame.display.update()
                                                                 if  12<=j1<=95 and 234<=k2<=305 and shart==1   :
                                                                      bozorg=bozorg+1
                                                                      if bozorg%2==0:
                                                                          screen2.blit(base6,(0,0))
                                                                          pygame.display.update()
                                                                      else:
                                                                          screen2.blit(base5,(0,0))
                                                                          pygame.display.update()
                                                                 if  1028<=j1<=1138 and 316<=k2<=387  :
                                                                         jj=ynbox('Do you want to go to mouse page?', 'mouse page', ('Yes', 'No'))
                                                                         if jj==True:
                                                                                 makwifi.mouse()
                                                                 if  138<=j1<=248 and 316<=k2<=387  :
                                                                      taipefarsi=taipefarsi+1
                                                                      if taipefarsi%2==0:
                                                                           screen2.blit(base5,(0,0))
                                                                           pygame.display.update()
                                                                           shart=1
                                                                      if taipefarsi%2!=0:
                                                                           screen2.blit(base3,(0,0))
                                                                           pygame.display.update()
                                                                           shart=0
        def network(self,o):
                                                from socket import *
                                                sn=result
                                                sp=12022
                                                cs=socket(AF_INET,SOCK_STREAM)
                                                cs.connect((sn,sp))
                                                str=o
                                                cs.send(str)
                                                ms=cs.recv(1024)
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
                                          base=pygame.image.load("WiFi-Mouse-Pro.png")
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
        def pc (slef):
          k10=[]
          import pygame
          import sys
          a=0
          x=0
          #1138 388
          pygame.init()
          pygame.display.set_caption("wifi mouse pro")
          base=pygame.image.load("WiFi-Mouse-Pro.png")
          base1=pygame.image.load("408899.jpg")
          base2=pygame.image.load("408899 - Copy (1).jpg")
          base3=pygame.image.load("Untitled-2.jpg")
          base4=pygame.image.load("english1.jpg")
          base5=pygame.image.load("persian2.jpg")
          base6=pygame.image.load("persian1.jpg")
          base9=pygame.image.load("Unt88itled.png")
          base50=pygame.image.load("1.png")
          screen9=pygame.display.set_mode((1286,391))
          screen9.fill((16,18,33))
          screen9.blit(base9,(0,0))
          pygame.display.update()
          k=0
          a="yes"
          q=2
          p=1
          taipefarsi=1
          shart=0
          bozorg=1
          k1=2
          while 1:
                    for event in pygame.event.get():
                             if event.type==pygame.KEYDOWN :
                                    if event.key ==pygame.K_CAPSLOCK:
                                       k1=k1+1
                                       screen9.blit(base50,(0,0))
                                       pygame.display.update()
                                    if event.key == pygame.K_a and k1%2==0:
                                       makwifi.network("a")
                                    if event.key ==pygame.K_b and k1%2==0:
                                       makwifi.network("b")
                                    if event.key ==pygame.K_c and k1%2==0:
                                       makwifi.network("c")
                                    if event.key ==pygame.K_d and k1%2==0:
                                       makwifi.network("d")
                                    if event.key ==pygame.K_e and k1%2==0:
                                       makwifi.network("e")
                                    if event.key ==pygame.K_f and k1%2==0:
                                       makwifi.network("f")
                                    if event.key ==pygame.K_g and k1%2==0:
                                       makwifi.network("g")
                                    if event.key ==pygame.K_h and k1%2==0:
                                       makwifi.network("h")
                                    if event.key ==pygame.K_q and k1%2==0:
                                       makwifi.network("q")
                                    if event.key ==pygame.K_w and k1%2==0:
                                       makwifi.network("w")
                                    if event.key ==pygame.K_r and k1%2==0:
                                       makwifi.network("r")
                                    if event.key ==pygame.K_t and k1%2==0:
                                       makwifi.network("t")
                                    if event.key ==pygame.K_y and k1%2==0:
                                       makwifi.network("y")
                                    if event.key ==pygame.K_u and k1%2==0:
                                       makwifi.network("u")
                                    if event.key ==pygame.K_i and k1%2==0:
                                       makwifi.network("i")
                                    if event.key ==pygame.K_o and k1%2==0:
                                       makwifi.network("o")
                                    if event.key ==pygame.K_p and k1%2==0:
                                       makwifi.network("p")
                                    if event.key ==pygame.K_s and k1%2==0:
                                       makwifi.network("s")
                                    if event.key ==pygame.K_j and k1%2==0:
                                       makwifi.network("j")
                                    if event.key ==pygame.K_k and k1%2==0:
                                       makwifi.network("k")
                                    if event.key ==pygame.K_l and k1%2==0:
                                       makwifi.network("l")
                                    if event.key ==pygame.K_z and k1%2==0:
                                       makwifi.network("z")
                                    if event.key ==pygame.K_x and k1%2==0:
                                       makwifi.network("x")
                                    if event.key ==pygame.K_v and k1%2==0:
                                       makwifi.network("v")
                                    if event.key ==pygame.K_n and k1%2==0:
                                       makwifi.network("n")
                                    if event.key ==pygame.K_SPACE :
                                       makwifi.network(" ")
                                    #if event.key ==pygame.K_BACKSPACE:
                                       #print chr(46),
                                    if event.key == pygame.K_m and k1%2==0:
                                       makwifi.network("m")
                                    if event.key ==pygame.K_a and k1%2!=0:
                                       makwifi.network("A")
                                    if event.key ==pygame.K_b and k1%2!=0:
                                       makwifi.network("B")
                                    if event.key ==pygame.K_c and k1%2!=0:
                                       makwifi.network("C")
                                    if event.key ==pygame.K_d and k1%2!=0:
                                       makwifi.network("D")
                                    if event.key ==pygame.K_e and k1%2!=0:
                                       makwifi.network("E")
                                    if event.key ==pygame.K_f and k1%2!=0:
                                       makwifi.network("F")
                                    if event.key ==pygame.K_g and k1%2!=0:
                                       makwifi.network("G")
                                    if event.key ==pygame.K_h and k1%2!=0:
                                       makwifi.network("H")
                                    if event.key ==pygame.K_q and k1%2!=0:
                                       makwifi.network("Q")
                                    if event.key ==pygame.K_w and k1%2!=0:
                                       makwifi.network("W")
                                    if event.key ==pygame.K_r and k1%2!=0:
                                       makwifi.network("R")
                                    if event.key ==pygame.K_t and k1%2!=0:
                                       makwifi.network("T")
                                    if event.key ==pygame.K_y and k1%2!=0:
                                       makwifi.network("Y")
                                    if event.key ==pygame.K_u and k1%2!=0:
                                       makwifi.network("U")
                                    if event.key ==pygame.K_i and k1%2!=0:
                                       makwifi.network("I")
                                    if event.key ==pygame.K_o and k1%2!=0:
                                       makwifi.network("O")
                                    if event.key ==pygame.K_p and k1%2!=0:
                                       makwifi.network("P")
                                    if event.key ==pygame.K_s and k1%2!=0:
                                       makwifi.network("S")
                                    if event.key ==pygame.K_j and k1%2!=0:
                                       makwifi.network("J")
                                    if event.key ==pygame.K_k and k1%2!=0:
                                       makwifi.network("K")
                                    if event.key ==pygame.K_l and k1%2!=0:
                                       makwifi.network("L")
                                    if event.key ==pygame.K_z and k1%2!=0:
                                       makwifi.network("Z")
                                    if event.key ==pygame.K_x and k1%2!=0:
                                       makwifi.network("X")
                                    if event.key ==pygame.K_v and k1%2!=0:
                                       makwifi.network("V")
                                    if event.key ==pygame.K_n and k1%2!=0:
                                       makwifi.network("N")
                                    if event.key == pygame.K_m and k1%2!=0:
                                       makwifi.network("M")
                                    if event.key ==pygame.K_1 and k1%2==0:
                                       makwifi.network("1")
                                    if event.key ==pygame.K_2 and k1%2==0:
                                       makwifi.network("2")
                                    if event.key ==pygame.K_3 and k1%2==0:
                                       makwifi.network("3")
                                    if event.key ==pygame.K_4 and k1%2==0:
                                       makwifi.network("4")
                                    if event.key ==pygame.K_5 and k1%2==0:
                                       makwifi.network("5")
                                    if event.key ==pygame.K_6 and k1%2==0:
                                       makwifi.network("6")
                                    if event.key ==pygame.K_7 and k1%2==0:
                                       makwifi.network("7")
                                    if event.key ==pygame.K_8 and k1%2==0:
                                       makwifi.network("8")
                                    if event.key ==pygame.K_9 and k1%2==0:
                                       makwifi.network("9")
                                    if event.key ==pygame.K_0 and k1%2==0:
                                       makwifi.network("0")
                                   #if event.key ==pygame.K_- and k1%2==0:
                                    #   print "-",
                                    #if event.key ==pygame.K_= and k1%2==0:
                                     #  print "=",
                                    #if event.key == pygame.K_` and k1%2==0:
                                     #  print "`",
                                    if event.key ==pygame.K_1 and k1%2!=0:
                                       makwifi.network("!")
                                    if event.key ==pygame.K_2 and k1%2!=0:
                                       makwifi.network("@")
                                    if event.key ==pygame.K_3 and k1%2!=0:
                                       makwifi.network("#")
                                    if event.key ==pygame.K_4 and k1%2!=0:
                                       makwifi.network("$")
                                    if event.key ==pygame.K_5 and k1%2!=0:
                                       makwifi.network("%")
                                    if event.key ==pygame.K_6 and k1%2!=0:
                                       makwifi.network("^")
                                    if event.key ==pygame.K_7 and k1%2!=0:
                                       makwifi.network("&")
                                    if event.key ==pygame.K_8 and k1%2!=0:
                                       makwifi.network("*")
                                    if event.key ==pygame.K_9 and k1%2!=0:
                                       makwifi.network("(")
                                    if event.key ==pygame.K_0 and k1%2!=0:
                                       makwifi.network(")")
                                    #if event.key ==pygame.K_- and k1%2!=0:
                                     #  print "_",
                                    #if event.key ==pygame.K_= and k1%2!=0:
                                     #  print "+",
                                    #if event.key ==pygame.K_- and k1%2!=0:
                                     #  print "_",
                                    #if event.key ==pygame.K_= and k1%2!=0:
                                     #  print "+",
                                    #if event.key == pygame.K_` and k1%2!=0:                                              
makwifi=makwifi1()
makwifi.menu()






































                                  
          
