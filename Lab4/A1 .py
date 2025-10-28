import random
import time

L = int(input('Введите количество примеров:'))
total_time = []
counter_answer = 0
for i in range(L):
    print (f'Вопрос {i+1}/{L}')
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    start_time = time.time()
    while True:
        try:
            answer = int(input(f'{a} * {b} = '))
            break
        except ValueError:
            print('Пожалуйста, введите целое число')
    time_spend = time.time() - start_time
    if answer == a * b:
        print('Верно!')
        counter_answer += 1
    else:
        print('Неверно!')
    print(f'Время:', time_spend)
    total_time.append(time_spend)
print("="*50)
print('СТАТИСТИКА')
print('='*50)
print('Общее время:', sum(total_time))
print('Среднее время на вопрос:', sum(total_time) / L)
print(f'Правильных ответов: {counter_answer}/{L}')

print(f'Процент правильных ответов: {(counter_answer/L)*100}%')
