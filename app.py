''''print('===KALKULATOR SEDERHANA===')
a=float(input('masukkan angka-1:'))
b=float(input('masukkan angka-2:'))
print(a,'+',b,'=',a+b)
print(a,'-',b,'=',a-b)
print(a,'dikali',b,'=',a*b)
print(a,'dibagi',b,'=',a/b)
print(a,'dibagi',b,'sisa baginya=',a%b)
print(a,'pangkat',b,'=',a**b)
print(a,'dibagi',b,'hasilnya (dalam bilangan bulat ke bawah)=',a//b)'''


'''print('===MEMBANDINGKAN 2 BILANGAN===')
a=float(input('masukkan angka-1:'))
b=float(input('masukkan angka-2:'))
if a>b:
    print(a,'lebih dari',b)
elif a<b:
    print(a,'kurang dari',b)
else :
    print(a,'sama dengan',b)'''


print('===MENENTUKAN BILANGAN POSITIF NEGATIF ATAU NOL===')
a=float (input('masukkan angka :'))
if a<0:
    print(a,'merupakan bilangan negatif')
elif a>0:
    print(a,'merupakan bilangan positif')
else :
    print(a, 'merupakan bilangan nol')
