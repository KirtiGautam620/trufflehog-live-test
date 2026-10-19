def calculate_shipping(weight):
    if weight <= 1:
        return 50
    elif weight <= 5:
        return 100
    else:
        return 200


def main():
    weight = 3
    cost = calculate_shipping(weight)
    print("Shipping cost:", cost)


if __name__ == "__main__":
    main()
