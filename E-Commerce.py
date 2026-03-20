import mysql.connector as mysql
import tabulate, sys

class E_Commerce:
    def display_all_product(self):
        cursor.execute("SELECT * FROM products;")
        data = cursor.fetchall()
        headers =  ["ID", "ProductName", "Category", "Price", "StockAvailability", "Rating", "Seller"]
        print(tabulate.tabulate(data, headers, tablefmt="grid"))
        
    def sort_category(self, catag_name):
        data = None
        try:
            cursor.execute("SELECT * FROM products WHERE LOWER(Category) = LOWER(%s)", (catag_name,))
            data = cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        self.display_product(data)
        
    def sort_price(self, price_low, price_high):
        if price_low < price_high and price_low >= 0:
            data = None
            try:
                cursor.execute("SELECT * FROM products WHERE Price BETWEEN %s AND %s", (str(price_low), str(price_high)))
                data = cursor.fetchall()
            except Exception as e:
                print(f"Error: {e}")

            self.display_product(data)
        else:
            print("Enter valid price range")
        
    def sort_rating(self):
        print("1. ⭐ and UP, 2. ⭐⭐ and UP, 3. ⭐⭐⭐ and UP, 4. ⭐⭐⭐⭐ and UP, 5. ⭐⭐⭐⭐⭐")
        choice = int(input("Enter your choice: "))
        data = None
        try:
            if choice == 1:
                cursor.execute("SELECT * FROM products WHERE Rating >= 1")
                data = cursor.fetchall()
        
            elif choice == 2:
                cursor.execute("SELECT * FROM products WHERE Rating >= 2")
                data = cursor.fetchall()
        
            elif choice == 3:
                cursor.execute("SELECT * FROM products WHERE Rating >= 3")
                data = cursor.fetchall()
            
            elif choice == 4:
                cursor.execute("SELECT * FROM products WHERE Rating >= 4")
                data = cursor.fetchall()
            
            elif choice == 5:
                cursor.execute("SELECT * FROM products WHERE Rating = 5")
                data = cursor.fetchall()
            
            else:
                print("Enter valid choice")
        except Exception as e:
                print(f"Error: {e}")
        self.display_product(data)

    def search_product(self):
        search = input("Enter product name: ")
        data = None
        try:
            cursor.execute("SELECT * FROM products WHERE ProductName LIKE %s",("%"+search.lower()+"%",))
            data = cursor.fetchall()
            
        except Exception as e:
            print(f"Error: {e}")
    
        self.display_product(data)
    
    def display_product(self,data):
        if data != None:
            headers =  ["ID", "ProductName", "Category", "Price", "StockAvailability", "Rating", "Seller"]
            print(tabulate.tabulate(data, headers, tablefmt="grid"))
        else:
            print("No products found")

class cart:
    def add_items_cart(self, product_id):
        cursor.execute("SELECT * FROM products")
        data = cursor.fetchall()
        try:
            for id in data:
                if product_id == id[0] and 'Out of Stock' != id[4]:
                    cursor.execute("INSERT INTO cart (ID, ProductName, Category, Price, StockAvailability, Rating, Seller) values (%s, %s, %s, %s, %s, %s, %s)", (id))
                    mycon.commit()
                    print("Product added to cart")
                    return
                elif product_id == id[0] and 'Out of Stock' == id[4]:
                    data = 1
                    break
                
            else:
                data = None
        except Exception as e:
            print(f"Error: {e}")
        self.display_cart_items(data)
        
     
    def remove_items_cart(self, product_id):
        cursor.execute("SELECT * FROM cart")
        data = cursor.fetchall()
        try:
            if len(data) == 0:
                    data = 2
            else:
                for id in data:
                    if product_id == id[0]:
                        print(type(product_id), product_id)
                        cursor.execute("DELETE FROM cart WHERE ID = '{}';".format(product_id))
                        mycon.commit()
                        print("Product deleted from the cart")
                        return
                else:
                    data = None
        except Exception as e:
            print(f"Error: {e}")
            
        self.display_cart_items(data)
                
    def display_cart_items(self, data):
        if data != None and data != 1 and data != 2:
            headers =  ["ID", "ProductName", "Category", "Price", "StockAvailability", "Rating", "Seller"]
            print(tabulate.tabulate(data, headers, tablefmt="grid"))
            
        elif data == 1:
            print("The product is Out of Stock")
        
        elif data == 2:
            print("The cart is Empty...")
            
        else:
            print("No products found")
        
         
class purchase:
    def displaying_bill(self):
        cursor.execute("SELECT * FROM cart")
        data = cursor.fetchall()
        cursor.execute("SELECT SUM(Price) FROM cart")
        total = cursor.fetchall()
        total_bill =(("", "", "", total, "", "", ""),)
        headers =  ["ID", "ProductName", "Category", "Price", "StockAvailability", "Rating", "Seller"]
        print(tabulate.tabulate(data, headers, tablefmt="grid"))
        print(tabulate.tabulate(total_bill, headers= ["", "", "", "Total", "", "",""], tablefmt = "grid"))
        cursor.execute("DELETE FROM cart;")
        mycon.commit()
            
            
#_main_
mycon = mysql.connect(host = 'localhost', user = 'root', password = 'passwd', database = 'E_Commerce', auth_plugin="mysql_native_password")
cursor = mycon.cursor()

while True:
    try:

        print(""" 
    ----------------------------------- Products Functions -----------------------------------
    1. To Display All The Products
    2. Sort by Catagory
    3. Sort by Price
    4. Sort by Rating
    5. Search Product by Name

    ---------------------------------------- Your Cart ----------------------------------------
    6. Add Item in Cart
    7. Remove Item form Cart
    8. Display Cart Items 

    ----------------------------------------- Purchase -----------------------------------------
    9. To Complete the Purchase of Items in Your Cart
    10. Exit 

    ---------------------------------------------------------------------------------------------

    Enter Your Chocie:
            """)
        chocie = eval(input())
        if type(chocie) == int:
            if chocie <= 5:
                product = E_Commerce()
                
                if chocie == 1:
                    product.display_all_product()
                
                elif chocie == 2:
                    print("...Sort by Category...\n")
                    print("""
    Distinct Category:
                        
    |Electronics      |
    | Footwear        |
    | Furniture       |
    | Fitness         |
    | Accessories     |
    | Home Appliances |
    | Kitchen         |
    | Pet Supplies    |
    | Home & Office   |
    | Office Supplies |
    | Home Decor      |
    | Outdoor         |
    | Beauty          |
    | Home Automation |
    | Personal Care   |
    | Home Security   |
    | Automotive      |
    | Home & Garden   |
    | Baby Care       |

    Please Copy The Category Name and Past it
    to Make Easier.\n     
                        """)
                    category = input("Enter Category Name: ")
                    product.sort_category(category)
                
                elif chocie == 3:
                    print("...Sort by Price...\n")
                    Lower_limit = int(input("Enter The Lower Limit: "))
                    Upper_limit = int(input("Enter The Upper Limit: "))
                    product.sort_price(Lower_limit, Upper_limit)
                    
                elif chocie == 4:
                    print("...Sort by Rating...\n")
                    product.sort_rating()
                
                elif chocie == 5:
                    print("...Search Product by Name...\n")
                    product.search_product()
                    
            elif chocie <= 8:
                Cart = cart()
                if chocie == 6:
                    print("...Adding Product in Cart...\n")
                    ID = input("Enter The Product ID: ")
                    Cart.add_items_cart(ID)
                
                elif chocie == 7:
                    print("...Removing Product From Cart...\n")
                    ID = input("Enter The Product ID: ")
                    Cart.remove_items_cart(ID)
                
                elif chocie == 8:
                    cursor.execute("SELECT * FROM cart")
                    data = cursor.fetchall()
                    if len(data) != 0:
                        Cart.display_cart_items(data)
                    
                    else:
                        print("Your Cart is Empty")
                    
            elif chocie == 9:
                Purchase = purchase()
                Purchase.displaying_bill()
                print("""
    1. Cards
    2. Cash
    3. Netbanking
    4. UPI
    5. Wallet
    """)
                
                pay = int("Choose The Way You Want to Make Payment")
            elif chocie == 10:
                print("Exiting...")
                break
            
            else:
                print("Enter Valid Chocie!")
                    
        else:
            print("Enter Valid Chocie!")

        
    except Exception as e:  
        print("Try Again...")
