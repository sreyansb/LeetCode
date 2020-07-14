class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xstr=bin(x)[2:]
        ystr=bin(y)[2:]
        xlen=len(xstr)
        ylen=len(ystr)
        if xlen>ylen:
            ystr="0"*(xlen-ylen)+ystr
            ylen=xlen
        elif ylen>xlen:
            xstr="0"*(ylen-xlen)+xstr
            xlen=ylen
        number=0
        for i in range(xlen):
            if xstr[i]!=ystr[i]:
                number+=1
        return number
        
