import pandas as pd
# Đọc file csv để tạo dataframe
dataFrame = pd.read_csv("Books.csv")
dataset = ["Book-Title", "Book-Author", "Year-Of-Publication"]
# print(dataFrame)
# newDataframe = dataFrame.loc[[0, 1, 2, 3], dataset]
# print(newDataframe)

# series = pd.Series([1, 2, 3], index=["a", "c", "d"], dtype=int)
# print(series)
# print(series.index)

# Hiển thị 5 dòng đầu tiên của Frame 
print(dataFrame.head())

