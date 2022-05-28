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
              base=pygame.image.load("a.png")
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
                              makwifi.pc()
        def network(self,o):
                from socket import *
                sn=result
                sp=12028
                cs=socket(AF_INET,SOCK_STREAM)
                cs.connect((sn,sp))
                str=o
                cs.send(str)
                ms=cs.recv(1024)
                cs.close()        
                          
        def pc (slef):
          k10=[]
          import pygame
          import sys
          a=0
          x=0
          #1138 388
          pygame.init()
          pygame.display.set_caption("wifi mouse pro")
          base=pygame.image.load("b.png")
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












