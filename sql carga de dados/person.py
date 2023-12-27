import psycopg2 as db
import csv

class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user":"postgres",
                "password": "9630",
                "host": "127.0.0.1",
                "port": "5432",
                "database": "pydb"
            }
        }
    
class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro na conexão", e)
            exit(1)
            
 
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_vaçl, exc_tb):
        self.commit()
        self.connection.close()
    
    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur
    
    def commit(self):
        self.connection.commit()      
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
    
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
    

class Person(Connection):
    def __init__(self):
        Connection.__init__(self)
        
    
    ##o id esta auto complete    
    def insert(self, *args):
        try:
            sql = "INSERT INTO person (name) VALUES (%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)
            
            
    def insert_csv(self, filename):
        try:
            data = csv.DictReader(open(filename, encoding="utf-8"))
            for row in data:
                print(row)
                self.insert(row["name"])##self.insert(row["name"],row["etc"])
            print("Registro inserido")
        except Exception as e:
            print("Erro ao inserir linha", e)
    
    
    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM person WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado para deletar"
            sql_d = f"DELETE FROM person WHERE id= {id}"
            self.execute(sql_d)
            self.commit()
            return "Registro deletado"
        except Exception as e:
            print("Erro ao deletar", e)
            
    
    def update(self, id , *args):
        try:
            sql = f"UPDATE person SET name = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Registro atualizado")
        except Exception as e:
            print("Erro ao atualizar", e)
            
            
    def search(self, *args, type_s="name"):
        sql = "SELECT * FROM person WHERE name LIKE %s"
        if type_s == "id":
            sql = "SELECT * FROM person WHERE id = %s"
        data = self.query(sql,args)
        if data:
            return data
        return "Registro não encontrado"
            
if __name__ == "__main__":
    person = Person()
    print(person.query("SELECT * FROM person"))
    # person.insert("Maria")
    # person.insert_csv("data.csv")
    # print(person.delete(4))
    #person.update(2,"Rodrigo MM")
    #print(person.search(22, type_s="id"))
    print(person.search("Rodrigo%"))
    #print(person.query("SELECT * FROM person"))
    