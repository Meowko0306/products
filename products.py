products = [] #裝name
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ') #如果使用者輸入q就不執行這行
	price = int(price)
	products.append([name, price])
print(products)

for product in products:
	print(product[0], '的價格是', product[1])

with open('products.csv', 'w', encoding='utf-8') as f: #encoding 使用utf-8編碼
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n') 