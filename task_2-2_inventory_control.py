# task_2-2_inventory_control.py
reagent_name = input("Введите название нового реактива: ")
reagent_quantity = int(input("Введите количество (целое число): "))
print(f"\nРеактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт.")
with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт.\n ")

print("\nОтчет записан в файл inventory.txt")