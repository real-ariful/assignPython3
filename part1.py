#Part 1: Sale Price Table


#Imporitng the numpy library
import numpy as np
#Taking two arrays using np.arange(start, end, increment
x=np.arange(9.95, 50, 5) #array of price of the products
y=np.arange(5, 55, 5) #array of off percentage

print("Normal Price\t",end='')

#for loop for printing the regular prices of items
for i in range(0,len(x)):
    print("$"+str(x[i]),end='\t')
print("")

#for loop for printing the discounted prices of items    
for j in range(0,len(y)):
    print("\n off\t",str(y[j])+"%",end='\t')
    for k in range(0,len(x)):
        dp =(x[k]*(100-y[j])/100)
        print('{0:.2f}'.format(dp),end='\t')
    