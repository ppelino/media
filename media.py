nota1 = float(input("Nota1: "))

nota2 = float(input('Nota 2: '))

simulado = float(input('Nota simulado: '))

ac1 = float(input('Nota AC1: '))

ac2 = float(input('Nota AC2: '))


media1 = (nota1+nota2)/2
mediaAC = (ac1+ac2)/2
mediaf = (media1+simulado+mediaAC)/3 

print (mediaf)

if mediaf == 6:
   print("na media")


if mediaf < 6:
   print("abaixo da media")