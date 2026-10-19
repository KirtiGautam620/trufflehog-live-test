
def calculate_order_total(prices):
    if not prices:
        return 0

    for price in prices:
        if price < 0:
            raise ValueError("Price cannot be negative")

    return sum(prices)


def apply_shipping(total, shipping_fee):
    if total < 0 or shipping_fee < 0:
        raise ValueError("Amounts cannot be negative")

    return total + shipping_fee


if __name__ == "__main__":
    print(calculate_order_total([100, 200, 150]))
    print(apply_shipping(450, 40))
