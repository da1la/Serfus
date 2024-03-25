import os
import random
import time
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_ascii_art():
    # Список файлов ASCII-арта
    ascii_art_files = [f'kerfus{i}.txt' for i in range(1, 6)]

    # Выбираем случайный файл
    chosen_file = random.choice(ascii_art_files)

    # Если выбран арт 4, добавляем после него арт 1
    if chosen_file == 'kerfus4.txt':
        ascii_art_files.append('kerfus1.txt')

    with open(chosen_file, 'r') as file:
        ascii_art = file.readlines()

    # Получаем размеры терминала
    terminal_height, terminal_width = os.get_terminal_size().lines, os.get_terminal_size().columns

    # Определяем максимальную высоту ASCII-арта (не более высоты терминала)
    max_height = min(len(ascii_art), terminal_height)

    # Масштабируем ASCII-арт под размеры терминала
    scaled_ascii_art = []
    for line in ascii_art:
        scaled_line = line.rstrip().ljust(terminal_width)[:terminal_width]
        scaled_ascii_art.append(scaled_line)

    # Добавляем пустые строки, если высота арта меньше высоты терминала
    scaled_ascii_art += [' ' * terminal_width] * (max_height - len(scaled_ascii_art))

    # Обрезаем ASCII-арт до максимальной высоты
    scaled_ascii_art = scaled_ascii_art[:max_height]

    return scaled_ascii_art

def main():
    try:
        while True:
            clear_screen()
            if '-b' in sys.argv:
                print("\033[34m")  # Синий цвет текста
            elif '-c' in sys.argv:
                print("\033[36m")  # голубой цвет текста
            elif '-r' in sys.argv:
                print("\033[31m")  # Красный цвет текста
            elif '-g' in sys.argv:
                print("\033[32m")  # Зелёный цвет текста
            elif '-o' in sys.argv:
                print("\033[33m")  # Оранжевый цвет текста
            elif '-p' in sys.argv:
                print("\033[35m")  # Фиолетовый цвет текста
            ascii_art = load_ascii_art()
            print('\n'.join(ascii_art))
            time.sleep(0.5)  # Пауза перед отображением следующего кадра
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
