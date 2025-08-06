def calculate_discount(price, discount_percent):
    
        if not (price >= 0 and 0 <= discount_percent <= 1):
            return "Price must be non-negative and discount must be between 0 and 1."
        if discount_percent >= 0.2:
            discount = price * discount_percent
            return price - discount
        return price
 



price = float(input("Enter price (e.g., 100): ").strip())
discount_percent = float(input("Enter discount as a decimal (e.g., 0.2 for 20%): ").strip())
r = calculate_discount(price, discount_percent)
if isinstance(r, str):
    print(r)
else:
    print(f"Final price: ${r:.2f}")
