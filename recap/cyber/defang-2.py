# Defanged IP without build in string functoins

ip = "192.168.1.1"

def defang(ip):
    ans = ''
    for i in ip:
        if i == ".":
            i = ''
        else:
            ans += i
    print(ans)
    
defang(ip)
