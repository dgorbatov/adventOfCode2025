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
        end_idx = 1
        
        # print("ID")
        invalid = id[:len(id)//2] == id[len(id)//2:]
                
        if invalid:
            ret += int(id)            
        # print("--------")
print(ret)