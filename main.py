def insertion_sort_max(x):
    
    for i in range(1,len(x)):
    # i in range 1 to length of x, x is the array of numbers input
        j=i-1 #j is the index of the number before i
        key=x[i] #key is the number in the array
        while j>=0 and x[j]<key: #while j is remaining and the examining value index (not the value) is less than the numbers in array
            x[j+1]=x[j] #the value of the index is the value of the index before it
            j=j-1 #decrement j
        x[j+1]=key #the value of the index is the key
    return x

def insertion_sort_min(x):
    for i in range(1,len(x)):
        j=i-1
        key=x[i]
        while j>=0 and x[j]>key:
            x[j+1]=x[j]
            j=j-1
        x[j+1]=key
    return x
x = []
adds = input("Enter a list of numbers: ")
print( input)
x = adds.split() #split the numbers by the space between them and add to array
print (x)
x = [int(i) for i in x]
print("The list of numbers in ascending order is: ", insertion_sort_min(x))
print("The list of numbers in descending order is: ", insertion_sort_max(x))