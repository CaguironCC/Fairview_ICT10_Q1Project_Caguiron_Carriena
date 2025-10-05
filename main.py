from pyscript import document

def createOrder(event):
    # Get customer info
    name = document.getElementById("customerName").value
    address = document.getElementById("customerAddress").value
    contact = document.getElementById("customerContact").value
    
    # Check if fields are empty
    if not name or not address or not contact:
        document.getElementById("orderOutput").innerHTML = '<span class="text-danger">ERROR: Please fill in all customer details</span>'
        return
    
    # Menu items
    items = [
        {"id": "carbonara", "name": "Spaghetti Carbonara", "price": 78.99},
        {"id": "garlicBread", "name": "Garlic Bread", "price": 50.00},
        {"id": "caesarSalad", "name": "Caesar Salad", "price": 150.00},
        {"id": "icedTea", "name": "Iced Tea", "price": 30.00},
        {"id": "sparklingWater", "name": "Sparkling Water", "price": 20.00}
    ]
    
    # Calculate total
    total = 0
    selected_items = []
    
    for item in items:
        checkbox = document.getElementById(item["id"])
        if checkbox.checked:
            total += item["price"]
            selected_items.append(item["name"])
    
    # Check if no items selected
    if not selected_items:
        document.getElementById("orderOutput").innerHTML = '<span class="text-danger">ERROR: Please select at least one menu item</span>'
        return
    
    # Create order summary
    summary = f"""
    Order for: {name}
    Address: {address}
    Contact: {contact}
    
    Items ordered:
    """
    
    for item in selected_items:
        summary += f"- {item}\n"
    
    summary += f"\nTotal: ₱{total:.2f}"
    
    # Show result
    document.getElementById("orderOutput").innerText = summary
