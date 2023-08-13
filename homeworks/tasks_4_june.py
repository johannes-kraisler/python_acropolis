"""3. Обчисліть, скільки секунд у добі
4. Обчисліть, скільки секунд у році
5. Відкрито нову планету! Введіть назву планети
і кількість земних днів в одному році на цій планеті (на
приклад один рік на новій планеті – 532 земних дні) Обчисліть і надрукуйте, скільки секунд становить рік
планети.
(«В одному році Zork 22118400 секунд»)
6. Візьміть як ціле число вік людини в місяцях і
виведіть «Істина», якщо особа старше 18 років, інакше
«False».
"""
seconds=60
minutes=60
hours=24
days=365

seconds_in_24h=seconds*minutes*hours
print(seconds_in_24h)
seconds_in_1year=seconds_in_24h*days
print(seconds_in_1year)

new_planet="Vencury"
days_n=days*100
seconds_in_24h_n=seconds_in_24h*days_n
print("One year on the planet {} equals to {} seconds".format(new_planet, seconds_in_24h_n))

age=int(input("What is your age in months?"))
in_years=age//12
if in_years>18:
    print(True, in_years)
else:
    print(False)