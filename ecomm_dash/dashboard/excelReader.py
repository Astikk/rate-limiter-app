import csv
from .models import Platform, Product, Category, Customer, Order

def handleExcelUpload(file_path):
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    category = row['Category']
                    product_id = row['ProductID']
                    product_name = row['ProductName']
                    customer_id = row['CustomerID']
                    customer_name  = row['CustomerName']
                    contact_email = row['ContactEmail']
                    phone_number = row['PhoneNumber']
                    order_id = row['OrderID']
                    quantity_sold = row['QuantitySold']
                    selling_price = row['SellingPrice']
                    delivery_status = row['DeliveryStatus']
                    platform_name = row['Platform']

                    platform, _ = Platform.objects.get_or_create(platform_name=platform_name)
                    category, _ = Category.objects.get_or_create(name=category)
                    product, _ = Product.objects.get_or_create(
                        product_id= product_id, 
                        product_name= product_name,
                        category=category)
                    customer, _ = Customer.objects.get_or_create(
                        customer_id = customer_id,
                        customer_name = customer_name,
                        contact_email = contact_email,
                        phone_number = phone_number
                    )
                    data = {
                        "order_id" : order_id,
                        "product" : product,
                        "customer": customer,
                        "quantity_sold" : quantity_sold,
                        "selling_price" : selling_price,
                        "delivery_status" : delivery_status,
                    }
                    Order.objects.get_or_create(**data)
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)
