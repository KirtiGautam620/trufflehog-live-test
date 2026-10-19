
def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")

    return price * discount_percent / 100


def final_price(price, discount_percent):
    discount = calculate_discount(price, discount_percent)
    return price - discount


if __name__ == "__main__":
    print(final_price(1000, 20))
