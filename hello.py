import numpy as np
import pandas as pd

# NumPy test
arr = np.array([1, 2, 3, 4, 5])

print("NumPy Array:")
print(arr)
print("Mean:", np.mean(arr))

# Pandas test
data = {
    "Name": ["Ali", "Sara", "John"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)