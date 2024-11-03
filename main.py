import matplotlib.pyplot as plt
import random
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Создаем главное окно
root = tk.Tk()
root.title("Triangle")
root.geometry("700x600")  # Устанавливаем начальное разрешение окна
root.configure(bg='black')  # Устанавливаем черный фон для окна

# Координаты исходных точек треугольника
top_point = (0.5, 1)
left_point = (0, 0)
right_point = (1, 0)
center_point = ((top_point[0] + left_point[0] + right_point[0]) / 3,
                (top_point[1] + left_point[1] + right_point[1]) / 3)

# Создание списка точек для отрисовки
points = [center_point]

# Количество итераций
iterations = 5000

# Создание графика
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')

# Настройка графика
ax.set_facecolor('black')
ax.axis('off')

# Функция для обновления графика
def update_plot(step):
    # Выбираем случайное число от 1 до 6
    roll = random.randint(1, 6)
    current_point = points[-1]

    # Вычисляем новую точку в зависимости от результата броска
    if roll in [1, 2]:  # Вверхняя точка
        new_point = ((current_point[0] + top_point[0]) / 2,
                     (current_point[1] + top_point[1]) / 2)
    elif roll in [3, 4]:  # Левая точка
        new_point = ((current_point[0] + left_point[0]) / 2,
                     (current_point[1] + left_point[1]) / 2)
    else:  # Правая точка
        new_point = ((current_point[0] + right_point[0]) / 2,
                     (current_point[1] + right_point[1]) / 2)

    points.append(new_point)

    # Обновляем график
    ax.clear()
    ax.set_facecolor('black')
    ax.axis('off')
    x_coords, y_coords = zip(*points)
    ax.scatter(x_coords, y_coords, color='green', s=0.1)

    # Обновляем текстовые метки
    roll_label.config(text=f"Число: {roll}")
    step_label.config(text=f"Кол-во шагов: {step}")

    # Обновляем окно, чтобы отобразить изменения
    canvas.draw()

    # Задержка для плавного отображения
    root.update_idletasks()
    root.after(5)  # Задержка 5 миллисекунд

    # Перезапускаем функцию обновления
    if step < iterations:
        root.after(1, update_plot, step + 1)

# Создание фрейма для размещения текстовых меток
frame = tk.Frame(root, bg='black')
frame.pack(side=tk.TOP, padx=20, pady=5)

# Создание текстовой метки для числа
roll_label = tk.Label(frame, text="Число: ", font=("Helvetica", 24), fg="#00FF00", bg="black")  # Зеленый цвет, черный фон
roll_label.grid(row=0, column=0, padx=(0, 5))  # Центрируем текст

# Создание текстовой метки для количества шагов
step_label = tk.Label(frame, text="Кол-во шагов: 0", font=("Helvetica", 24), fg="#00FF00", bg="black")  # Зеленый цвет, черный фон
step_label.grid(row=0, column=1, sticky='e')  # Выравнивание по правому краю

# Убираем фон у текстовых меток
roll_label.config(bg='black')  # Устанавливаем фон метки черным
step_label.config(bg='black')  # Устанавливаем фон метки черным

# Добавляем график в окно
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Запускаем процесс обновления графика
update_plot(0)

# Запускаем основной цикл приложения
root.mainloop()
