import re


with open("day3.txt", 'r') as f:
    contents = f.read()
banks = contents.split("\n")

ret = 0
for bank in banks:
    digit = []
    stack = []
    for idx, battery in enumerate(bank):
        if idx < 12:
            digit.append(battery)
            
            if len(digit) > 1 and int(digit[-2]) <= int(digit[-1]):
                stack.append(len(digit)-2)       
        elif len(stack) > 0 and int("".join(digit)) < int("".join(digit[:stack[0]])+"".join(digit[stack[0]+1:]) + battery):
            remove = stack.pop(0)
            digit.pop(remove)
            
            for idx in range(len(stack)):
                stack[idx] -= 1
            digit.append(battery)
        
            if len(digit) > 1 and int(digit[-2]) < int(digit[-1]):
                stack.append(len(digit)-1)
                
    if int(bank[-1]) > int(digit[-1]):
        digit[-1] = bank[-1]
    digit_str = ''.join(digit)
    print(digit_str)
        
    ret += int(digit_str)
print(ret)