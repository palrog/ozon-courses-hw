
import random
deposit = 10000
print ('\nПриветствуем вас в нашем виртуальном казино!\nВаш стартовый депозит: ', deposit, '\n')
while deposit > 0:
    cifra = int(input('Укажите число от 2 до 12 и нажмите Enter для броска кубика\n'))
    kubik = random.randint(2,12)
    if kubik == cifra:
        print('Ваше число: ', cifra, 'На кубике выпало: ', kubik)
        deposit += 1000
        print('Вам повезло! Теперь Ваш депозит:', deposit)
    else:
        print('Ваше число: ', cifra, 'На кубике выпало: ', kubik)
        deposit -= 1000
        print('Повезёт в следующий раз! Теперь Ваш депозит: ', deposit)
print('Увы! Приходите в следующий раз :)')