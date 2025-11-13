import mysql.connector

class WarehuseInventoryModel:
    
    def __init__(self, db):
        self.db = db
    

    def GetALL(self):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM lager_manger")

                myresult = cursor.fetchall()
                result = []
                for wh in myresult:
                    result.append(WarehuseInventoryModel._tuple2Dict(wh))
                return result                 
        
        except Exception as e:
            print("Error getting LagerManger:", e)
            return False
        

    def GetByID(self, id):

        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM lager_manger where lagermangerID = %s ", (id,))
                myresult = cursor.fetchall()
                return WarehuseInventoryModel._tuple2Dict(myresult[0])
        except Exception as e:
            print(f"Error finding lager_manager: {e}")
            return False
    
    def GetByProductID(self,produktID):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM lager_manger where produktID = %s ", (produktID,))
                myresult = cursor.fetchall()
                result = []
                for wh in myresult:
                    result.append(WarehuseInventoryModel._tuple2Dict(wh))
                return result             
        except Exception as e:
            print("Error getting LagerManger by produktID:", e)
            return False
        
    def GetByWarehouseID(self,lagerID):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM lager_manger where lagerID = %s ", (lagerID,))
                myresult =cursor.fetchall()
                result = []
                for wh in myresult:
                    result.append(WarehuseInventoryModel._tuple2Dict(wh))
                return result            
        except Exception as e:
            print("Error getting LagerManger by id:", e)
            return False
        
    def Insert(self,lagerID,produktID,antal):
        
        try:
            n_id = -1
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                query = "INSERT INTO lager_manger (lagerID, produktID,antal) VALUES (%s, %s, %s)"

                cursor.execute(query, (lagerID, produktID,antal))
                n_id = cursor.lastrowid
            conn.commit()
            wh = {
                "id": n_id,
                "warehouse_id": lagerID,
                "product_id": produktID,
                "quantity": antal
            }     
            return wh
        except Exception as e:
            print("Error inserting LagerManger:", e)
            return False

    def Update(self, id, lagerID, produktID, antal):
        try:           
            conn = self.db.get_connection() 
            with conn.cursor() as cursor:
                query = """
                    UPDATE lager_manger
                    SET lagerID = %s, produktID = %s, antal = %s
                    WHERE lagermangerID = %s
                """
                cursor.execute(query, (lagerID, produktID, antal, id))                
            conn.commit()
            wh = {
                "id": id,
                "warehouse_id": lagerID,
                "product_id": produktID,
                "quantity": antal
            }     
            return wh
        except Exception as e:
            print(f"Error updating LagerManger: {e}")
            return False

    def Delete(self, id):
        try:
            conn = self.db.get_connection() 
            with conn.cursor() as cursor:
                query = "DELETE FROM lager_manger WHERE lagermangerID = %s"
                cursor.execute(query, (id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting LagerManger: {e}")
            return False
    def showSmartAll(self):
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT"
                     f" lagers.navn,"
                     f" produkts.navn,"
                     f" produkts.pris, "
                     f" lager_manger.antal "
                     f"FROM lager_manger"
                     f" join produkts on lager_manger.produktID = produkts.produktID"
                     f" join lagers on lager_manger.lagerID = lagers.lagerID"
                     f" ORDER BY lagers.navn ASC"
                     #f" where lagers.lagerID = %s ", (id,)
                     )


                myresult = cursor.fetchall()
                result = []
            for wh in myresult:
                result.append(WarehuseInventoryModel._tuple2Dict(wh))
            return result                 
        
        except Exception as e:
            print("Error getting LagerManger:", e)
            return False
    def _tuple2Dict(tuple):
        return {
            "id": tuple[0], 
            "warehouse_id": tuple[1],
            "product_id": tuple[2],            
            "quantity": tuple[3]
            }