import mysql.connector

class OrdersModel:
    def __init__(self,db):
        self.db = db
    
    def GetAll(self):
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM orders")

                myresult = cursor.fetchall()
                orders = []
                for ord in myresult:
                    orders.append(self._totuple(ord))
        
            return orders
        except Exception as e:
            print("Error getting all orders:", e)
            return False


    def Insert(self, produktID,invoicenummer,customerid,status,mangde,lagerID):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor(dictionary=True) as cursor:
                query = "INSERT INTO orders (produktID, invoicenummer,customerid,status,mangde,lagerID) VALUES (%s, %s, %s,%s, %s, %s)"

                cursor.execute(query, (produktID, invoicenummer, customerid,status,mangde,lagerID))
                result = cursor.fetchall()
                #n_id = cursor.lastrowid
            conn.commit()
            #result = self.GetByProductID(produktID)
            return True
        except Exception as e:
            print("Error inserting orders:", e)
            return False
    def GetByID(self, OrderID):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM orders where OrderID = %s ", (OrderID,))

                myresult = cursor.fetchall()
        
            return self._totuple(myresult[0])
        except Exception as e:
            print("Error getting orders by orderID:", e)
            return False

    def GetByProductID(self, produktID):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(f"SELECT * FROM orders where produktID = %s ", (produktID,))

                myresult = cursor.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders by productID:", e)
            return False


    def GetByCustomerID(self, customerid):
        
        try:
            conn = self.db.get_connection()
            conn.execute(f"SELECT * FROM orders where customerid = %s ", (customerid,))

            myresult = conn.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders by customerID:", e)
            return False

    def GetByWarehouseID(self, lagerID):
        
        try:
            conn = self.db.get_connection()
            conn.execute(f"SELECT * FROM orders where lagerID = %s ", (lagerID,))

            myresult = conn.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders by lagerID:", e)
            return False


    def GetbyStatus(self, status):
        
        try:
            conn = self.db.get_connection()
            conn.execute(f"SELECT * FROM orders where status = %s ", (status,))

            myresult = conn.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders by status:", e)
            return False


    def GetByInvoiceNumber(self, invoicenummer):
        
        try:
            conn = self.db.get_connection()
            conn.execute(f"SELECT * FROM orders where invoicenummer = %s ", (invoicenummer,))

            myresult = conn.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders by invoicenumber:", e)
            return False
    
    def UpdateOrder(self, orderID, produktID,invoicenummer,customerid,status,mangde,lagerID):

        try:
            conn = self.db.get_connection()
            with conn.cursor(dictionary = True) as cursor:
                query = f"UPDATE orders SET produktID = {produktID}, invoicenummer = {invoicenummer}, customerid = {customerid}, status = '{status}', mangde = {mangde}, lagerID = {lagerID} WHERE OrderID = {orderID}"
                cursor.execute(query)
                result = cursor.fetchall()
            conn.commit()
            return result
        except Exception as e:
            print("Error updating order:", e)
            return False

    def UpdateStatus(self, OrderID,newStatus):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor(dictionary = True) as cursor:
                query = "UPDATE orders SET status = %s WHERE OrderID = %s"

                cursor.execute(query, (newStatus, OrderID))
            conn.commit()
        
            return self.GetByID(OrderID)
        except Exception as e:
            print("Error updateing orders status:", e)
            return False
        
    def OrderCustomerView(self, customerid):
        
        try:
            conn = self.db.get_connection()
            conn.execute(f"SELECT"
                     f" orders.invoicenummer,"
                     f" produkts.navn,"
                     f" produkts.pris, "
                     f" orders.status, "
                     f" orders.mangde "
                     f"FROM orders "
                     f" join produkts on orders.produktID = produkts.produktID"
                     f" join customers on orders.customerid = customers.customerID"
                     f" where orders.customerid = %s ", (customerid,))

            myresult = conn.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders in customerview:", e)
            return False

    def _totuple(self, myresult):
        result = {
                "orderID": myresult[0],
                "produktID": myresult[1],
                "invoicenummer": myresult[2],
                "customerID": myresult[3],
                "status": myresult[4],
                "mangde": myresult[5],
                "lagerID": myresult[6]
            }
        return result
    