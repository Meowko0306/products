#refactor
import os #operating system 載入作業系統

#讀取檔案
def read_file(filename):
    products = [] #裝name
    #讀取檔案
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #繼續
            name, price = line.strip().split(',') #先拿掉換行符號sprip() 然後作逗點切割split(',')
            products.append([name,price])
    return products #讀完的清單存進 products 所以要回傳


#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ') #如果使用者輸入q就不執行這行
        price = int(price)
        products.append([name, price])
    print(products)
    return products

#印出所有購買紀錄
def print_products(products):
    for product in products:
        print(product[0], '的價格是', product[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f: #encoding 使用utf-8編碼
        f.write('商品,價格\n')
        for product in products:
            f.write(product[0] + ',' + str(product[1]) + '\n') 

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#檢查檔案在不在
        print('yeah! 找到檔案了!')
        products = read_file(filename)
    else:
        print('到不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()