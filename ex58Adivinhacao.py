from random import randint
computador = randint(0,10)

print('Sou seu computador...')
print('Acabei de pensar em um numero de 0 a 10.')
print('Será que você consegue adivinhar qual foi?')

tentativas = 0
acertou = False

while not acertou:
    palpite = int(input('Qual o seu palpite? '))
    tentativas += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite > computador:
            print('Menos...tente mais uma vez.')
        elif palpite < computador:
            print('Mais...tente mais uma vez')
print('Acertou com {} tentativas!!'.format(tentativas))