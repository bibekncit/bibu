 #Find factors of any given number using concept of list
List = []
number = int(input("Enter any number you want to find Factors of:"))
for num in range(1,number+1):
    if number%num == 0:
        List.append(num)

print("The factors of ", number , "are: ")   
     
for list_num in range(len(List)):
    print(List[list_num])