import mysql.connector 

myconn = mysql.connector.connect(host = "localhost", user = "root",  
passwd = "", database = "oidoioi") 
# in đối tượng connection ra màn hình 
print(myconn) 
# tạo đối tượng cursor 
cur = myconn.cursor() 
# in đối tượng cursor ra màn hình 
print(cur)