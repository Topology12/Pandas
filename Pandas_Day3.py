import pandas as pd
import numpy as np

dataFrame = pd.DataFrame([np.arange(5), np.arange(0,10, 2)], columns=["1", "2", "3", "4","5"])
# print(dataFrame)


arr = np.arange(5)

data_copy = dataFrame.copy()
data_copy.iloc[:,[1,2]] = pd.NA
print(data_copy)
data_copy.iloc[1,2:5] 