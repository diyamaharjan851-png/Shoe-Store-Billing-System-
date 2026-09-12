import datetime as dt
from write import write_file

def buy(product_list, file_path):
    vendor_name = input("\nEnter vendor name: ")
    while True:
        try:
            vendor_phone = input("Enter customer phone number: ")
            if len(vendor_phone) != 10:
                print('Phone number has to be 10 digits.')
                continue
            vendor_phone = int(vendor_phone)
            break
        except ValueError:
            print("Phone number must be numbers only.")

    buy_list = []

    while True:
        try:
            product_id = input("\nEnter product ID to buy: ")
            product_id =  int(product_id)
            product = None
            for p in product_list:
                if int(p[0]) == product_id:
                    product = p
                    break

            if not product:
                print("Product ID not found.")
                continue

            print(f"Selected: {product[1]} (Current Stock: {product[3]}, Price: Rs.{product[4]})")
            qty = int(input("How many to add?: "))
            
            if qty <= 0:
                print("Quantity must be greater than zero.")
                continue

            unit_price = float(product[4])
            line_total = unit_price * qty

            buy_list.append({
                "id": product[0],
                "name": product[1],
                "price": unit_price,
                "added_quantity": qty,
                "line_total": line_total
            })

            product[3] = str(int(product[3]) + qty)
            print(f"New stock for {product[1]}: {product[3]}")

            more = input("Add more products? (y/n): ").lower()
            if more != 'y':
                break

        except ValueError:
            print("Please enter a valid number.")
            continue

    # ====== Generate Invoice ======
    invoice_text = []
    invoice_text.append("========== BUY INVOICE ==========\n")
    invoice_text.append(f"Date   : {dt.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}")
    invoice_text.append(f"Vendor : {vendor_name}")
    invoice_text.append(f"Phone  : {vendor_phone}")
    invoice_text.append("-" * 60)
    invoice_text.append(f"{'ID':<5} {'Name':<15} {'Price':>8} {'Qty':>6} {'Line Total':>15}")
    invoice_text.append("-" * 60)

    total_qty = 0
    grand_total = 0

    for item in buy_list:
        invoice_text.append(f"{item['id']:<5} {item['name']:<13} "
                            f"Rs.{item['price']:>7.2f} {item['added_quantity']:>6} "
                            f"Rs.{item['line_total']:>13.2f}")
        total_qty += item['added_quantity']
        grand_total += item['line_total']

    invoice_text.append("-" * 60)
    invoice_text.append(f"{'TOTAL':<15} {'Qty:':>10} {total_qty:>6}   {'Total:':>8} Rs{grand_total:>10.2f}")
    invoice_text.append("=" * 60)

    print()
    print("\n".join(invoice_text))
    print()

    if input("Confirm buy? (y/n): ").lower() == 'y':
        prefix = dt.datetime.now().strftime("%d_%m_%Y-%H-%M-%S")
        file_name = "buy_invoice_" + prefix + ".txt"
        with open(file_name, 'w') as f:
            f.write("\n".join(invoice_text))
        write_file(file_path, product_list)  # update inventory
        print(f"Buy confirmed. Invoice saved as {file_name}")
    else:
        print("Buy cancelled.")

def sell(product_list, file_path):
    # Customer details
    customer_name = input("\nEnter customer name: ")
    while True:
        try:
            customer_phone = input("Enter customer phone number: ")
            if len(customer_phone) != 10:
                print('Phone number has to be 10 digits.')
                continue
            customer_phone = int(customer_phone)
            break
        except ValueError:
            print("Phone number must be numbers only.")

    sell_list = []

    while True:
        try:
            product_id = int(input("\nEnter product ID to sell: "))
            product = None
            for p in product_list:
                if int(p[0]) == product_id:
                    product = p
                    break

            if not product:
                print("Product ID not found.")
                continue

            print(f"Selected: {product[1]} (Available: {product[3]}, Price: Rs.{product[4]})")
            qty = int(input("How many to sell?: "))

            if qty > int(product[3]):
                print("Not enough stock.")
                continue

            unit_price = float(product[4])
            line_total = unit_price * qty

            sell_list.append({
                "id": product[0],
                "name": product[1],
                "price": unit_price,
                "origin": product[5],
                "sale_quantity": qty,
                "line_total": line_total
            })

            product[3] = str(int(product[3]) - qty)

            more = input("Add more products? (y/n): ").lower()
            if more != 'y':
                break

        except ValueError:
            print("Please enter a valid number.")
            continue

    # --- Invoice calculation ---
    total_sum = 0
    international = 0
    domestic = 0
    for x in sell_list:
        total_sum += x["line_total"]
        if x["origin"].lower() == "international":
            international += 1
        if x["origin"].lower() == "domestic":
            domestic += 1

    discount_rate = 0
    if international >= 10:
        discount_rate += 0.05
    if domestic >= 10:
        discount_rate += 0.07

    total_discount = round(discount_rate * total_sum, 2)
    final_price = round(total_sum - total_discount, 2)

    # --- Build invoice text ---
    invoice_text = []
    invoice_text.append("========== SALE INVOICE ==========\n")
    invoice_text.append(f"Date     : {dt.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}")
    invoice_text.append(f"Customer : {customer_name}")
    invoice_text.append(f"Phone    : {customer_phone}")
    invoice_text.append("-" * 60)
    invoice_text.append(f"{'ID':<5} {'Name':<15} {'Price':>8} {'Qty':>6} {'Line Total':>15}")
    invoice_text.append("-" * 60)

    total_qty = 0

    for item in sell_list:
        invoice_text.append(f"{item['id']:<5} {item['name']:<15} "
                            f"Rs.{item['price']:>6.2f} {item['sale_quantity']:>6} "
                            f"Rs.{item['line_total']:>13.2f}")
        total_qty += item['sale_quantity']

    invoice_text.append("-" * 60)
    invoice_text.append(f"{'TOTAL':<15} {'Qty:':>10} {total_qty:>6}   {'Total:':>8} Rs.{total_sum:>10.2f}")
    invoice_text.append(f"{'':<15} {'':>10} {'':>4}   {'Discount:':>8} Rs.{total_discount:>10.2f}")
    invoice_text.append(f"{'':<15} {'':>10} {'':>6}   {'Final:':>8} Rs.{final_price:>10.2f}")
    invoice_text.append("=" * 60)

    # --- Print invoice ---
    print()
    print("\n".join(invoice_text))
    print()

    # --- Save if confirmed ---
    if input("Confirm sale? (y/n): ").lower() == 'y':
        prefix = dt.datetime.now().strftime("%d_%m_%Y-%H-%M-%S")
        file_name = "sale_invoice_" + prefix + ".txt"
        with open(file_name, 'w') as f:
            f.write("\n".join(invoice_text))
        write_file(file_path, product_list)  # update inventory
        print(f"Sale confirmed. Invoice saved as {file_name}")
    else:
        print("Sale cancelled.")
