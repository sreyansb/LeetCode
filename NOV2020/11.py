#attempt1: VERY DIFFICULT, GOT 5 WAs
from math import inf,atan,pi,floor
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        #p1 is the base point
        distp1p2=((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
        distp1p3=((p1[0]-p3[0])**2+(p1[1]-p3[1])**2)**0.5
        distp1p4=((p1[0]-p4[0])**2+(p1[1]-p4[1])**2)**0.5
        print(distp1p2,distp1p3,distp1p4,distp1p2==distp1p4,distp1p3**2+distp1p4**2,distp1p2**2)
        if distp1p2 and distp1p2==distp1p3 and abs(distp1p2**2+distp1p3**2-distp1p4**2)<1:
            try:
                m1=(p2[1]-p1[1])/(p2[0]-p1[0])
            except:
                m1=inf
            try:
                m2=(p3[1]-p1[1])/(p3[0]-p1[0])
            except:
                m2=inf
            try:
                m3=(p2[1]-p4[1])/(p2[0]-p4[0])
            except:
                m3=inf
            try:
                m4=(p3[1]-p4[1])/(p3[0]-p4[0])
            except:
                m4=inf
            #print(m1,m2)
            if (m1==inf and m2==0) or (m1==0 and m2==inf) or 1+m1*m2<0.005:
                if (m3==inf and m4==0) or (m3==0 and m4==inf) or 1+m1*m2<0.005 or atan(abs(m4-m3)/(1+m3*m4))==pi/2 :
                    return True
                else:
                    return False
            if atan(abs(m2-m1)/(1+m1*m2))==pi/2:
                return True
            return False
        elif distp1p2 and distp1p2==distp1p4 and abs(distp1p2**2+distp1p4**2-distp1p3**2)<1:
            try:
                m1=(p2[1]-p1[1])/(p2[0]-p1[0])
            except:
                m1=inf
            try:
                m2=(p4[1]-p1[1])/(p4[0]-p1[0])
            except:
                m2=inf
            if (m1==inf and m2==0) or (m1==0 and m2==inf) or 1+m1*m2<0.005:
                return True
            if atan(abs(m2-m1)/(1+m1*m2))==pi/2:
                return True
            return False
        elif distp1p3 and distp1p3==distp1p4 and abs(distp1p4**2+distp1p3**2-distp1p2**2)<1:
            try:
                m1=(p4[1]-p1[1])/(p4[0]-p1[0])
            except:
                m1=inf
            try:
                m2=(p3[1]-p1[1])/(p3[0]-p1[0])
            except:
                m2=inf
            #print(m1,m2)
            if (m1==inf and m2==0) or (m1==0 and m2==inf) or 1+m1*m2<0.005:
                return True
            if atan(abs(m2-m1)/(1+m1*m2))==pi/2:
                return True
            return False
        else:
            return False
        
