# Exercise 3
import csv
import random


# Create random order_id
def order_id():
    return random.randint(1, 1000000)


# dictionary for discount codes
discount_codes = {
    'ifs354': 0.25,
    'man307': 0.10,
    'ifs361': 0.15,
}
# dictionary for Clothing options
apparel = {
    'Jeans': 250,
    'T-shirt': 130,
    'Sneakers': 500
}


# Track function to save data to CSV file
def track_orders(orders, disc_name):
    with open('orders.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if disc_name:
            writer.writerow([orders['order_id'], orders['total'], disc_name, orders['items']])
        else:
            writer.writerow([orders['order_id'], orders['total'], "None/Invalid", orders['items']])


# Summary of Order details
def order_summary(orders):
    summary = f"Order ID: {orders['order_id']}, "
    summary += f"Total: R{orders['total']:.2f}, "
    summary += f"Items: {orders['items']} "
    return summary


def latest_order():     # Order process logic
    order = {
        'order_id': order_id(),
        'total': 0,
        'items': {},
        'discount': 0
    }

    print('Available Clothing')
    for item in apparel:    # Display clothing to users
        print(item)
    while True:
        item = input("Enter item name (or 'done' to finish): ")     # Give user option to select multiple items
        if item.lower() == 'done':
            break
        if item in apparel:
            quantity = int(input("Enter quantity: "))   # Allow user to select no. items
            order['items'][item] = quantity
            order['total'] += apparel[item]*quantity
        else:
            print("Invalid item.")

    disc_code = input('Please insert your discount code: ')     # User insert code for discount

    if disc_code in discount_codes:
        discount_percentage = discount_codes[disc_code]
        discount_amount = order['total'] * discount_percentage
        order['discount'] = discount_amount
        order['total'] -= discount_amount       # if code valid, deduct discount amount from total
        print(f'Valid discount applied: R{discount_amount:.2f}')
    elif disc_code == 'none':       # if none, do nothing
        print('No discount applied')
    else:   # if invalid, do nothing
        print('Invalid discount')

    track_orders(order, disc_code if disc_code in discount_codes else None)
    print('Order details saved to orders.csv')
    print(order_summary(order))     # Display order summary to user


if __name__ == '__main__':
    latest_order()
