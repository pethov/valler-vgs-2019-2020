

'''
class Diff:
    
    def diff1(self,f, x, h=1E-5):
        return (f(x+h) - f(x))/h

    def diff2(self,f,x,h=1E-5):
        return (f(x) - f(x-h))/h

    def diff3(self,f,x,h=1E-5):
        return (f(x+h) - f(x-h))/(2*h)

    def diff4(self,f,x,h=1E-5):
        return (-f(x+2*h)+8*f(x+h) - 8*f(x-h)+f(x-2*h))/(12*h)

class Y:
    def __init__(self,v0):
        self.v0= v0
    
        
            
    def value(self,t):
        return sin(t*self.v0)
      
    





y1 = Y(2*pi)


dy1dt = diff1(y1.value, 0.1)
dy2dt = diff2(y1.value, 0.1)
dy3dt = diff3(y1.value, 0.1)
dy4dt = diff4(y1.value, 0.1)

#print ('y(t=%g; v0=%g) = %g' % (t, y.v0, v))
#print( y.formula())
print(dy1dt)
print(dy2dt)
print(dy3dt)
print(dy4dt)


from pylab import*

class Grunnstoff: 
    def __init__ (self, a_num, sym, navn, masse, el_neg):
        self.a_num = a_num
        self.sym = sym
        self.navn = navn 
        self.masse = masse 
        self.el_neg = el_neg 
    def sjekk(self): 
        return self.a_num, self.sym, self.navn, self.masse, self.el_neg
    
Karbon = Grunnstoff(6,"C", "Karbon", 12.01, 2.5)

Litium = Grunnstoff(3, "Li", "Litium", 6.941, 1.0)

Fluor = Grunnstoff(9, "F", "Fluor", 19.00, 4.0)

Brom = Grunnstoff(35, "Br", "Brom", 79.9, 3.0)

Klor = Grunnstoff(17, "Cl", "Klor", 35.45, 3.2)

Kalium = Grunnstoff(19, "K", "Kalium", 39.10, 0.8)

Oksygen = Grunnstoff(8, "O", "Oksygen", 16.00, 3.5)

Hydrogen = Grunnstoff(1, "H", "Hydrogen", 1.008, 2.1)

def bindingstype(grunnstoff1, grunnstoff2):
    bipbop = grunnstoff1.el_neg
    heihei = grunnstoff2.el_neg
    forskjell = heihei -bipbop
    if forskjell >= 2.0 :
        print("Dette er en ionebinding")
    elif forskjell < 2.0 and forskjell > 1.6 :
        print("Dette kan være en ionisk binding og en polar kovalent binding")
    elif forskjell <= 1.6 and forskjell >= 0.5 : 
        print("Dette er en polar binding") 
    elif forskjell <  0.5 and forskjell > 0.3 : 
        print("Denne bindingen er mellom en polar og en polar kovalent")
    elif forskjell <= 0.3: 
        print("Dette er en upolar kovalent binding")
        
print("LiF:")
LiF =  bindingstype(Litium, Fluor)

print("\nBrCl:")
LiF =  bindingstype(Brom, Klor)

print("\nK2O:")
LiF =  bindingstype(Kalium, Oksygen)

print("\nCH4:")
LiF =  bindingstype(Karbon, Hydrogen)

'''
from pylab import*

class Grunnstoff: 
    def __init__ (self, a_num, sym, navn, masse, el_neg):
        self.a_num = a_num
        self.sym = sym
        self.navn = navn 
        self.masse = masse 
        self.el_neg = el_neg  
        
    def sjekk(self): 
        return self.a_num,self.sym,self.navn, self.masse,self.el_neg

karbon = Grunnstoff(6,"C", "Karbon", 12.01, 2.5)

litium = Grunnstoff(3, "Li", "Litium", 6.941, 1.0)

fluor = Grunnstoff(9, "F", "Fluor", 19.00, 4.0)

brom = Grunnstoff(35, "Br", "Brom", 79.9, 3.0)

klor = Grunnstoff(17, "Cl", "Klor", 35.45, 3.2)

kalium = Grunnstoff(19, "K", "Kalium", 39.10, 0.8)

oksygen = Grunnstoff(8, "O", "Oksygen", 16.00, 3.5)

hydrogen = Grunnstoff(1, "H", "Hydrogen", 1.008, 2.1)
 


   
def bindingstype(grunnstoff1, grunnstoff2):
    neg1 = grunnstoff1.el_neg
    neg2 = grunnstoff2.el_neg
    forskjell = neg2 - neg1
    if forskjell >= 2.0 :
        print("ionebinding")
    elif forskjell < 2.0 and forskjell > 1.6 :
        print("mellom ionebinding og polar kovalent binding")
    elif forskjell <= 1.6 and forskjell >= 0.5 : 
        print("polar binding") 
    elif forskjell <  0.5 and forskjell > 0.3 : 
        print("mellom polar og  upolar kovalent")
    elif forskjell <= 0.3: 
        print("upolar kovalent binding binding")
'''
def bindingstype(grunnstoff1, grunnstoff2):
    bipbop = grunnstoff1.el_neg
    heihei = grunnstoff2.el_neg
    forskjell = heihei -bipbop
    if forskjell >= 2.0 :
        print("Dette er en ionebinding")
    elif forskjell < 2.0 and forskjell > 1.6 :
        print("Dette kan være en ionisk binding og en polar kovalent binding")
    elif forskjell <= 1.6 and forskjell >= 0.5 : 
        print("Dette er en polar binding") 
    elif forskjell <  0.5 and forskjell > 0.3 : 
        print("Denne bindingen er mellom en polar og en polar kovalent")
    elif forskjell <= 0.3: 
        print("Dette er en upolar kovalent binding")
'''
print("LiF:")
LiF =  bindingstype(litium, fluor)

print("\nBrCl:")
LiF =  bindingstype(brom, klor)

print("\nK2O:")
LiF =  bindingstype(kalium, oksygen)

print("\nCH4:")
LiF =  bindingstype(karbon, hydrogen)
