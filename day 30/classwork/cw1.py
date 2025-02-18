# lists
#append
#remove
#pop

my_list=["gvanca" , "gabrieli" , "giorgi" , "elene" , "vano"] 

numbers_list=[5 , 23 , 68 , 1 , 6 , 43 , 95 , 10 , 90 , 3]

print(len(numbers_list))

for i in range(len(numbers_list)):
    print(numbers_list[i])


for i in range (0 , 5):
    print(my_list[i])
    print(i)

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

#davbewdot mxolod luwi ricxvebi

for i in range(len(numbers_list)):
    if numbers_list[i] % 2 == 0:
        print(numbers_list[i])
   