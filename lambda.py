#def#
def greeting(name) :
    print(f"Hello {name}")
greeting ('nana')

#lambda#
salam = lambda name : print(f"Hello {name}")
salam("anto")
salam ("Budi")

#def#
def addition(angka1, angka2) :
    hasil = angka1 + angka2
    return hasil
angka1 = int(input("Enter first number: "))
angka2 = int(input("Enter second number: "))
add1 = addition(angka1, angka2)
print(f"{angka1} + {angka2} = {add1}")

#lambda#
tambah = lambda angka1, angka2 : angka1 + angka2
print(f"20 + 30 = {tambah(20, 30)}")
kali = lambda angka1, angka2 : angka1 * angka2
print(f"1 * 2 = {kali(1, 2)}")
kurang = lambda angka1, angka2 : angka1 - angka2
print(f"50 - 40 = {kurang(50, 40)}")
bagi = lambda angka1, angka2 : angka1 / angka2
print(f"40 / 2 = {bagi(40, 2)}")
#tambahan buat pembagian (dibagi 0)#
bagi = lambda angka1, angka2 : angka1 / angka2 if angka2 != 0 else "tidak bisa dibagi 0"
print(f"40 / 0 = {bagi(40, 0)}")

#konversi suhu ke fahrenheit, kelvin, dan reamure menggunakan input#
suhu = float(input("masukkan suhu dalam derajar celcius: "))
konversi = input('konversi ke f/k/r: ').lower()
c_to_r = lambda c : (4/5) * c
c_to_f = lambda c : (9/5) * c + 32
c_to_k = lambda c : c + 273.15


if konversi == 'k' :
    print(f"{suhu} derajat celcius = {c_to_k(suhu)} derajat kelvin")
elif konversi == 'f' :
    print(f"{suhu} derajat celcius = {c_to_f(suhu)} derajat fahrenheit")
elif konversi == 'r' :
    print(f"{suhu} derajat celcius = {c_to_r(suhu)} derajat reamure")
