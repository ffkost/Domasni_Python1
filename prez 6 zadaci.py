# Zadaca 1 |  Zbir na brooevi vo edna lista   / zadaca

'''lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sumanabroevi_volista(a):
    return sum(a)
a = sumanabroevi_volista(lsita)
print(a)''' # vaka od nekoj od kursot

'''lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sumanabroevi_volista(a): # po moe
    suma = 0
    for i in a:
        suma = suma + int(i)
    return suma
a = sumanabroevi_volista(lista)
print(a)'''
#---------------------------------------------------------------------
'''#Zadaca 2 | funkcija koja ke naoga maksimum od 3 broja
def najgolemodtribr(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
z = najgolemodtribr( 2 ,33, 66)
print(z)'''
#-------------------------------------------------------------------------------------------------------------
'''#Zadaca 4, 3ta nema |  funkcija faktoriel na daden broj  # na cas do cetvrta na 6ti cas
def fakotirijel(a):
    rez = 1
    for i in range(1, a + 1):
        rez = rez * i

    return rez
z = fakotirijel(11)
print(z)'''
#-------------------------------------------------------------------------------------------------------------
'''# Zadaca 5 | od lista od tricifreni broevi gi vraka onie koj se delivi so sumata na nivnite cifri / na cas
def tricif_div_sum_dig(a): # moja
    barani_broevi = []

    for i in a:
        istr = str(i)
        zbir = 0
        for j in istr:
            zbir = zbir + int(j)
        if i % zbir == 0:
            barani_broevi.append(i)

    return barani_broevi

listata = [123, 242, 525, 367, 222, 373, 275, 869, 956, 352, 823, 344, 852, 548]
rezlista = tricif_div_sum_dig(listata)
print(f"Baranata lista:  {rezlista}")'''

'''lista = []

def broevi():
    for i in range(100, 1000):
        s = str(i)
        prv = s[0]
        vtor = s[1]
        tret = s[2]
        suma = int(prv) + int(vtor) + int(tret)
        if i % suma ==0:
            lista.append(i)
        i = int(i)

broevi()
print(lista)'''

#------------------------------------------------------------------------------------------------------------
'''# Zadaca 6 | Nzd na dva broja / na cas

def nzd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
# NZD moja
i1 = 56
i2 = 98
rez = nzd(i1, i2)
print(f"Nzd da {i1} and {i2} is: {rez}")'''

'''def najmal(a,b):
    if a < b:
        return а
    else:
        return b

def NZD(a,b):
    naj = najmal(a,b)  # ovde goren den najmal nema potreba moze naj = min(a,b)
    for i in range(naj, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

a = int(input("Vnesi broj a  "))
b = int(input("Vnesi broj b  "))

print(NZD(a,b))'''

'''#Zadaca 7 | funkcija za kalkulator / na cas
def kalkulator(a, b, c):
    d = 0
    if b == "+":
        d = a + c
        return d
    elif b == "-":
        d = a - c
        return d
    elif b == "/":
        d = a / c
        return d
    elif b == "*":
        d = a * c
        return d
    else:
        return "Greska"

rez = kalkulator( 2,"*",5)
print(rez)'''


'''# Zadaca 8 | Funkcii za diametar, plostina i parametar na krug

def diametar(a):

    return a*2
def parametarkrug(b):
    pi = 3.14159
    rez = 2*b*pi
    return rez
def areakrug(c):
    pi = 3.14159
    rez = pi*c*c
    return rez

def funkkombinacija(r):
    rez1 = diametar(r)
    rez2 = parametarkrug(r)
    rez3 = areakrug(r)
    return rez1, rez2, rez3


radius = 5
a,b,c = funkkombinacija(5)

print(f"Diametr: {a}")
print(f"Parametar : {b}")
print(f"Area: {c}")'''

'''#Zadaca 9 |

def presmetka():
    rez = []
    broj =0
    for i in range(1000,10000):
        istr = str(i)

        prvi2 = int(istr[:2])
        posledni2 = int(istr[2:])

        suma = prvi2 + posledni2

        if suma != 0 and i % suma ==0:
            rez.append(i)
            broj = broj + 1
    return rez, broj

a,b =presmetka()
print(f"Broevite koj go ispolnuvaat praviloto: {a} ")
print(f"Imame {b} takvi na broj")'''

# Zadaca 10 | Kako argument prima ima i plata na vraboteniot i gi ispecatuva so default plata od 9000

#version 1

'''def show_employee(ime, plata = 9000):
    print(f" Ime {ime}, Salary: {plata} ")

show_employee("Filip", 50000)
show_employee("Johnny")'''

'''def show_employee(vlez):
    ime = vlez.get("ime") # ako ovde e eime a dole pred filip pisuvas drugo dava none
    plata = vlez.get("plata",9000)
    print(f"Ime: {ime}, Plata : {plata}")

show_employee({"ime": "Filip", "plata": 50000})
show_employee({"ime":"Pande"})'''

'''#Zadaca 11 | prima 2 broja  i ke presmeta zbir i razlika od funk da se vrata dvete vrednosti

def zbir_razlika1(a,b): #tuple
    zbir = a + b
    razlika = a - b
    return zbir, razlika

def zbir_razlika2(a,b):  #dictionary
    zbir = a + b
    razlika = a - b
    return { "suma":zbir , "razlika": razlika}

def zbir_razlika3(a, b):   # return lista
    zbir = a + b
    razlika = a - b
    return [zbir, razlika]

def zbir_razlika4(a, b): # return string
    zbir = a + b
    razlika = a - b
    return f"Sumata e {zbir} \nRazlikata e {razlika}"

def zbir_razlika5(a, b): # vraka poveke promenlivi
    zbir = a + b
    razlika = a - b
    return zbir, razlika

rezultat1 = zbir_razlika1(10 ,5)
rezultat2 = zbir_razlika2(10 ,5)
rezultat3 = zbir_razlika3(10, 5)
rezultat4 = zbir_razlika4(10, 5)
rez5zbir, rez5razlika = zbir_razlika5(10, 5)
print(rezultat1)
print(rezultat2)
print(rezultat3)
print(rezultat4)
print("\n")
print(rez5zbir)
print(rez5razlika)
print("\n")'''

'''#Zadaca 12 | Od lsita na  vlez da go najde najgolemiot najmaliot i average na site elementi

def funkcija1(a):
    if not all(isinstance(n, (int, float)) for n in a): # !!!
        return "Error: All elements must be ibers."


    min = a[0]
    maks = a[0]
    vkupno = 0

    for i in a:
        if i < min:
            min = i
        if i > maks:
            maks = i
        vkupno += i

    average = vkupno / len(a)
    return min, maks, average  # return tuple
    #return {'min': min, 'max': maks, 'average': average} # return dictionary
    #return [min, maks, average] # return lista
    #return f"The minimum is {min}, the maximum is {max}, and the average is {average:.2f}"
    #return min, maks, average # multiple variables

# Example usage
rez = funkcija1([1, 2, 3, 4, 5])
print(rez)  # Output: (1, 5, 3.0)

rez = funkcija1([1, 2, 'a', 4, 5])
print(rez)  # Output: Error: All elements must be ibers.

#mi,ma,avg = funkcija1([1, 2, 3, 4, 5])  # za vrakane na multiple variables
#print(f"Min: {mi}, Max: {ma}, Avg: {avg:.2f}")  # Output: Min: 1, Max: 5, Avg: 3.00'''


#-------------------------------------------------------------------------------------------------
'''# Zadaca 13 | Finkcija koja presmetuva dali odreden broj pripaga vo daden rang

def funkcija1():

    start = float(input("Vnesi go pocetokot  "))
    kraj = float(input("Vnesi go krajot      "))
    broj = float(input(f"Vnesi go brojot za proverka dali e vo intervalot od {start} do {kraj}"))

    if start <= broj and broj <= kraj:
        return True, broj
        #return { "vorang": True, "broj": broj }
        #return [True, number]
        #return f"{number} is in range."
    else:
        return False, broj
        #return {"vorang": True, "broj": broj}
        #return [False, number]
        #return f"{number} is not in range."

rez = funkcija1()
print(rez)'''


#--------------------------------------------------------------------------------------------
'''# Zadaca 14 | lista od elementi kako argument i ke vrati nova uniqantna lista

def bez_duplikati(a):
    novalista = []
    for i in a:
        if i not in novalista:
            novalista.append(i)
    return novalista # vraka lista
    #return (novalista)
    #return tuple(novalista)
    #return {"unikatni elementi": novalista }
    #return f"Unikatni elementi se: {novalista}"

# Example usage
rez = bez_duplikati([1, 2, 2,2,2 ,3, 'a', 'a', 'b'])
print(rez)  # Output: [1, 2, 3, 'a', 'b']'''

#-----------------------------------------------------------------------------------------------
'''# Zadaca 15 | na vlez prima lista na izlez dava lista so neparni broevi

def neparni_int_broevi(a):
    neparni = []
    for i in a:
        if isinstance(i, int) and i % 2 != 0:
            neparni.append(i)
    return neparni
    #return set(neparni)
    #return tuple(neparni)
    #return {'Neparni broevi: ': neparni}
    #return f"Neparni broevi:  {neparni}"

rez = neparni_int_broevi([1, 2, 3, 4, 'a', 5.5, 7])
print(rez)'''
#------------------------------------------------------------------------------------------------------------
#Zadaca 16 | Dali daden vlezen string e pangram ili ne (gi sodzri site bukvi od azbukata barem ednas)

'''def dali_e_pangram(a):
    azbuka = set("abcdefghijklmnopqrstuvwxyz")
    lista1 = set(a.lower())
    #return azbuka.issubset(a)
    #return {'Dalie e pangram ': azbuka.issubset(a)} # dictionary
    #return azbuka.issubset(lista1), a  # ! ova e dobro
    #return [azbuka.issubset(lista1), a]

    #if azbuka.issubset(lista1):
        #return f"'{a}' E pangram."
    #else:
        #return f"'{a}' NE E pangram."
    


rez = dali_e_pangram("The quick brown fox jumps over the lazy dog")
print(rez)  # Output: True

rez = dali_e_pangram("Hello World")
print(rez)  # Output: False'''



'''def dali_e_pangram3(a):
    azbuka = 'abcdefghijklmnopqrstuvwxyz'
    letter_count = {letter: 0 for letter in azbuka}
    for i in a.lower():
        if i in letter_count:
            letter_count[i] += 1
    return all(count > 0 for count in letter_count.values()) # ne ja svakam'''

'''def dali_e_pangram4(a):
    azbuka = list('abcdefghijklmnopqrstuvwxyz')
    for i in a.lower():
        if i in azbuka:
            azbuka.remove(i)

    return len(azbuka) == 0'''

'''def is_pangram(input_string):
    alphabet_flags = [False] * 26
    for char in input_string.lower():
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            alphabet_flags[index] = True
    return all(alphabet_flags)'''

'''def is_pangram(input_string):
    input_set = {char for char in input_string.lower() if char.isalpha()}
    return len(input_set) == 26

# Example usage
result = is_pangram("The quick brown fox jumps over the lazy dog")
print(result)  # Output: True

result = is_pangram("Hello World")
print(result)  # Output: False'''

'''# Example usage
result = is_pangram("The quick brown fox jumps over the lazy dog")
print(result)  # Output: True

result = is_pangram("Hello World")
print(result)  # Output: False



rez = dali_e_pangram4("The quick brown fox jumps over the lazy dog")
print(rez)  # Output: True

rez = dali_e_pangram4("Hello World")
print(rez)  # Output: False'''
#--------------------------------------------------------------------------------------------------------
# Zadaca 17 | Vo edna recenica ke gi izbroi samoglaskite i soglaskite

'''def funkcija1(a):
    samoglaski = "aeiou"
    brsamoglaski = 0
    brsoglaski = 0
    #counts = {"samoglaski": 0,"soglaski":0} # dictinaries

    for i in a.lower():
        if i.isalpha():
            if i in samoglaski:
                brsamoglaski += 1
                #counts["samoglaski"] += 1 #dictionary
            else:
                brsoglaski += 1
                #counts["soglaski"] += 1 #dictionary
    #return brsamoglaski,brsoglaski # touple
    #return counts #dictionaries
    #return [brsamoglaski, brsoglaski]  #list
    #return f"Vowels: {brsamoglaski}, Consonants: {brsoglaski}"


rez = funkcija1("dsajdzioxcweiytwqtowtowtoetwqemkfnwevwbfiweytweqfhs fsda fhsau dfhu isadhf usad hfu as342 ")
print(rez)'''

'''#Zadaca 17.1 | sega na izlez seko jzbor kolku samoglaski i soglaski ima

def funkcija7(a):
    samoglaski = 'aeiou'
    words = a.lower().split()
    counts = {}

    for i in words:
        brsamoglaski = 0
        brsoglaski = 0
        for j in i:
            if j.isalpha():
                if j in samoglaski:
                    brsamoglaski += 1
                else:
                    brsoglaski += 1
        counts[i] = {'samoglaski': brsamoglaski, 'soglaski': brsoglaski}

    return counts


# Example usage
rez = funkcija7("The quick brown fox jumps over the lazy dog")
print(rez)
# Output: {'the': {'vowels': 1, 'consonants': 2}, 'quick': {'vowels': 2, 'consonants': 3}, ...}'''



