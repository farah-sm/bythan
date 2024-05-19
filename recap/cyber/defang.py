ip = "192.168.1.1"

def defang(ip):
    ip = (ip.replace(".", ""))
    print(ip)
    
defang(ip)
