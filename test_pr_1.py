def calculate_total(price, quantity):
    return price * quantity


def main():
    total = calculate_total(100, 3)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
