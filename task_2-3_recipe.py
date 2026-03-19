# task_2-3_recipe.py
medium_name = input("Введите название питательной среды: ")
agar_concentration = float(input("Введите концентрацию агара (%): "))
sterilization_temperature = int(input("Введите температуру стерилизации (С): "))
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"=== {medium_name} ===\n")
    file.write(f"Концентрация агара: {agar_concentration}%\n")

print("\nФайл 'recipe.txt' успешно сформирован!")