lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())

	lst.append(ele)  
print("Minimum value is:",min(lst))  
print("Array in reverse order: ");        
for i in range(len(lst )-1, -1, -1):     
    print(lst [i]),     
