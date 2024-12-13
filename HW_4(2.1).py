import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'fruit': ['apple', 'banana', 'orange'] * 3,
    'weight': ['high', 'medium', 'low'] * 3,
    'price': np.random.randint(0, 15, 9)
})

df2 = pd.DataFrame({
    'pazham': ['apple', 'orange', 'pine'] * 2,
    'kilo': ['high', 'low'] * 3,
    'price': np.random.randint(0, 15, 6)
})

merged_df = pd.merge(df1, df2, left_on=['fruit', 'weight'], right_on=['pazham', 'kilo'])

print("Результат объединения двух DataFrame:")
print(merged_df)
