# Define the calculate_discount function
def calculate_discount(price, discount_percent):
    # set the conditions for applying the 20% discount
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage for the item: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price != price:
        print(f"Final price after discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Original Price is: {price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
