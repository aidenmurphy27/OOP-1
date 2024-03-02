import CellPhoneClass as c

def main():
    phone = c.Cellphone('Apple', 'iPhone 12', 699.99)

    print(f"{phone.get_manufact()}, {phone.get_model()}, ${phone.get_retail_price()}")

main()