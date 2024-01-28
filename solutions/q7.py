hjshd = [2]
vdsfdgdfg = 1_000_000_000

def urwue(n):
    for jkk in range(0, len(hjshd)):
        if n % hjshd[jkk] == 0:
            return False
    return True

def jhdsb(n):
    if len(hjshd) >= n:
        return hjshd[n-1]
    
    for ioplkj in range(max(hjshd)+1, vdsfdgdfg):
        if (urwue(ioplkj)):
            hjshd.append(ioplkj)
            if len(hjshd) == n:
                return hjshd[-1]

poiuy = int(input().strip())
for mnbvc in range(poiuy):
    hgfdsa = int(input().strip())
    print(jhdsb(hgfdsa))
