print("Program to print star pattern: \n");
num_rows = int(input("Enter maximum stars you want display on a single line: "))
for i in range (0, num_rows):
    for j in range(0, i + 1):
        print("* ", end='')
    print("\r")
for i in range (num_rows, 0, -1):
    for j in range(0, i -1):
        print("* ", end='')
    print("\r")
    
'''
Program to print star pattern: 

Enter maximum stars you want display on a single line: 3
* 
* * 
* * * 
* * 
* 
'''