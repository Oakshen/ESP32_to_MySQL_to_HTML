import socket
import datetime
import pymysql

# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 以下设置解决ctrl+c退出后端口号占用问题
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(('服务器的内网IP',8090)) #绑定要监听的地址（内网ip）和端口
server.listen(5) #开始监听 表示可以使用五个链接排队

#打开数据库连接
mysql_conn = pymysql.connect(user="xxxx",password="xxxxx",host="localhost",database="xxxxx",port=3306)
#获取游标

while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print(conn, addr)
    try:
        data = conn.recv(1024)  #接收数据
        if data:
            print('Time:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            de_data=data.decode()
            print('recive:',de_data) #打印接收到的数据

            count =0
            //将数据保存到MySQL
            while (count<7):
                if de_data[count]=="Y":
                   cursor=mysql_conn.cursor()
                   m_count=count+1
                   cursor.execute("""UPDATE load2 set sta=1 where id=%s""",m_count)
                   #提交到数据库执行
                   mysql_conn.commit()
                   print('第',m_count,'个用电器数据修改成功')
                   count=count+1
                   cursor.close()#先关闭游标
                elif de_data[count]=="N":
                   cursor=mysql_conn.cursor()
                   m_count=count+1
                   cursor.execute("""UPDATE load2 set sta=0 where id=%s""",m_count)
                    #提交到数据库执行
                   mysql_conn.commit()
                   print('第',m_count,'个用电器数据修改成功')
                   count=count+1
                   cursor.close()#先关闭游标   

    except ConnectionResetError as e:
        print('关闭了正在占线的链接！')
        break
    # conn.close()
    //按Ctrl+C结束程序
