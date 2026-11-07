import numpy as np
import matplotlib.pyplot as plt

def add_vectors(v1, v2):
    '''Adds two 1D vectors element-wise.
    Args: v1 (np.array), v2 (np.array)
    Returns: np.array (sum of vectors)
    '''
    if len(v1) != len(v2):
            raise ValueError(f"Векторы должны иметь одинаковую длину. Получено: {len(v1)} и {len(v2)}")
    return v1 + v2
def scalar_multiply(scalar, v):  # Функция умножение вектора на скаляр
    """Multiplies a scalar by a 1D vector.
    Args: scalar (float or int), v (np.array)
    Returns: np.array (scaled vector)
    """
    return scalar * v
def calculate_dot_product(v1, v2):
    '''Calculates dot product of two 1D vectors.
    Args: v1 (np.array), v2 (np.array)
    Returns: float (dot product)
    '''
    if len(v1) != len(v2):
        raise ValueError(f"Векторы должны иметь одинаковую длину. Получено: {len(v1)} и {len(v2)}")
    return np.dot(v1, v2)
def get_magnitude(v):
    """Calculates the magnitude (length) of a 1D vector.
    Args: v (np.array)
    Returns: float (magnitude of the vector)
    """
    return np.linalg.norm(v)
def visualize_projection(v1, v2):
    '''Visual projection two 1D vectors
    Args: v1 (np.array), v2 (np.array)
    Returns: visual plot
    '''
    fig, ax = plt.subplots()
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue')
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red')
    scalar_proj = calculate_dot_product(v1, v2) / calculate_dot_product(v2, v2)
    v1_proj_on_v2 = scalar_proj * v2
    ax.quiver(0, 0, v1_proj_on_v2[0], v1_proj_on_v2[1], angles='xy', scale_units='xy', scale=1, color='green', linewidth=3, label='Проекция v1 на v2')
    ax.plot([v1[0], v1_proj_on_v2[0]], [v1[1], v1_proj_on_v2[1]], color='gray', linestyle=':', linewidth=1, label='Перпендикуляр')
    ax.set_xlim()
    ax.set_ylim()
    ax.grid(True)
    ax.legend()
    plt.show()
if __name__ == "__main__":
    print('==Проверка работы калькулятора==')
    v1 = np.array([3, 4])
    v2 = np.array([1, 2])
    print(add_vectors(v1, v2))
    print(scalar_multiply(2, v1))
    print(calculate_dot_product(v1, v2))
    print(get_magnitude(v1))
    print("=== Запуск Векторного калькулятора ===")
    while True:#Цикл с выходом когда пожелает пользователь
        print('1.Сложение покомпонентно векторов')
        print("2.Умножение вектора на скаляр")
        print("3.Cкалярное произведение")
        print("4.Длина вектора (magnitude)")
        print("5.Визуализация графика проекции векторов")
        print("0.Выход")#То самое желание, которое закончит бесконечный цикл
        try:
            operation = int(input('Введите операцию от 0-5: '))
        except ValueError:
            print("Ошибка: введите число от 0 до 5")
            continue  # вернуться к началу цикла
        if operation == 0:#Проверка на выход, ели True, цикл завершён
            print("Калькулятор закрыт! Спасибо")
            break
        if 1 <= operation <= 5:#Проверяем диапазон ввода, если диапазон True, то запускаем цикл по просчёту
            try:
                num_1 = list(map(float, input("Введите первый вектор: ").split()))
                num_2 = list(map(float, input("Введите второй вектор: ").split()))
            except ValueError:
                print("Ошибка: введите только числа, разделённые пробелами")
                continue  # вернуться к началу цикла
            v1 = np.array(num_1)
            v2 = np.array(num_2)
            if operation == 1:
                print(f'Результат {add_vectors(v1, v2)}')
            elif operation == 2:
                scalar = int(input('Введите скаляр: '))
                print(f'Результат c первым вектором {scalar_multiply(scalar, v1)} \n Результат со вторым вектором {scalar_multiply(scalar, v2)}')
            elif operation == 3:
                print(f'Результат {calculate_dot_product(v1, v2)}')
            elif operation == 4:
                print(f'Длина вектора №1 = {get_magnitude(v1):.2f}')
                print(f'Длина вектора №2 = {get_magnitude(v2):.2f}')
            elif operation == 5:
                visualize_projection(v1, v2)
        else:#Если пользователь ввёл цифру вышедшую из диапазона, при этом цикл не завершается
            print(f'Некорректный ввод, попробуйте снова')