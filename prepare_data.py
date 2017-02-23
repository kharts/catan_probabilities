import pandas as pd

numbers_str = "8, 4, 8, 6, 6, 2, 4, 8, 11, 8, 3, 6, 6, 9, 2, 5, 5, 11, 9, 7, 6, 8, 10, 6, 3, 9, 9, 10, 6, 7, 3, 9, 5, 3, 6, 7, 6".split(", ")

df = pd.DataFrame({"number": numbers_str})

df.to_csv("data.csv")