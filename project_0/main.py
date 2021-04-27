import numpy as np

number = np.random.randint(1, 101)

def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

def game_core_v3(number):
    count = 1
    left = 1
    right = 100
    predict = (left + right) // 2
    while right > left + 1 and number != predict:
        predict = (left + right) // 2
        count += 1
        if number > predict:
            left = predict
        else:
            right = predict
    return(count)

score_game(game_core_v3)


