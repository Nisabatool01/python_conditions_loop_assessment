
# Task 2: Smart Pharmacy Inventory & Sales Management System
# Topic: Loop Structures, for loop, range(), conditions,
# counters and accumulators.

print("=" * 55)
print("       SMART PHARMACY INVENTORY & SALES SYSTEM")
print("=" * 55)

# STEP 1: Get number of medicines

medicines = int(input("\nEnter the number of medicines: "))

if medicines <= 0:
    print("\nInvalid number of medicines!")

else:
    # STEP 2: Initialize counters and accumulator

    total_revenue = 0
    processed_medicines = 0
    restock_medicines = 0

    # STEP 3: Process each medicine using for loop

    for medicine in range(1, medicines + 1):

        print(f"\n--- Medicine {medicine} ---")

        # Collect medicine information

        medicine_name = input("Enter medicine name: ")

        try:
            stock = int(input("Enter available stock: "))
            price = float(input("Enter price per unit (Rs.): "))
            quantity_sold = int(input("Enter quantity sold: "))

            # STEP 4: Validate medicine information

            if medicine_name.strip() == "":
                print("Invalid medicine name!")
                continue

            elif stock < 0 or price < 0 or quantity_sold < 0:
                print("Invalid input! Values cannot be negative.")
                continue

            elif quantity_sold > stock:
                print("Insufficient stock! Sale cannot be processed.")
                continue

            else:
                # STEP 5: Calculate sales and remaining stock

                sales_amount = price * quantity_sold
                remaining_stock = stock - quantity_sold

                # STEP 6: Display medicine sales details

                print("\n--- MEDICINE SALES DETAILS ---")
                print(f"Medicine Name   : {medicine_name}")
                print(f"Available Stock : {stock}")
                print(f"Quantity Sold   : {quantity_sold}")
                print(f"Sales Amount    : Rs. {sales_amount:.2f}")
                print(f"Remaining Stock : {remaining_stock}")

                # STEP 7: Check low stock

                if remaining_stock < 10:
                    print("WARNING: Low stock! Restocking required.")
                    restock_medicines += 1

                else:
                    print("Stock Status: Sufficient Stock")

                # STEP 8: Update accumulator and counter

                total_revenue += sales_amount
                processed_medicines += 1

        except ValueError:
            print("Invalid input! Please enter valid numeric values.")

    # STEP 9: Generate final pharmacy report

    print("\n" + "=" * 55)
    print("             PHARMACY DAILY SALES REPORT")
    print("=" * 55)

    print(f"Total Medicines Entered : {medicines}")
    print(f"Successfully Processed  : {processed_medicines}")
    print(f"Total Sales Revenue     : Rs. {total_revenue:.2f}")
    print(f"Medicines to Restock    : {restock_medicines}")

    print("=" * 55)
    print("       THANK YOU FOR USING PHARMACY SYSTEM")
    print("=" * 55)
