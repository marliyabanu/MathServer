price = float(input("Enter Price: "))
gst = float(input("Enter GST %: "))

gst_amount = (price * gst) / 100
total_bill = price + gst_amount

# SERVER SIDE OUTPUT
print("\nGST Calculation Result")
print("Price = ₹", price)
print("GST = ", gst, "%")
print("GST Amount = ₹", gst_amount)
print("Total Bill = ₹", total_bill)