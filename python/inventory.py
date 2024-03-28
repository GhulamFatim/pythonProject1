class Cart:
  """
  A class to represent a shopping cart.
  """
  def __init__(self):
    self.items = []

  def add_item(self, item_id, quantity=1):
    """
    Adds an item to the cart.

    Args:
      item_id: The ID of the item to add.
      quantity: The quantity of the item to add (default: 1).
    """
    for item in self.items:
      if item["id"] == item_id:
        item["quantity"] += quantity
        return

    self.items.append({"id": item_id, "quantity": quantity})

  def remove_item(self, item_id):
    """
    Removes an item from the cart.

    Args:
      item_id: The ID of the item to remove.
    """
    for i, item in enumerate(self.items):
      if item["id"] == item_id:
        del self.items[i]
        return

    print(f"Item with ID {item_id} not found in cart.")

  def update_item(self, item_id, quantity):
    """
    Updates the quantity of an item in the cart.

    Args:
      item_id: The ID of the item to update.
      quantity: The new quantity of the item.
    """
    for item in self.items:
      if item["id"] == item_id:
        item["quantity"] = quantity
        return

    print(f"Item with ID {item_id} not found in cart.")

  def delete_item(self, item_id):
    """
    Deletes an item from the cart (same as remove_item).

    Args:
      item_id: The ID of the item to delete.
    """
    self.remove_item(item_id)

  def get_total_quantity(self):
    """
    Gets the total quantity of all items in the cart.

    Returns:
      The total quantity of items in the cart.
    """
    total_quantity = 0
    for item in self.items:
      total_quantity += item["quantity"]
    return total_quantity

  def get_cart_items(self):
    """
    Gets a list of all items in the cart.

    Returns:
      A list of dictionaries representing the items in the cart.
    """
    return self.items

# Example usage
cart = Cart()

cart.add_item(100, 2)  # Add item with ID 100, quantity 2
cart.add_item(200, 1)  # Add item with ID 200, quantity 1

print(cart.get_cart_items())  # Output: [{'id': 100, 'quantity': 2}, {'id': 200, 'quantity': 1}]

cart.update_item(100, 3)  # Update quantity of item 100 to 3
cart.remove_item(200)  # Remove item with ID 200

print(cart.get_cart_items())  # Output: [{'id': 100, 'quantity': 3}]

cart.delete_item(100)  # Delete item with ID 100 (same as remove_item)

print(cart.get_cart_items())  # Output: []

print(cart.get_total_quantity())  # Output: 0
