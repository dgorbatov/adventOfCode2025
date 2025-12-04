with open("day1.txt", 'r') as f:
    contents = f.read()

num_zero = 0
curr_num = 50
for i in contents.split("\n"):
    num = int(i[1:])
    

    num_zero += (num // 100)
    num = num % 100

    if i[0] == "L":
        curr_num -= num
        
        if curr_num < 0:
            if curr_num + num != 0:
                print("add")
                num_zero += 1
            curr_num = curr_num % 100
    else:
        curr_num += num
        
        if curr_num >= 100:
            curr_num = curr_num % 100            
            
            if curr_num != 0:
                print("add")
                num_zero += 1

    print(curr_num)
    if curr_num == 0:
        num_zero += 1

print(num_zero)
            
        