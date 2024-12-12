# Assume a shipping price of $7 per pound for items over 50 pounds and $10 per pound for items 50 pounds or under.
# Calculate the shipping price based on the unit weight
def calculate_shipping_price(unit_weight, qty):
    """
    Calculate shipping price based on item_weight and quantity

    Parameters:
        item_weight (float): Weight of a single item in pounds
        quantity (int): Number of items

    Returns:
        float: Shipping price based on total weight

    """
    # Calculate the total weight
    total_weight = unit_weight * qty
    if total_weight > 50:
        return total_weight * 7
    else:
        return total_weight * 10
