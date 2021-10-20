###########################################
# Carlos Andres del Valle Urberuaga
#
#Este codigo incluye las dos modificaciones
###########################################
from random import random
x=int(100*random())
print('Adivina un numero del 0 al 100\n')
mode='a'
while(mode not in ['y','n']):
  mode = input('Quieres infinitos intentos?, y para si, n para no. ')
  if(mode not in ['y','n']):
    print('tu respuesta no es valida, intentalo de nuevo.')

if(mode=='n'):
  ni=int(input('Cuantos itentos quieres? '))
  # inicia delclaración de control iterativo
  flag=True # =NO ADIVINÓ. Cuando <<buscamos>> algo podemo usar un flag
  i=0
  while i<ni :
    print('Intento ',i+1)
    y=int(input('Escribe tu numero: '))
    if x==y:
      print('Felicitaciones. Adivinaste ',x)
      flag=False
      break
    else:
      if(x<y):
        hint='Tu numero es muy grande'
      else:
        hint = 'Tu numero es muy pequeño'
      print('No adivinaste.', hint)
    i=i+1
  #fin de control iterativo
  if flag:
    print('Lo siento no adivinó. Mi numero es',x)

else:
  flag=True # =NO ADIVINÓ. Cuando <<buscamos>> algo podemo usar un flag
  i=0
  while True:
    print('Intento ',i+1)
    y=int(input('Escribe tu numero: '))
    if x==y:
      print('Felicitaciones. Adivinaste ',x)
      flag=False
      break
    else:
      if(x<y):
        hint='Tu numero es muy grande'
      else:
        hint = 'Tu numero es muy pequeño'
      print('No adivinaste.', hint)
    i=i+1
  #fin de control iterativo
  if flag:
    print('Lo siento no adivinó. Mi numero es',x)
