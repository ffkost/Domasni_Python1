'''
#primer 1
i = 0
word = "Hello"
while i < len(word):
    if word[i] == "e" or word[i] =="o":
        i += 1
        continue
    print("Returned letter",word[i])
    i += 1'''


'''
# primer 2
n = int(input("Enter a number: "))
while n != 0:
    n = int(input("Enter zero to quit: "))'''

'''
#primer 3
p = 5
sum = 0
count = 0

while p >0:
    count += 1
    f = int(input("Enter the number:  "))
    sum =sum + f
    p = p-1
average = sum/count
print("Average of given Number:", average)'''
#-----------------------------------------------------------------------------------------------------------------

'''
#zadaca 1 | broievi od a do b delivi so c da bidat ispecateni, (a,b,c) se vnesuvaat od tastatura 
# na cas resena

print("Vnesi broevi vo format (a,b,c) :")
a = int(input("a - ? :"))
b = int(input("b - ? :"))
c = int(input("c - ? :"))
lista = []
count = 0
print(f"Delivi so {c} se: ")
for i in range(a,b+1):
    #print(i)
    if i % c == 0:
        count = count + 1
        lista.append(i)
print(list)
d = len(lista) # moze vo ciklusot da ima brojac promenliva
print(d)
print(f"Postojat {d} broevi delivi so {c}")'''


'''
zadaca 2 | factoriel na daden broj / na cas
a = int(input("Presmetka na fakoriel od brojot?:   "))
j =1
for i in range(1, a+1):
    j = j*i
    
print(f"Faktoriel na {a} e: {j}")'''

'''# drug kako ja resil
broj = int(input("Vnesi broj  "))
faktoriel = broj
if broj < 0:
    print("Brojot mora da bide pozitiven ")
elif broj ==0:
    print("Faktoriel na 0 e 1")
else:
    for i in range(broj - 1):
        faktoriel = faktoriel * (broj-1)
        broj = broj -1
print(faktoriel)'''

#zadaca 3 | vo interval ispecati gi site prosti broevi / na cas
'''# moj nacin
print("Vnesi go n (1,n)")
a = int(input("n:   "))

lista = []
for i in range(1, a+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
            lista.append(i)
print(lista)
d = len(lista)
print(d)'''

'''n = int(input("Vnesi broj n: "))
print(f"Простите броеви од 1 до {n} се:")
# Итерација низ сите броеви од 1 до n
for num in range(1, n + 1):
    if num < 2:
        continue
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1): # ???

        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)'''

'''#zadaca 4 | ispecati sema na broevi do  n - vnesen broj vo oblik na piramida
# Function to demonstrate printing pattern of numbers
# na cas
n = int(input("Vnesi ja goleminata na osnovata na peramidata")) # moe resenie
for i in range(0, n):
    a = 1

    for j in range(0, i + 1):
        # printing number
        print(a, end=" ")

            # incrementing number at each column
        a = a + 1
    print("")'''

'''n = int(input("Vnesi broj"))
text = ""
for i in range(1, n+1):
    text = text + str(i) + " "
    print(text)'''

'''# Внесување на бројот n од корисникот
n = int(input("Внеси број n: "))

# Итерација низ секој ред од 1 до n
for i in range(1, n + 1):
    # Во секој ред печатиме броеви од 1 до i
    for j in range(1, i + 1):
        print(j, end=" ")
    # По секој ред додаваме нова линија
    print()'''



'''# Zadaca 5 | Prevrtena verzija na vnesen broj  / na cas
a = int(input("Vnesi broj koj ke se ispecati vo negovaga (prevrtena verzija) ")) # moj kod
b = 0
while a > 0:
    b = b * 10
    b = b + a % 10
    a = a // 10

print (b)'''


'''n = input("Vnesi broj: ")  # od petar
l = len(n)
broj = ""
for i in range(l-1, -1,-1): # oti l e dolzina pa zapocnuva od l-1 , do stop 0 ama neli -1, so -1 ikrement
    broj = broj + n[i]
broj = int(broj)
print(broj)'''

'''broj = input("Vnesi broj")
obraten = broj[::-1]
print(obraten)'''




'''# Zadaca 6 kolku broevi vo daden interval site cifri se parni broevi / na cas
# na petar !
m = int(input("Enter the start of range: "))
n = int(input("Enter the end of range: "))
broj_na_parni_broevi = 0
parni_broevi = []

for i in range(m, n + 1):
    broj = str(i)
    lenght = len(broj)
    paren = True
    for j in range(0, lenght):
        if int(broj[j]) % 2 != 0:
            paren = False
    if paren:
        broj_na_parni_broevi = broj_na_parni_broevi + 1
        parni_broevi.append(i)
if broj_na_parni_broevi >0:
    print(f"Broj na parni broevi: {broj_na_parni_broevi}")
    print(f"Parnite broevi se: {parni_broevi}")
else:
    print("Nema broevi kade sekoja cifra e paren broj")'''



'''#zadaca 7 | od kuceski godini vo covecki godini
#1 - 10.5 2-21
age = int(input("Vnesete kolku godini e kuceto "))
human_age = 1
if age > 0 and age <= 1:
    human_age = 10.5
    print(f" {human_age} Covecki godini")

elif age > 1 and age <= 2:
    human_age = 21
    print(f" {human_age} Covecki godini")
else:
    human_age = 21
    for i in range(3, age+1):
        human_age = human_age + 4

    print(f" {human_age} Covecki godini")'''




'''
#zadaca 8 | n vnese od tasatura gi printa site broevi vi interval (1,n)
#ako e deliv so 3 printa #tri, deliv so 5 - #pet, deliv so 3 i 5 - #tripet
# na cas resena ja davale na intervju

print("Interval (1,n)")
a = int(input("Vnesete go n "))

for i in range(1,a+1):
    if i%3 ==0 and i%5 == 0:
        print(f"{i} - #TriPet")
    elif i%3 == 0:
        print(f"{i} - #Tri")
    elif i%5 == 0:
        print(f"{i} - #Pet")
    else:
        print(i)'''

'''#zadaca 9 | stringovi od lista vo lowercase

print("Dodavaj elementi vo listata q za kraj")
lista = []
while True:
    a=input("Vnesi broj ili nula za kraj")
    if a == "q":
        break
    else:
        x = a.lower()
        lista.append(x)

print(lista)'''

'''#zadaca 10 | string na vlez da izbroi kolku bukvi i broevi se vneseni / na cas

a = input("Vnesi string | kolku bukvi i broevi sodrzi --> ")
br1 = 0
br2 = 0
for i in a:
    if i.isalpha() == True:
        br1 = br1 +1
    if i.isdecimal() == True:
        br2 = br2 +1
print(f" Brojot na bukvi e {br1} brojot na cifri e {br2}")'''


'''
#zadaca 11 | tablica za mnozene
a = int(input("Broj za tablica za mnozene: "))
if a > 0 and a < 11:
    for i in range(1, 11):
        print(a, 'x', i, '=', a*i)'''

'''#zadaca 12 | go printa kvadratot na site broevi od 1 do 20
a = 1
for i in range (1,21):
    a = i**2
    print(f"kvadratot na brojot {i} e {a} ") '''

'''#zadaca 13 | string na vlez na output karakteri na neparni pozicii
a = input("Vnesi string")
print(f"Originalniot string: {a}")
b = len(a)
print(b)
lista1 = []
lista2 = []

for i in range(1,b,2):
    lista1.append(a[i])
for i in range(0,b,2):
    lista2.append(a[i])
print(lista1)
print(lista2)'''

'''#zadaca 14 | kolku pati daden zbor se sozdrzi vo edna recenica 

print("Vnesi recenica:")
a = input("   ")
print("Vnesi go zborot")
b = input("   ")

c =a.count(b)
print(c)'''

'''#zadaca15 | fibinoci za vlez

n = int(input("Vnesi broj za....:  "))
a = 1
b = 1

print(" n = 0 | ____ 0")
print(" n = 1 | ____ 1")
print(" n = 2 | ____ 1")


for i in range(3, n+1):
    c = a + b
    a=b
    b=c
    print(f" n = {i} | ____ {c}")'''

'''#zadaca 16 | kolku cifri ima vnesen broj
a = int(input("Vnesi broj"))
print(a)
b=str(a)
c=len(b)
print(c)
d = float(a)
brojpati = 0
for i in range(0,c):
    d = d/10
    brojpati = brojpati + 1
print(brojpati)'''

'''#zadaca 17 | y = x^n  n i y se vnesuvaat od tastatura
print("y= x^n")
a = int(input("x:   "))
b = int(input("n:   "))
c = a
for i in range(1,b):
    c = c * a

print(c)'''

'''#zadaca 19 | Zbir na cifri za daden broj
a = int(input("Vnesi broj"))
suma = 0

while a != 0:
    suma = suma + (a % 10)
    a = a//10
print(suma)'''

'''
# zadaca 20 | najmal blag broj od interval (m,n) # resena

print("Vnesi go intervalot (a,b) ")
m = int(input("m:    "))
n = int(input("n:    "))
rez = None
for i in range(m, n + 1):
    siteparni = True
    a = str(i)
    for j in a:
        if int(a) % 2 != 0:
            siteparni = False
            break

    if siteparni:
        rez = i
        break

if rez is None:
    print(f"Ne postoi broj so parni cifri vo intervalot ({m}, {n}) ")
else:
    print(f" Najmaliot broj so koj e sostaven od samo parni cifri e {rez} vo intervalot ({m}, {n}) ")'''


'''# Zadaca 21 | "interesen" broj e kade negovito obraten broj e deliv so brojot na negovite cifri 
# Da se najde najgolemiot vakov broj vo intervalot 9 - n, n e vnesen od tastatura

n = int(input("Vnesi broj pogolem od 9:     "))

if n <= 9:
    print("Brojot ne e validen")
else:
    rez = None

    for i in range(n, 9, -1):

        a = str(i)
        obraten_brojstr = a[::-1]
        obraten_broj = int(obraten_brojstr)
        dolzbr = len(a)

        if obraten_broj % dolzbr ==0:
            rez = i
            break

    if rez is None:
        print(f"Ne postoi takov broj vo intervalot (9 - {n})")
    else:
        print(f"Najgolemiot broj vo interval (9 - {n})  e brojot {i}")'''


'''# Zadaca 22 | Na vlez n, vo interval 0 do n, da najde broj cij zbir na negovi deliteli e najgolem

n = int(input("Vnesi go n (0-n)   "))

makssuma = 0
baranbroj = 0

for i in range (0, n+1):
    delsuma = 0
    for j in range(1, i): # do n-1 nemoze vo sumata samiot broj da postoi
        if i % j == 0:
            delsuma = delsuma + i

    if delsuma > makssuma:
        makssuma = delsuma
        baranbroj = i

print(f" Brojojt {baranbroj} e  broj cija suma na deliteli e najgolema ({makssuma})")'''

'''#Zadaca 23 | Korisnik vnesuva z , parovi (a,b) se dodeka (0,0) e vneseno
# kolku pati brojot z == a + b i kolkav procent od vnesenite parovi se takvi broevi

z = int(input("Vnesi intiger z:     "))
print("Vnesuvaj parovi (a,b) za kraj vnesi (0,0)")
parsuma_ednakvana_z = 0
brparovi = 0
procent = 0


while True:
    a = int(input("Vnesi a "))
    b = int(input("Vnesi b "))
    if a == 0 and b ==0:
        break
    print("Vo while ")
    brparovi = brparovi + 1
    suma = a+b
    #print(suma)
    #print(z)
    if suma == z:
        #print("Vnatre sum")
        parsuma_ednakvana_z = parsuma_ednakvana_z + 1
        print(parsuma_ednakvana_z)
    suma = 0
#print(parsuma_ednakvana_z)
#print(brparovi)
procent = (parsuma_ednakvana_z/brparovi)*100
print(procent)
print(f"Broj na parovi so suma ednakva na {z} e: {brparovi} so procentualna zastapenost od {procent:.2f}")'''

#

























