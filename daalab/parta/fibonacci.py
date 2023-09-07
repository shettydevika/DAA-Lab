n = int(input ("Enter the number you want to print: "))     
# Take input from user that how many numbers you want to print  
a = 0    
b = 1    
for i in range(0,n):  
    print(a, end = " ")              
    c = a+b                      
    a = b                
    b = c  
    
'''
Enter the number you want to print: 10
0 1 1 2 3 5 8 13 21 34'''