from math_operations import add, subtract, multiply, divide
from utils import get_number

def main():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Введите номер операции (1/2/3/4): ")

    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")

    if choice == '1':
        print(f"Результат: {add(num1, num2)}")
    elif choice == '2':
        print(f"Результат: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Результат: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Результат: {divide(num1, num2)}")
    else:
        print("Неверный выбор операции.")

if __name__ == "__main__":
    main()

    