while True:
  c1=int(input('Enter your grade:'))
  c2=int(input('Enter your second grade:'))
  c3=int(input('Enter your third grade:'))

promedio=c1+c2+c3/3

print(("Tu promedio es,", promedio))


if (promedio<6):
  print("you failed")

if (promedio>=6):
  print("you pass")

if (promedio>=9):
  print("you won")