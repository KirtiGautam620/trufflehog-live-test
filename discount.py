def apply_discount(price, discount_percent):
    discount = price * discount_percent / 100
    return price - discount


def main():
    price = 1000
    discount_percent = 20
    final_price = apply_discount(price, discount_percent)
    print("Final price:", final_price)


if __name__ == "__main__":
    main()
