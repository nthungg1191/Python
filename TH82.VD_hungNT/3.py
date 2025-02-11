import mysql.connector 
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
passwd = "", database = "oidoioi") 
# in đối tượng connection ra màn hình 
print(myconn) 