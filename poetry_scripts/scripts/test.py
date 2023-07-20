import subprocess
import sys

def main():
    # Команда для запуска тестов Django
    command = ["poetry", "run", "python", "manage.py", "test"]

    # Передаем аргументы командной строки, если они есть
    if len(sys.argv) > 1:
        command.extend(sys.argv[1:])

    # Запускаем команду
    subprocess.run(command, check=True)

if __name__ == "__main__":
    main()