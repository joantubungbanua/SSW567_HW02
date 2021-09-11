#Joan Marie Tubungbanua 09/11

def classify_triangle(a,b,c): 
    if(a==b==c): 
        return("equilateral triangle")
    elif((a==b and a != c) or (a==c and a!=b) or (b==c and b!=a)): 
        if((a**2)+(b**2)==(c**2)): 
            return("isoceles right triangle")
        else: 
            return("isoceles triangle")
   
    elif((a!=b and a!=c and b!=c)): 
        if((a**2)+(b**2)==(c**2)): 
            return("scalene right triangle")
        else:
            return("scalene triangle")
    

