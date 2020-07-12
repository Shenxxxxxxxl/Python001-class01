
from concurrent.futures import ThreadPoolExecutor,as_completed
from multiprocessing import freeze_support
import datetime,sys,pickle
from dealIpUtil import gen_ip
import ping3,argparse,socket
import threading
mutex = threading.Lock()
def ping_one(host):
    pingTime=ping3.ping(host,timeout=1,unit='ms')
    if pingTime:
        print('%s is ok'%host)
        return host
    else:
        print('%s is fail'%host)
        return None

def tcp_one(ip,port):
    print("当前ip{0} 端口{1}".format(ip,port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建套接字
    sock.settimeout(1)   # 设置延时时间
    try:
        result = sock.connect_ex((ip, port))
        if result == 0: 
            print("{0}端口处于开放状态}".format(port))
            return port
    except Exception as e:
        #print("{0}exception -------{1}".format(port,e))
        pass
    finally:
        sock.close()     # 关闭套接字
    return None
    

def tcp_scan(dest):
    #探测目标主机是否开放了指定端口（1-1024）
    enale_port = []
    with ThreadPoolExecutor(max_workers=dest.Num) as executor:
        futures = {executor.submit(tcp_one, dest.Ip, i) : i for i in range(200 + 1)}
        for future in as_completed(futures):
            e_p = future.result()
            if e_p:
                enale_port.append(e_p)
        print(enale_port)
        if dest.file:
            if len(enale_port) < 1:
                print("无可用端口，无需写入")
                return
            with open( dest.file, 'w', newline='',encoding='utf-8') as f:
                f.write(str(enale_port))

def ping_scan(dest):
    enable_ip = []
    with ThreadPoolExecutor(max_workers=dest.Num) as executor:
        futures = executor.map(ping_one, dest.ip_arr)
        for future in futures:
            if future:
                enable_ip.append(future)
        print(enable_ip)
        if dest.file:
            if len(enable_ip) < 1:
                print("无可用IP，无需写入")
                return
            with open( dest.file, 'w', newline='',encoding='utf-8') as f:
                f.write(str(enable_ip))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #dest 设置这个选项的value解析出来后放到哪个属性中 type 类型 nargs - 指定这个参数后面的value有多少个
    parser.add_argument('-w', '--file', dest='file', type=str, help='保存文件名')
    parser.add_argument('-f', '--function', dest='Function', type=str, required=True, choices=['ping', 'tcp'] , default='ping', help='指定方法进行测试')
    parser.add_argument('-ip', '--ip', dest='Ip', type=str, required=True ,help='需要扫描的ip')
    parser.add_argument('-n', '--number', dest='Num', required=True,type=int, help='指定并发数量')
    print("----------------------")
    dest = parser.parse_args()
    ip_arr = []
    isTcp = False;
    if '-' in dest.Ip:
        try:
            ip_arr = gen_ip(dest.Ip)
        except Exception as e:
            print(e)
            print('ip格式不对')
            sys.exit()
    else:
        ip_arr.append(dest.Ip)
    dest.ip_arr = ip_arr
    print(dest)
    if ip_arr:
        if dest.Function == 'ping':
            ping_scan(dest)
        elif dest.Function == 'tcp':
            if len(ip_arr) < 2:
                tcp_scan(dest)
            else:
                #使用扫描器可以快速检测一个指定 IP 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
                print('扫描tcp端口只允许指定一个ip')
                sys.exit()
    else:
        print('ip格式不对')
        sys.exit()