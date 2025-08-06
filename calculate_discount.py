def calculate_discount(price, discount_percent):
    if discount_percent >= 0.2:
        dis = price*discount_percent
        price_after_dis = price -dis
        return price_after_dis
    return price

r=calculate_discount(100,0.2)

print(r)
