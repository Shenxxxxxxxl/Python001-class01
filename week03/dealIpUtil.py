def ip2num(ip):
    ips = [int(x) for x in ip.split('.')]
    return ips[0]<< 24 | ips[1]<< 16 | ips[2] << 8 | ips[3]

def num2ip (num):
    return '%s.%s.%s.%s' % ((num >> 24) & 0xff, (num >> 16) & 0xff, (num >> 8) & 0xff, (num & 0xff))


def gen_ip(ip):
    start ,end = [ip2num(x) for x in ip.split('-')]
    return [num2ip(num) for num in range(start,end+1) if num & 0xff]

if __name__ == '__main__':
    a_ip = '192.168.1.1'
    if '-' in a_ip:
        print(1)
    else:
        print(2)
    a_len = a_ip.split('-')
    print(len(a_len))
    print(a_ip.index('-'))
    # if a_ip.index('-'):
    #     arr = gen_ip('192.168.1.1')
    # else:
    #     arr =[a_ip]
    # if arr:
    #     print(1)
    # else:
    #     print(2)
    # print(len(arr))