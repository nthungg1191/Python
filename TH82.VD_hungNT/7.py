import mysql.connector 

# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root", 
        password = "", database = "pythondb") 
    
# tạo đối tượng cursor 
cur = myconn.cursor()   
    
try: 
    # tạo bảng Employee gồm 4 cột name, id, salary, và department id   
    dbs = cur.execute("create table Employee(name varchar(20) not null, " 
        + "id int(20) not null primary key, salary float not null, " 
        + "dept_id int not null)") 
except:  
    myconn.rollback() 

myconn.close()