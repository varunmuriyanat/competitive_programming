mapping = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z', 'y', 'z']

def num_of_ways(s):
    print(s)
    for i in range(len(s)-1, -1, -1):
        index = int(s[i:i+1])
        print(index, mapping[index]) 

        combined_idx = int(s[i:i+2])
        if (combined_idx > 9) and (combined_idx < len(mapping)-1):
            combined = mapping[combined_idx]
            print(combined_idx, combined)
        

num_of_ways("1221310")
print("")
num_of_ways("12")

