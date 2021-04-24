
a= "uno"
b= "dos"
c= "a+b"
print(c)
print(a+b)

#cadenas de texto
a=14
b=12
c="a+b"
print(a+b)
print(a,"hola", b, '=',c )
print()


h="hola"
i="="


#ala hora de concatenar numero y cadenas de texto es necesario convertir variables a textos
print(str (a), h ,str(b)), i, str(c)
s="KILOMETER"
print(s.lower())
#operaciones con boolean
a=1
b=0
print("a=" ,a,"b=",b)
print("a and b-->",a and b)
print("a or b-->", a or b)

#operadores de incremento
a=23
print("a=23-->",a)
a=a+1
print("a=a+1-->",a)
a+=1
a*=2
print("a*2-->",a)
a/=2
print("a/=2-->",a)
a-=2
print("a-=1-->",a)
a**=2
print("a**=1-->",a)
#trabajo con decimales = decimal
a=4.2
b=2.1
print(a+b)
#estructuras de control
#if:condicion
#for:repeticion
#while:repeticion
edad=10
if edad<0:
    print("menor que cero")
elif edad < 0:
        print("usted es menor de edad")  

#for
nums = [4, 78, 9, 84]
for x in nums:
    print(x)         
 #bucle diccionario
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k in valores:
    print(k)   
 #items
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k, v in valores.items():
    print('k=', k, ', v=', v)

coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e == 7:
        print(e)
        break
#PRACTICAS
a=10
b=20
c=(a+b)
print(a*b)
    