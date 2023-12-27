import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = senha
post_id = 5432
conn = None
##cur = None


try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = post_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        ## cur = conn.cursor()
        
            cur.execute('DROP TABLE IF EXISTS employee')
            
            create_script = '''CREATE TABLE IF NOT EXISTS employee(
                                    id      int PRIMARY KEY,
                                    name    Varchar(40) NOT NULL,
                                    salary  int,
                                    dept_id varchar(30))'''
            cur.execute(create_script) 
            
            insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'James', 12000, 'D1'),(2, 'Robin', 15000, 'D1'),(3, 'Maria', 22000, 'D2') ]
            for record in insert_values:
                cur.execute(insert_script, record)
                
                
                
            update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)
            

            delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('James',)
            cur.execute(delete_script,delete_record)

            ##para print aqui no vscode, o cursor_factory=psycopg2.extras foi adicionadocur = conn.cursor(cursor_factory=psycopg2.extras)   
            cur.execute('SELECT * FROM EMPLOYEE')
            for record in cur.fetchall():
                print(record['name'],record['salary'])
            
        
        
            ##conn.commit()  -- se usar o conn = psycopg2.connect
except Exception as error:
    print(error)
    
finally:
    if conn is not None:
        conn.close()