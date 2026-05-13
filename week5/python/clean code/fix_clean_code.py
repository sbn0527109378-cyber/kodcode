# תרגיל 1

# def returns_adult_and_active(listi):
#     new_list = []
#     for line in listi:
#         if line[1] >= 18 and line[2]:
#             new_list.append(line[0])
#     return new_list
#
# list_of_students = [
#     ["Dan", 25, True],
#     ["Noa", 16, True],
#     ["Yael", 30, False],
# ]
#
# print(returns_adult_and_active(list_of_students))


# תרגיל 2

def validation_check(user_email,stock,quantity):
    if not user_email:
        print("Invalid user")
        return None
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return None


def returns_price_updating_price(product_price,quantity,stock):
    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    stock -= quantity
    return price

def handle_purchase(user_email, product_name, product_price, quantity):
    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = product_price
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status

