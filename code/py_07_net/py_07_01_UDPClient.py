from socket import *

# 创建udp socket
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 准备接收方地址
# 192.168.1.19:8080(raspberry)
# 存储为元组，IP为字符串，端口为数字
dest_addr = ('192.168.1.19',8080)

# 获取输入的数据
send_data = input("请输入想要发送的数据")

# 发送
udp_socket.sendto(send_data.encode("utf-8"),dest_addr)

# 关闭socket
udp_socket.close()