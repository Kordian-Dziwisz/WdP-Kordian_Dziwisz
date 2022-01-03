import numpy as np
import pandas as pd
data = pd.read_csv("miasta.csv")
df = pd.DataFrame(2010, 999, 888, 777)
data.concat(df)
print(data)
