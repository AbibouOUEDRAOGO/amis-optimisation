import pandas as pd
data = {
     "nom": ["Alice", "Paul", "Sarah", "Thomas", "Inès"],
    "age": [21, 23, 22, 24, 21],
    "note": [15, 11, 17, 9, 14]
}

df = pd.DataFrame(data)
df.sort_values("note", ascending=False)

print(df)