products = [] #裝name
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ') #如果使用者輸入q就不執行這行
	products.append([name, price])
print(products)