import mysql.connector 
  
#tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "", database = "PythonDB") 
  
#tạo đối tượng cursor 
cur = myconn.cursor() 
  
try: 
    cur.execute("SELECT name, id, salary FROM Employee") 
      
    # tìm nạp các hàng từ đối tượng con trỏ   
    result = cur.fetchall() 
  
    for x in result: 
        print(x);  
  
except: 
    myconn.rollback() 
  
myconn.close() 