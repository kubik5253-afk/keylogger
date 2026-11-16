import time
from pynput import keyboard
import os

# Файл для записи лога
LOG_FILE = "invoker_cast_log.txt"

# Глобальная переменная для хранения времени старта
start_time = None

def on_press(key):
    global start_time
    
    # Инициализируем время при первом нажатии
    if start_time is None:
        start_time = time.time()
        
    try:
        # Получаем символ клавиши
        char = key.char
    except AttributeError:
        # Если это специальная клавиша (Shift, Ctrl, Q, W и т.д.)
        char = str(key)

    # Вычисляем время с момента начала записи
    elapsed_time = time.time() - start_time
    
    # Форматируем строку лога: Время(сек) | Клавиша
    log_entry = f"{elapsed_time:.4f} sec : {char}\n"
    
    print(log_entry.strip())  # Вывод в консоль для отладки
    
    # Записываем в файл
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def on_release(key):
    # Опционально: можно записывать отпускание клавиш, 
    # но для анализа прокаста обычно важнее только нажатие.
    if key == keyboard.Key.esc:
        # Останавливаем слушатель при нажатии Esc
        return False

def main():
    print("--- Кейлоггер запущен ---")
    print(f"Логи записываются в файл: {os.path.abspath(LOG_FILE)}")
    print("Нажмите ESC для остановки записи.")
    
    # Очищаем файл перед новой записью
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("") 

    # Запускаем слушатель клавиатуры
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    print("--- Запись остановлена ---")

if __name__ == "__main__":
    main()