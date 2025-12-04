with open("day3.txt", 'r') as f:
    contents = f.read()
banks = contents.split("\n")

ret = 0
for bank in banks:
    first = -1
    second = -1
    
    for battery in bank[:-1]:
        if int(battery) > first:
            first = int(battery)
            second = -1
        elif int(battery) > second:
            second = int(battery)
            
    if int(bank[-1]) > second:
        second = int(bank[-1])
        
    ret += first * 10 + second
print(ret)