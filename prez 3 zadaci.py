'''
# Zadaca1 | dali vnesen broj e paren   / na cas /

a = int(input("Vnesi broj"))
if a%2 ==0:
    print("Brojot e paren")
else:
    print("Brojot e neparen")
'''

'''
#Prez 3 zadaca 2 | spored vnese broj teks od dadena tabela  / na cas

a = int(input("Vnesi broj"))
if a >= 1000:
    print("preterano pozitiven")
elif a >=100 and a < 999:
    print("mnogu pozitiven")
elif a >=100 and a <= 999:
    print("mnogu pozitiven")
elif a >0 and a < 100:
    print("pozitiven")
elif a == 0:
    print("nula")
elif a >-100 and a < 0:
    print("negtiven")
elif a >-999 and a <= -100:
    print("mnogu negativen")
elif a <= -1000:
    print("pozitiven")
else:
    print("Greska") '''
'''#alt j za selection na poveke isti zborovi ...'''

'''
# zadaca 3 | poeni na vles ocenka na izlez / na cas

a = int(input("Vnesi osvoeni bodovi od testot"))
if a >=0 and a < 61:
    print("Ocenka: 1")
elif a >= 61 and a <= 70:
    print("Ocenka: 2")
elif a >= 71 and a <= 80:
    print("Ocenka: 3")
elif a >= 81 and a <= 90:
    print("Ocenka: 4")
elif a >= 91 and a <= 100:
    print("Ocenka: 5")
else:
    print("Greska") '''


''' #zadaca 3.4 | Calculator

a = int(input("Vnesete go prviot broj"))
b = input("Vnesete go operatorot (+ - / *)")
c = int(input("Vnesete go vtoriot broj"))

if b == "+":
    d = a + c
elif b == "-":
    d = a - c
elif b == "/":
    d = a / c
elif b == "*":
    d = a * c
else:
    print("Greska")
print(d)'''


'''# zadaca 3.5 | broj na mesec --> kolku denovi ima  
a = int(input("Vnesete broj od 0-12"))
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or  a== 10 or a == 12:
    print("Mesecot ima 31 den")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print("Mesecot ima 30 den")
elif a == 2:
    print("Mesecot im 28(29) dena")
else:
    print("Greska vnesni broj od 0-12")'''

'''# zadaca 3.6 | broj na den vo nedela --> denot

a = int(input("Vnesete reden broj na den vo nedelata"))
if a == 1:
    print("Ponedelnik")
elif a == 2:
    print("Vtornik")
elif a == 3:
    print("Sreda")
elif a == 4:
    print("Cetvrtok")
elif a == 5:
    print("Petok")
elif a == 6:
    print("Sabota")
elif a == 7:
    print("Nedela")
else:
    print("Greska")'''

'''# 3.7 | spored prosek od 5 oceni kakov e ucenikot 

a = input("Vnesi ime na ucenik:")
print("Vnesi gi ocenkite za:")
b = int(input("matematika"))
c = int(input("makedonski"))
d = int(input("geografija"))
e = int(input("istorija"))
f = int(input("informatika"))
g = (b+c+d+e+f)/5
m = b+c+d+e+f
print(f"Prosekot e: {g} a vkupniot zbir: {m}")
if g >= 4.5 and g <= 5:
    print("odlicen")
elif g >= 3.5 and g < 4.5:
    print("mnogu dobar")
elif g >= 2.5 and g < 3.5:
    print("dobar")
elif g >= 1.5 and g < 2.5:
    print("dovolen")
elif g > 0 and g < 1.5:
    print("nedovolen")
else:
    print("Greska")'''

'''#zad 3.8 | dozvoleno vnes samo na dvocifren broj vlez 89 na izlez "osum devet"

a=input("Vnesete dvocifren broj:")
if len(a) != 2:
    print("Greska")                            
elif a.isdecimal() != True:
    print("Greska")
else:
    if a[0] == "1":
        b = "eden"
    elif a[0] == "2":
        b = "dva"
    elif a[0] == "3":
        b = "tri"
    elif a[0] == "4":
        b = "cetiri"
    elif a[0] == "5":
        b = "pet"
    elif a[0] == "6":
        c = "sest"
    elif a[0] == "7":
        b = "sedum"
    elif a[0] == "8":
        b = "osum"
    elif a[0] == "9":
        b = "devet"
    else:
        b = "nula"
    if a[1] == "1":
        c = "eden"
    elif a[1] == "2":
        c = "dva"
    elif a[1] == "3":
        c = "tri"
    elif a[1] == "4":
        c = "cetiri"
    elif a[1] == "5":
        c = "pet"
    elif a[1] == "6":
        c = "sest"
    elif a[1] == "7":
        c = "sedum"
    elif a[1] == "8":
        c = "osum"
    elif a[1] == "9":
        c = "devet"
    else:
        c = "nula"
    print(b + " " + c)'''



'''
#Zadaca 9 | dali vnesenata godina e prestapna

a = input("Vnesi ja godinata:")
if len(a) != 4:
    print("Greska")
elif a.isdecimal() != True:
    print("Greska")
else:
    if a % 4 ==0
        print("Pristapna godina")
    else:
        print("Ne e prestana")'''


'''
#Zadaca 10 | vnesena godina na ragane izlez dali moze da glasa

b = input("Vnesi godina na ragane:")
if len(b) != 4:
    print("Greska")
elif a.isdecimal() != True:
    print("Greska")
else:
    a=int(b)
    if 2024-a >= 18:
        print("Imate pravo na glas")
    else:
        print("Nemate pravo na glas")'''


'''#zad12 ne postoi 11| dali daden karakter e cifra bukva ili specialen karakter 

a = input("Vnesi eden karakter")
if len(a) != 1:
    print("Greska")
elif a.isdecimal() == True:
    print("Karakterot e cifra")
elif a.isalpha() == True:
    print("Karakterot e bukva")
else:
    print("karakterot e specialen znak")'''

'''
#zad13 | zbir na agli 180 - bez proverka na vlez

print("Vnesi 3 agli")
a = int(input("Vnesi agol broj 1 :"))
b = int(input("Vnesi agol broj 2 :"))
c = int(input("Vnesi agol broj 3 :"))
d = a+b+c
if d == 180:
    print("Moze da se formira triagolnik")
else:
    print("Ne moze da se formira triagolnik")'''



'''#zad14 | dadena dictionry korisnik vnesuva grad da se ispecati ako postoi negovata cena vo sportivno None...

flight_prices = {
    "Dortmund":4489, "Frankfurt":7128, "Budapest":2595, "Berlin":8910,
     "Paris":3537, "Venice":2668, "London":2595, "Milan":2595, "Rome":5658, "Malta":5578,}

a = input("Destinacija:")
if a == "Dortmund":
    print(flight_prices["Dortmund"])
elif a == "Frankfurt":
    print(flight_prices["Frankfurt"])
elif a == "Budapest":
    print(flight_prices["Budapest"])
elif a == "Berlin":
    print(flight_prices["Berlin"])
elif a == "Paris":
    print(flight_prices["Paris"])
elif a == "Venice":
    print(flight_prices["Venice"])
elif a == "London":
    print(flight_prices["London"])
elif a == "Milan":
    print(flight_prices["Milan"])
elif a == "Rome":
    print(flight_prices["Rome"])
elif a == "Malta":
    print(flight_prices["Malta"])
else:
    flight_prices[a] ="None"
    print(f"Ne postoi grad {a}")
    print(flight_prices)'''

'''
#zad15 | Da spojuva 2 listi, DA NEE E l1+l2 > 10 elementi  ; l1+l2>4 inaku dopolni so 0;
# l1+l2 da nema duplikati i sortirana po azbucen redosled;

#a = [1,2,3,4,5]
#b = [6,7,8,9,10]
#a= [1]
#b = []
#a = [1,2,3,4,5]
#b = [6,7,8,9,10,11,12]
#a = ["F","i","i"]
#b = ["Q"]
a= ["Fi","lip"]
b = ["kos","sta","di","nov"]

adolz = len(a)
bdolz = len(b)
d = adolz + bdolz

flag = 1



if d > 10:
    #print("Greska")
    flag = 0
if d < 4:
    if d == 3:
        if adolz < bdolz:
            a.append(0)
        else:
            b.append(0)
    elif d == 2:
        a.append(0)
        b.append(0)
    else:                     # a - 1 b-0 ili b-1 a-0
        if adolz < bdolz:
            a.append(0)
            a.append(0)
            b.append(0)
        else:
            b.append(0)
            b.append(0)
            a.append(0)


adolzcopy = a.copy()
adolzcopy.extend(b)
    #print(adolzcopy)
m = len(adolzcopy)
z5 = 1
z6 = 1
z7 = 1
z8 = 1
z9 = 1
z10 = 1
z1 = a.count(adolzcopy[0])
z2 = a.count(adolzcopy[1])
z3 = a.count(adolzcopy[2])
z4 = a.count(adolzcopy[3]) # 4
if m > 4:
    z5 = a.count(adolzcopy[4])
if m > 5:
    z5 = a.count(adolzcopy[5])
if m > 6:
    z5 = a.count(adolzcopy[6])
if m > 7:
    z5 = a.count(adolzcopy[7])
if m > 8:
    z5 = a.count(adolzcopy[8])
if m > 9:
    z5 = a.count(adolzcopy[9])


if z1 >= 2 or z2 >= 2 or z3 >= 2 or z4 >= 2 or z5 >= 2 or z6 >= 2 or z7 >= 2 or z8 >= 2 or z9 >= 2 or z10 >= 2:
    flag =0
if flag ==0:
    print("Error")
else:
    adolzcopy.sort()
    print(adolzcopy)'''



'''
#copy prefrleno dole 
x1 = a.count(a[0])
x2 = a.count(a[1])
x3 = a.count(a[2])
x4 = a.count(a[3])
#x5 = a.count(a[4])
x6 = a.count(a[5])
x7 = a.count(a[6])
x8 = a.count(a[7])
x9 = a.count(a[8])
x10 = a.count(a[9])
y1 = a.count(a[0])
y2 = a.count(a[1])
y3 = a.count(a[2])
y4 = a.count(a[3])
y5 = a.count(a[4])
y6 = a.count(a[5])
y7 = a.count(a[6])
y8 = a.count(a[7])
y9 = a.count(a[8])
y10 = a.count(a[9])
# ne moze da ostranuva duplikati pred da se spojat listite i istite da gi izvadi od listite i pred uslovot za d>10
if x1 >= 2 or x2 >= 2 or x3 >= 2 or x4 >= 2 or x5 >= 2 or x6 >= 2 or x7 >= 2 or x8 >= 2 or x9 >= 2 or x10 >= 2:
    flag =0
if y1 >= 2 or y2 >= 2 or y3 >= 2 or y4 >= 2 or y5 >= 2 or y6 >= 2 or y7 >= 2 or y8 >= 2 or y9 >= 2 or y10 >= 2:
    flag =0'''
