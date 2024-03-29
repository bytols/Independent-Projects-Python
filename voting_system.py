

nulo = antonio = jose = maria = branco = total = 0

while True:
   print(f'\n[1] Antonio\n'
         f'[2] José\n'
         f'[3] Maria\n'
         f'[4] BRANCO\n'
         f'[ ] NULO')
   voto = int(input('Seu voto [0 para terminar]: '))
   if voto != 0:
      total += 1
   if voto not in range(5):
      nulo += 1
   elif voto == 1:
      antonio += 1
   elif voto == 2:
      jose += 1
   elif voto == 3:
      maria += 1
   elif voto == 4:
      branco += 1
   elif voto == 0:
      print('Votação encerrada!\n')
      break

print('=' * 22)
print('RESULTADO DAS ELEIÇÕES')
print('=' * 22)
print(f'Candidato Antonio obteve {antonio} votos!\n'
      f'Candidato José obteve {jose} votos!\n'
      f'Candidata Maria obteve {maria} votos!\n'
      f'Votos em Branco = {branco}\n'
      f'Votos nulos = {nulo}\n\n'
      f'Eleitores que compareceram às urnas = {total}')

vencedor = max(antonio,jose,maria)
if (antonio == jose and antonio == vencedor) or  \
   (antonio == maria and antonio == vencedor) or \
   (jose == maria and jose ==vencedor):
   print('VOTAÇÃO EM SEGUNDO TURNO')

# Poderia ser ((antonio+jose+maria)-min(antonio,jose,maria))/max(antonio,jose,maria)==2