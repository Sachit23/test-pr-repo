def calculate_final_price(price, discount_percent, quantity):
    """
    Calculates the final price after applying a percentage discount.
    If quantity is more than 10, an extra 5% is shaved off.
    """
    # Basic discount calculation
    reduced_price = price * (1 - (discount_percent / 100))
    
    # Bulk discount logic
    if quantity > 10:
        reduced_price = reduced_price * 0.95
        
    return reduced_price * quantity

# --- EXISTING TESTS ---
def test_calculate_final_price():
    # Test a normal case
    assert calculate_final_price(100, 10, 1) == 90.0
    
    # Test bulk discount
    # 100 * 0.9 (10% off) = 90. 90 * 0.95 (bulk) = 85.5. 85.5 * 20 = 1710
    assert calculate_final_price(100, 10, 20) == 1710.0