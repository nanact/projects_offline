import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Score': [85, 90, 78, 88]
}

df = pd.DataFrame(data)
print(df)

print(df.info()) 
print(df.describe()) 
print(df.head(2))  
print(df.tail(2))  
