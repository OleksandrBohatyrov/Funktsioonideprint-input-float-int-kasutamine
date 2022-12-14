from math import *
from random import *


#1
##Ras4et diametra okruzhnosti1
##Napishite programmu, kotoraya sprosit dlinu okruzhnosti u dereva

#print("Puu läbimõõdu arvutamine")
#try:
#    C=float(input("Anna ümbermõõt "))
#    if C>0:
#        d=round(C/pi, 2)
#        print("Puu läbimõõt =",d)
#    else:
#        print("C peab olema suurem kui 0")
#except:
#    print("Andmetüüp on vale")

#2 Рассчитайте длину диагонали прямоугольного участка земли размерами Nm x Mm в командной строке Python. N и M спрашивают пользователя.

#try:
#    M=float(input("Ristüliku esimine külg ->"))
#    N=float(input("Ristüliku teine külg ->"))
#    if M>0 and N>0:
#        c=round(sqrt(N**2+M**2),2)
#        print("Ristkülikukujulise maatüki diagonaal on",c)
#    else:
#       print("Nepravilno")
#except:2
#      print("M ja N peavad o")
    

#3 Leidke järgnevast näiteprogrammist semantiline viga
#try:
#    aeg = float(input("Mitu tundi kulus sõiduks? "))
#    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#    if aeg>0 and teepikkus>0:
#        kiirus = teepikkus / aeg
#        print("Sinu kiirus oli " + str(kiirus) + " km/h")
#    else:
#        print("Menshe 0")
#except:
#    print("Nepravilno")



#4 


#try:
#    A1=int(input("Esimene arv: "))
#    A2=int(input("Teine arv: "))
#    A3=int(input("Kolmas arv: "))
#    A4=int(input("Neljas arv: "))
#    A5=int(input("Viies arv: "))
#    if A1>0 and A2>0 and A3>0 and A4>0 and A5>0:
#        avg=(A1+A2+A3+A4+A5)/5
#        print("Kesknime on ", avg)
#    else:
#        print("Menshe 0")
#except:
#        print("Nepravilno")

#5
#print("  @..@ ")
#print(" (----)")
#print(" ( \__/ ) ")
#print(' ^^ "" ^^ ')

#6

#try:
#    a=randint(0,100)
#    b=randint(0,100)
#    c=randint(0,100)
#    print(f"a={a}\nb={b}\nc={c}")
#    P=a+b+c
#    print("ümbermõõt ", P)
#except:
#    print("Nepravilno")


#7
#try:
#    P=randint(1,6)
#    summa=(12.9*1.1)/P
#    print(P,"-st, Igaüks maksab ", summa)
#except:
#    print("Nepravilno")

#8
#try:
#    l=float(input("sisestage täidetud kütuse liitrid: "))
#    km=float(input("sisestage läbitud kilomeetrid: "))
#    if l>0 and km>0:
#        kulu=(l/km)*100
#        print("Kütusekulu",kulu)
#    else:
#        print("Menshe 0")
#except:
#    print("Nepravilno")

#9
#try:
#    M=int(input("Minutid: "))
#    if M>0:
#        M=M/60
#        tee=M*29.9
#        print("Jõuab",tee,'km')
#    else:
#        print("Menshe 0")
#except:
#    print("Nepravilno")


#10
#try:
#    M=int(input("sisestage minutid: ")) 
#    if M>0:
#        H=M//60 
#        M=M%60 
#        print(f"{H}:{M}")
#    else:
#        print("Menshe")
#except:
#    print("Nepravilno")

#11
#Ülessanne "Ema roobot".
#Ema küsib "Mis hinde sa koolis said?", laps vastab ja ootab ema reaktsioon
print("Ema roobot")
a=input("Sisesta: ")
print(a.isalpha(), a.isdigit())
if a.isdigit() and int(a)>0 and int(a)<=5:
    a=int(a)
    if a==5:
        print("Hästi")
    elif a==4:
        print("Hästi")
    elif a==3:
        print("Normaalset")
    elif a==2:
        print("Halvasti")
    elif a==1:
        print("Halvasti")
else:
    print("Sa valesti vastas")
    #123