import os #operating system 載入作業系統

products = [] #裝name
if os.path.isfile('products.csv'):#檢查檔案在不在
	print('yeah! 找到檔案了!')
	#讀取檔案
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name, price = line.strip().split(',') #先拿掉換行符號sprip() 然後作逗點切割split(',')
			products.append([name,price])
	print(products)
else:
	print('找不到檔案......')


#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ') #如果使用者輸入q就不執行這行
	price = int(price)
	products.append([name, price])
print(products)

#印出所有購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])

with open('products.csv', 'w', encoding='utf-8') as f: #encoding 使用utf-8編碼
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n') 