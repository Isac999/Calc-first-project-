
op=0
repet=op
while repet==0 or repet>5:
  print('--------------Calculadora Simples---------------')
  print('Selecione a operação')
  print('1-Adição')
  print('2-Subtração')
  print('3-Multiplicação')
  print('4-Divisão')
  print('5-Raiz quadrada')
  op=int(input('Operação selecionada: '))
  if op==1 or op==2 or op==3 or op==4 or op==5: 
    if op==5:
      import math
      valor=int(input('Digite um número: '))
      raiz= math.sqrt(valor)
      print('A raiz quadrada de {} é {}'.format(valor,raiz))
    else:
      print('Selecione o número de elementos (no máximo 5 algarismos)')
      element=int(input('Número de elementos: '))
      if element==2 or element==3 or element==4 or element==5:  
        if element==2: 
          n01=float(input('Número 1: '))
          n02=float(input('Número 2: '))
          if op==1: 
            nfinal=n01+n02
            print('A soma de {} + {} = {}'.format(n01,n02,nfinal))
          elif op==2: 
            nfinal=n01-n02
            print('A subtração de {} - {} = {}'.format(n01,n02,nfinal))
          elif op==3: 
            nfinal=n01*n02
            print('A multiplicação de {} * {} = {}'.format(n01,n02,nfinal))
          elif op==4: 
            nfinal=n01/n02
            print('A divisão de {} / {} = {}'.format(n01,n02,nfinal))
        if element==3:
          n01=float(input('Número 1: '))
          n02=float(input('Número 2: '))
          n03=float(input('Número 3: '))
          if op==1: 
            nfinal=n01+n02+n03
            print('A soma de {} + {} + {} = {}'.format(n01,n02,n03,nfinal))
          elif op==2: 
            nfinal=n01-n02-n03
            print('A subtração de {} - {} - {} = {}'.format(n01,n02,n03,nfinal))
          elif op==3: 
            nfinal=n01*n02*n03
            print('A multiplicação de {} * {} * {} = {}'.format(n01,n02,n03,nfinal))
          elif op==4: 
            nfinal=n01/n02/n03
            print('A divisão de {} / {} / {} = {}'.format(n01,n02,n03,nfinal))
        if element==4:
          n01=float(input('Número 1: '))
          n02=float(input('Número 2: '))
          n03=float(input('Número 3: '))
          n04=float(input('Número 4: '))
          if op==1: 
            nfinal=n01+n02+n03+n04
            print('A soma de {} + {} + {} + {} = {}'.format(n01,n02,n03,n04,nfinal))
          elif op==2: 
            nfinal=n01-n02-n03-n04
            print('A subtração de {} - {} - {} - {} = {}'.format(n01,n02,n03,n04,nfinal))
          elif op==3: 
            nfinal=n01*n02*n03*n04
            print('A multiplicação de {} * {} * {} * {} = {}'.format(n01,n02,n03,n04,nfinal))
          elif op==4: 
            nfinal=n01/n02/n03/n04
            print('A divisão de {} / {} / {} / {} = {}'.format(n01,n02,n03,n04,nfinal))
        if element==5:
          n01=float(input('Número 1: '))
          n02=float(input('Número 2: '))
          n03=float(input('Número 3: '))
          n04=float(input('Número 4: '))
          n05=float(input('Número 5: '))
          if op==1: 
            nfinal=n01+n02+n03+n04+n05
            print('A soma de {} + {} + {} + {} + {} = {}'.format(n01,n02,n03,n04,n05,nfinal))
          elif op==2: 
            nfinal=n01-n02-n03-n04-n05
            print('A subtração de {} - {} - {} - {} - {} = {}'.format(n01,n02,n03,n04,n05,nfinal))
          elif op==3: 
            nfinal=n01*n02*n03*n04*n05
            print('A multiplicação de {} * {} * {} * {} * {} = {}'.format(n01,n02,n03,n04,n05,nfinal))
          elif op==4: 
            nfinal=n01/n02/n03/n04/n05
            print('A divisão de {} / {} / {} / {} / {} = {}'.format(n01,n02,n03,n04,n05,nfinal))
      else: print('Quantidade de elementos inexistente!')
  else: print('Operação inexistente!')
  print('Feito por Isac o/')
  print('------------------------------------------------')