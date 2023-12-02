import pandas as pd  

bookFrame = pd.read_csv("Books.csv")
# print(bookFrame)

# # Lấy dữ liệu hàng đầu tiên 
# print(bookFrame.iloc[0])

# # Lấy nhiều hàng : 
# print(bookFrame.iloc[0:5])

# # Lấy các hàng và cột được chỉ định 
# print(bookFrame.iloc[0:5, 0:3])

# Lấy dữ liệu bằng nhãn
print(bookFrame.loc[0:3, "Book-Title"])
