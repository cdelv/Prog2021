def sort_up(x,digitos):
  n = str(x)
  number = []
  #Tener en cuenta los ceros a la izquierda
  while(len(n)<digitos):
    number.append('0')
    

  for i in n:
    number.append(i)
  number = sorted(number, reverse=True)
  return int(''.join(number))

def sort_down(x,digitos):
  n = str(x)
  number = []

  for i in n:
    number.append(i)
  number = sorted(number, reverse=False)
  return int(''.join(number))

def kaprekar_iter(x):

  digitos = len(str(x))
  constantes = [[0],[-1]]
    
  if digitos == 2:
    constantes = [[0],[9, 81, 63, 27, 45]]
  if digitos == 3:
    constantes = [[0,495],[-1]]
  if digitos == 4:
    constantes = [[0,6174],[-1]]
  if digitos == 5:
    constantes = [[0],[82962, 75933, 63954, 61974,74943, 62964, 71973, 83952,53955, 59994]]
  if digitos == 6:
    constantes = [[0,549945, 631764], [420876, 642654, 750843, 840852, 851742, 860832, 862632]]
  if digitos == 7:
    constantes = [[0],[7509843, 9529641, 8719722, 8649432, 7519743, 8429652, 7619733, 8439552]]
  if digitos == 8:
    constantes = [[0,63317664, 97508421],[64308654, 83208762, 86526432, 43208766, 85317642, 75308643, 84308652, 86308632, 86326632, 64326654]]
  if digitos == 9:
    constantes = [[0,864197532,554999445],[554999445, 864197532, 753098643, 762098733, 763197633, 844296552, 863098632, 865296432, 
                                           865395432, 873197622, 874197522, 883098612, 954197541, 964395531, 965296431, 976494321]]
  if digitos > 9:
    print('No conozco las constantes o bucles de kaprekart para '+str(digitos)+' digitos.')
    return None

  iter = 0
  z = x
  ref = 0
  while((z not in constantes[0]) and (z not in constantes[1])):
    z = sort_up(x,digitos) - sort_down(x,digitos)
    x = z
    iter +=1
    if z in constantes[1]:
      ref = 1


  return iter, ref, x

def print_kaprekar(x):
  iter, ref, conv = kaprekar_iter(x)
  string = ''
  if ref == 0:
    string = ' que es una constante.'
  elif ref == 1:
    string =' que es parte de un bucle.'
  print('Numero de iteraciones para que '+str(x)+' converja a un bucle o constante es '+str(iter)+' iteraciones.')
  print(str(x)+' converge a '+str(conv)+string)

def main():
  print_kaprekar(1112)

if __name__ == '__main__':
  main()