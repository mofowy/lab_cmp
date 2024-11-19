import sys
import logging
import os
import subprocess

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Імпортуємо модулі з лабораторними роботами
from lab1.main import main as lab1_main
from lab2.main import main as lab2_main
from lab3.main import main as lab3_main
from lab4.main import main as lab4_main
from lab5.main import main as lab5_main
from lab6.main import main as lab6_main
from lab7.main import main as lab7_main
from lab8.main import main as lab8_main


class LabRunnerFacade:
    """Facade для запуску лабораторних робіт."""

    def __init__(self):
        logging.info("Ініціалізація лабораторних робіт...")
        self.labs = {
            1: lab1_main,
            2: lab2_main,
            3: lab3_main,
            4: lab4_main,
            5: lab5_main,
            6: lab6_main,
            7: lab7_main,
            8: lab8_main,
        }
        logging.info("Ініціалізація завершена.")

    def run_lab(self, lab_number):
        """Запускає відповідну лабораторну роботу."""
        if lab_number in self.labs:
            print(f"\nЗапуск лабораторної роботи {lab_number}...\n")
            try:
                self.labs[lab_number]()  # Виклик функції main() для відповідного модуля
            except Exception as e:
                print(f"Помилка під час виконання лабораторної роботи {lab_number}: {e}")
        else:
            print(f"Лабораторна робота {lab_number} не знайдена.")

    def run_tests(self, lab_number):
        """Запускає тести для відповідної лабораторної роботи."""
        test_files = {
            1: "lab6/tests/AdditionTests.py",
            2: "lab6/tests/DividionTests.py",
            3: "lab6/tests/ErrorHandlingTests.py",
            4: "lab7/tests/test_api_client.py",
        }
        test_file = test_files.get(lab_number)
        if not test_file:
            print(f"Для лабораторної роботи №{lab_number} тести не знайдено.")
            return

        if os.path.exists(test_file):
            print(f"Запускаємо тести для лабораторної роботи №{lab_number}...")
            subprocess.run(["python", "-m", "unittest", test_file])
        else:
            print(f"Файл з тестами не знайдено: {test_file}.")


def display_menu():
    """Виводить меню на екран."""
    print("=== Меню запуску лабораторних робіт ===")
    print("1. lab1")
    print("2. lab2")
    print("3. lab3")
    print("4. lab4")
    print("5. lab5")
    print("6. lab6")
    print("7. lab7")
    print("8. lab8")
    print("9. unittests")
    print("0. Exit")

def display_unittest():
    print("\n=== Меню запуску тестів ===")
    print("1. lab6_AdditionTests")
    print("2. lab6_DividionTests")
    print("3. lab6_ErrorHandlingTests")
    print("4. lab7_test_api_client")
    print("0. Back")

def main():
    """Головна функція Runner."""
    runner = LabRunnerFacade()

    while True:
        display_menu()
        try:
            choice = int(input("Input: "))
            if choice == 0:
                sys.exit()
                runner.run_lab(choice)
            elif choice == 9:
                while(True):
                    display_unittest()
                    try:
                        choice = int(input("Input: "))
                        if choice == 0:
                            break
                        elif 1 <= choice <= 4:
                            runner.run_tests(choice)
                        else:
                            print("Некоректний вибір.")
                    except ValueError:
                        print("Помилка: введіть коректне число.")
                    except Exception as e:
                        print(f"Сталася помилка: {e}")
            elif 1 <= choice <= 8:
                runner.run_lab(choice)
            else:
                print("Некоректний вибір.")
        except ValueError:
            print("Помилка: введіть коректне число.")
        except Exception as e:
            print(f"Сталася помилка: {e}")


if __name__ == "__main__":
    main()