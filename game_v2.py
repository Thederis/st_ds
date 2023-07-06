"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

def random_predict(namber: int=1) -> int:
    """Рандомно угадываем число

    Args:
        namber (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Предполагаемое число
        if namber == predict_number:
            break # Выход из числа
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения  колличества попыток
    np.random.seed(1) # фиксируем сид для производимости
    random_arry = np.random.randint(1, 101, size = 1000) # Загадали список чисел
    for namber in random_arry:
        count_ls.append(random_predict(namber))
    score = int(np.mean(count_ls)) # Находим среднее колличество попыток
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток.")
    return score
# RUN
if __name__ == '__main__':
    score_game(random_predict)