from rich import print
from time import sleep

cores_texto = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;7;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'azulclaro': '\033[1;36m',
    'cinza': '\033[1;37m'
}

cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m',
    'vermelho': '\033[1;41m',
    'verde': '\033[1;42m',
    'amarelo': '\033[1;43m',
    'azul': '\033[1;44m',
    'roxo': '\033[1;45m',
    'azulclaro': '\033[1;46m',
    'cinza': '\033[1;47m'
}

print('-=' * 10)
print('{}|      EcoCAR      |{}'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('=-' * 10)
print()

preco_gasolina = float(input('Qual o preço da Gasolina? '))
preco_etanol = float(input('Qual o preço do Etanol? '))
print()
print('{}CALCULANDO...{}'.format(cores_texto['azul'], cores_texto['limpa']))
sleep(2)
print()


def calculo(preco_gasolina, preco_etanol):
  '''
  Preço Gasolina * 0.7 = Se o valor for menor que o Preço Máximo do Etanol, abasteça com Gasolina!
  Se o valor for maior, abasteça com Etanol
  '''
  if ((preco_gasolina * 0.70) < preco_etanol):
    print('{}Compensa abastecer com Gasolina.{}'.format(cores_texto['vermelho'], cores_texto['limpa']))
  elif ((preco_gasolina * 0.70) > preco_etanol):
    print('{}Compensa abastecer com Etanol.{}'.format(cores_texto['verde'], cores_texto['limpa']))
  else:
    print('São equivalentes, abasteça com qualquer um.')

calculo(preco_gasolina, preco_etanol)