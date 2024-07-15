list = [1,1,2,3,4,5,6,11]

def find_pair(list,target_number):
    for x in range(len(list)):
        for y in range(len(list)):
            if list[x]+list[y] == target_number:
                return (list[x],list[y])
            else:
                continue
    return None

print(find_pair(list,11))