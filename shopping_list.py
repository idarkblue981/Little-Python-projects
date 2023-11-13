def main():
    shopping_list()

def shopping_list():
    while True:
        try:
            print('When the list is ready, write "X" in the product section.')
            list_products = []
            list_prices = []
            for _ in range(1000):
                product = input('Enter product: ')
                if product == 'X' or product == 'x':
                    break
                list_products.append(product)
                price = float(input('Enter price: '))
                list_prices.append(price)
            print("-----------------------------------------------------------------------------------------------------------------")
            print(f'List of products: {list_products}')
            print(f'Total sum to pay: {sum(list_prices)}')
            print(f'Biggest price / product: {max(list_prices)}')
            print(f'Smallest price / product: {min(list_prices)}')
            print("-----------------------------------------------------------------------------------------------------------------")
        except ValueError:
            pass

if __name__ == '__main__':
    main()
