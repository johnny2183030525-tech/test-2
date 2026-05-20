import pandas as pd

stock1 = [120, 80, None, 60, 95, None, 110]

index_labels = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Peach', 'Melon']
stock2 = pd.Series(stock1, index=index_labels)

stock3 = stock2.to_dict()

print(stock1)
print(stock2)
print(stock3)

print(stock2['Banana'])

print(stock2.isnull().sum())

stock2.to_csv('0520_stock.csv', index=True, header=['Stock'])