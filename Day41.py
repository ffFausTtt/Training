def calculate_discount(price, is_member, purchase_history):
    discount_percent = 0.0
    
    if price > 1000:
        discount_percent += 5
    
    if is_member:
        discount_percent += 10
    
    if purchase_history > 0:
        bonus_discount = (purchase_history // 5000) * 3
        discount_percent += bonus_discount
    
    if discount_percent > 30:
        discount_percent = 30
    
    final_price = price * (1 - discount_percent / 100)
    
    return final_price, discount_percent


# Проверка
print("=== Тест 1 ===")
final_price, discount = calculate_discount(500, False, 0)
print(f"Итоговая цена: {final_price} руб.")
print(f"Скидка: {discount}%")

print("\n=== Тест 2 ===")
final_price, discount = calculate_discount(1500, True, 3000)
print(f"Итоговая цена: {final_price} руб.")
print(f"Скидка: {discount}%")

print("\n=== Тест 3 ===")
final_price, discount = calculate_discount(3000, True, 15000)
print(f"Итоговая цена: {final_price} руб.")
print(f"Скидка: {discount}%")