def main():
    try:
        print("When the list is ready, write 'X' in the product section.")
            
        list_products = []
        total = 0
        biggest_price = -float('inf')
        smallest_price = float('inf')
        biggest_product = ""
        smallest_product = ""
            
        while True:
            product = input("Enter product: ").strip().lower()
            if product == 'x':
                break
            list_products.append(product)

            price = float(input("Enter price: "))
            if price < 0:
                raise ValueError
            total += price
            if price > biggest_price:
                biggest_price = price
                biggest_product = product
            if price < smallest_price:
                smallest_price = price
                smallest_product = product

        if list_products:
            print("---- ---- ---- ---- ---- ---- ---- ----")
            print(f"List of products: {list_products}")
            print(f"Total sum to pay: {total}")
            print(f"Biggest price / product: {biggest_price} / {biggest_product}")
            print(f"Smallest price / product: {smallest_price} / {smallest_product}")
            print("---- ---- ---- ---- ---- ---- ---- ----")
        else:
            print("No products entered.")

    except ValueError:
        print("Please enter a non-negative value here.")

if __name__ == "__main__":
    main()
