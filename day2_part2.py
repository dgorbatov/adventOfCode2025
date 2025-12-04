with open("day2.txt", 'r') as f:
    contents = f.read()

ret = 0
for range_str in contents.split(","):
# for range_str in ["1188511880-1188511890"]:
    start, end = range_str.split("-")
    
    start = int(start)
    end = int(end)
    
    for i in range(start,end + 1):
        # find if id is valid
        id = str(i)
        invalid = False
        
        n = len(id)
        for pattern_len in range(1, n // 2 + 1):
            if n % pattern_len == 0:
                pattern = id[:pattern_len]
                repetitions = n // pattern_len
                if repetitions >= 2:
                    if id == pattern * repetitions:
                        invalid = True
                
        if invalid:
            print("Invalid: ", id)
            ret += int(id)            
        # print("--------")
print(ret)
print("-------------")