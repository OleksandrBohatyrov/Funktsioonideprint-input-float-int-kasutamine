from math import *
from random import *


#1
#Ras4et diametra okruzhnosti
#Napishite programmu, kotoraya sprosit dlinu okruzhnosti u dereva

#print("Puu läbimõõdu arvutamine")
#C=float(input("Anna ümbermõõt "))
#d=round(C/pi,2)
#print("Puu läbimõõt =",d)

#2 Рассчитайте длину диагонали прямоугольного участка земли размерами Nm x Mm в командной строке Python. N и M спрашивают пользователя.

#print("Ristüliku omadused")
#M=float(input("Ristüliku esimine külg ->"))
#N=float(input("Ristüliku teine külg ->"))
#c=math.sqrt(N**2+M**2)
#print("Ristüliku pikkus on", round(c,2))
#print()


#3 Leidke järgnevast näiteprogrammist semantiline viga
#aeg = float(input("Mitu tundi kulus sõiduks? "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus = teepikkus / aeg

#print("Sinu kiirus oli " + str(kiirus) + " km/h")

#4 

#print("Aritmeetiline kekmine")
#A1=int(input("Esimene arv: "))
#A2=int(input("Teine arv: "))
#A3=int(input("Kolmas arv: "))
#A4=int(input("Neljas arv: "))
#A5=int(input("Viies arv: "))
#avg=(A1+A2+A3+A4+A5)/5
#print("Kesknime on ", avg)

#5
#print("  @..@ ")
#print(" (----)")
#print(" ( \__/ ) ")
#print(' ^^ "" ^^ ')

#6

#a=randint(0,100)
#b=randint(0,100)
#c=randint(0,100)
#print(f"a={a}\nb={b}\nc={c}")
#P=a+b+c
#print("ümbermõõt ", P)


#7

#P=randint(1,6)
#summa=(12.9*1.1)/P
#print(P,"-st, Igaüks maksab ", summa)

#8
#l=float(input("sisestage täidetud kütuse liitrid: "))
#km=float(input("sisestage läbitud kilomeetrid: "))
#kulu=(l/km)*100
#print("Kütusekulu",kulu)

#9

#print("Rulluisutajad")
#M=int(input("Minutid: "))
#M=M/60
#tee=M*29.9
#print("Jõuab",tee,'km')


#10
M=int(input("sisestage minutid: ")) #1h=60m
H=M//60 #H
M=M%60 #min
print(f"{H}:{M}")