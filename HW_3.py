import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\User\Desktop\комп Настя\Ivan\python\HW3_pandas.csv"

try:
    data = pd.read_csv(file_path)
    print("Данные успешно загружены!")
except FileNotFoundError:
    print("Ошибка: файл не найден. Проверьте путь к файлу.")
    exit()

print(f"Имена столбцов файла: {data.columns}")

required_column = 'Баллы'
if required_column not in data.columns:
    raise ValueError(f"Столбец '{required_column}' не найден в файле. Проверьте содержимое данных!")

print("\nПервые 5 строк данных:")
print(data.head())

filtered_data = data[data[required_column] > 50]
print(f"\nОтфильтрованные данные (где '{required_column}' > 50): {filtered_data.shape[0]} строк")
print(filtered_data)

data[f'{required_column}_doubled'] = data[required_column] * 2
print("\nДобавлен новый столбец:")
print(data.head())

print("\nОбработка пропущенных данных...")
if data.isnull().values.any():
    data.fillna(data.mean(numeric_only=True), inplace=True)
print(data.head())

plt.figure(figsize=(10, 6))
plt.scatter(data[required_column], data[f'{required_column}_doubled'], label=f'{required_column} vs Doubled')
plt.title('График зависимости', fontsize=14)
plt.xlabel(required_column, fontsize=12)
plt.ylabel(f'{required_column}_doubled', fontsize=12)
plt.legend()
plt.grid()
plt.show()

