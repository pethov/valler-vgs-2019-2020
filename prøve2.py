from pylab import*
# oppgave 4
def h(x):
    return 0.00868*x**2-1.66*x+87.4

def hder(x):
    return  0.00868*2*x-1.66

def c(x):
    return 0.000295*x**2+0.00554*x+35.7

def cder(x):
    return 0.000295*2*x+0.00554

N= 1000
t= 90
dt= t/N

nh= zeros(N)
nhder = zeros(N)
cl = zeros(N)
clder= zeros(N)
tid= zeros(N)


nh[0]=87.4
nhder[0]=-1.66
cl[0]=35.7
clder[0]=0.00554

p=0


for i in range (N-1):
    nh[i]=h(i)
    nhder[i]= hder(i)
    cl[i]=c(i)
    clder[i]=cder(i)
    nh[i+1]= nh[i]+nhder[i]*dt
    cl[i+1]= cl[i]+ dt
    tid[i+1]=tid[i]+dt
    while  h(p)!=c(p):
        p+=1
        
        
    

plot(tid,cl)
plot(tid,nh)
print(p)


    
    
plot(i,h)
'''
#oppgave 5
N = 10000
tid = 60
dt = tid / N

k =-0.1


T= zeros(N)
t = zeros(N)
Tder = zeros(N)

T[0]=75
t[0]=0


for i in range(N-1):
    Tder[i]=-0.16*(T[i]-21)
    T[i+1]= T[i]+ Tder[i]*dt
    t[i+1]= t[i] + dt
    
plot(t,T)
'''

    
    

