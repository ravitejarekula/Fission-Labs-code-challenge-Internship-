TC=int(input())

for num in range(0,TC):
   N=int(input())
   for X in range(2,N+1): 
       if N%X == 0:      
         print (str(N - X)+" "+str(X)) 
         break  

