#Simple Addition, ,,  
def simp_add(a, b):
    print ("The addition is " + str(a + b))

simp_add(2, 3)


#Simple subtraction
def simp_sub(a, b):
    print ("The subtraction is " + str(a - b))

simp_sub(5, 3)


#Simple division
def simp_div(a, b):
    print ("The division is " + str(a / b))

simp_div(10, 2)


#Simple multiplication
def simp_mul(a, b):
    print ("The multiplication is " + str(a * b))   

simp_mul(4, 2)

#Simple average
def simp_avg(a, b, c, d, e):
    print ("The average is " + str((a + b + c + d + e) / 5))

simp_avg(1, 2, 3, 4, 5)


#Simple Average
def avg(add, n):
    return ( sum(add)/ n)
    
add = 1,2,3,4,5
n = len(add)
Ans= avg(add, n)
print ("The average is "  + str(Ans))


#Weighted Average
def Weg_Avg(num, den):
    return (sum(num)/sum(den))

w1=2; x1=3; w2=4; x2=5; w3=6; x3=4; w4=2; x4=2; w5=4; x5=1
num = w1*x1, w2*x2, w3*x3, w4*x4, w5*x5
den = w1,w2,w3,w4,w5
Answer = Weg_Avg(num, den)
print ("The weighted average is " + str(Answer))


#Geometric Mean
def Geo_Mean(add, n):
    return pow(sum(add), (1/n))

add = 10,20,30,40,50
n   = 5
Ans = Geo_Mean(add,n)
print ("The Geometric mean is " + str(Ans))


#Harmonic Mean
def Harm_Mean(num, den):
    return(num/sum(den))

den = 2**(-1), 3**(-1), 4**(-1), 5**(-1), 6**(-1)
num = len(den)
Ans = Harm_Mean(num, den)  

print ("The Harmonic mean is " + str(Ans))


#Quadratic root
import math
#import cmath #It does not solve equations with complex roots.
def Quad_Root(a, b, c):
    print ("The Quadratic Root is given as  " + str((-b + (math.sqrt((b**2) - (4*a*c)))) / 2*a) +  " , " + str((-b - (math.sqrt((b**2) - (4*a*c)))) / 2*a))

Quad_Root(1,3,-4)

