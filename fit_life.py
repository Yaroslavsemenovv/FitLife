# Проект FitLife - MVP версия 1.0
import sys

sys.stdout.reconfigure(encoding="utf-8")
# Падал 6 тест

# 1. Знакомство
print("Привет! Я FitLife — твой помощник в заботе о здоровье.")
user_name = input("Как тебя зовут? ")
user_age = int(input("Сколько тебе лет? "))


# 2. Сбор данных
user_weight = float(input("Укажи свой вес в кг "))
user_height = float(input("Укажи свой рост в метрах "))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)


# Подсчет воды: вес * 30 мл
water_ml = user_weight * 30
water_l = water_ml / 1000


# 4. Вывод красивого результата
print(f"Привет, {user_name}!")
print(f"Твой возраст: {user_age} лет")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л в день")
print("Расчет окончен. Будьте здоровы!")
